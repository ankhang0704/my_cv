import re
import os
import sys
import argparse

class ATSAnalyzer:
    def __init__(self, filepath):
        self.filepath = filepath
        self.code = ""
        self.score = 100
        self.warnings = []
        self.positives = []

    def load_file(self):
        if not os.path.exists(self.filepath):
            print(f"[-] Error: File '{self.filepath}' not found.")
            return False
        with open(self.filepath, 'r', encoding='utf-8') as f:
            self.code = f.read()
        return True

    def analyze(self):
        self.load_file()
        if not self.code:
            return

        self._check_section_headers()
        self._check_layout_and_positioning()
        self._check_tables_and_grids()
        self._check_graphics_and_visual_bars()
        self._check_font_encoding()
        self._check_hyperlinks()
        
        # Ensure score does not drop below 0
        self.score = max(0, self.score)

    def _check_section_headers(self):
        """Checks for standard, ATS-parsable section headers."""
        standard_sections = {
            'experience': ['experience', 'work experience', 'professional experience', 'employment history', 'internship', 'training', 'position of responsibility', 'kinh nghiệm', 'lịch sử làm việc', 'quá trình làm việc'],
            'education': ['education', 'academic background', 'studies', 'học vấn', 'giáo dục', 'quá trình học tập'],
            'skills': ['skills', 'technical skills', 'core competencies', 'skills & technologies', 'kỹ năng', 'khả năng'],
            'projects': ['projects', 'selected projects', 'personal projects', 'technical projects', 'dự án', 'đề tài']
        }
        
        # Find all \section{...} and \begin{rSection}{...} definitions
        sections = re.findall(r'\\section\*?\{([^}]+)\}', self.code)
        rsections = re.findall(r'\\begin\{rSection\}\{([^}]+)\}', self.code)
        sections.extend(rsections)
        
        sections_lower = [s.lower().strip() for s in sections]
        
        for category, keywords in standard_sections.items():
            found = False
            for s in sections_lower:
                if any(kw in s for kw in keywords):
                    found = True
                    break
            
            if found:
                self.positives.append(f"Standard section for '{category.capitalize()}' detected.")
            else:
                self.score -= 10
                self.warnings.append(
                    f"Missing standard '{category.capitalize()}' section header. "
                    f"Make sure your header uses standard wording (e.g. {', '.join(keywords)})."
                )

    def _check_layout_and_positioning(self):
        """Checks for absolute positioning packages that might alter reading order in PDF streams."""
        bad_packages = {
            'textpos': "Absolute positioning package 'textpos' might result in out-of-order text rendering in the compiled PDF, confusing ATS readers.",
            'tcolorbox': "Highly stylized container boxes ('tcolorbox') can prevent some basic parsers from reading structural content.",
            'tikz': "Using 'tikz' for major structural components can hide text from standard text extraction processes."
        }
        
        for pkg, desc in bad_packages.items():
            if re.search(r'\\usepackage\*?\{[^\}]*' + pkg + r'[^\}]*\}', self.code):
                self.score -= 8
                self.warnings.append(f"Layout Warning: {desc}")

    def _check_tables_and_grids(self):
        """Checks for complex tables used for styling that could break ATS text extraction."""
        tables = re.findall(r'\\begin\{tabular', self.code)
        if len(tables) > 3:
            self.score -= 5
            self.warnings.append(
                f"Grid Warning: Detected {len(tables)} tables. "
                "Ensure tables are only used for listing structured tabular data, not as grids to align job experience bullets or paragraphs."
            )
        
        # Check for nested tables
        nested_check = len(re.findall(r'\\begin\{tabular\}.*?\\begin\{tabular\}', self.code, re.DOTALL))
        if nested_check > 0:
            self.score -= 12
            self.warnings.append(
                "Critical Layout Warning: Nested tables detected. "
                "ATS parsers are highly likely to read nested cells out of order."
            )

    def _check_graphics_and_visual_bars(self):
        """Checks for graphics, icons, and visual progress indicators representing competencies."""
        if 'progressbar' in self.code.lower() or 'progress' in self.code.lower() and 'bar' in self.code.lower():
            self.score -= 15
            self.warnings.append(
                "Critical Element Warning: Visual progress/skills bars detected. "
                "Do not use visual metrics or bar charts to rate your skills. ATS cannot parse these. Group skills by text lists instead."
            )

    def _check_font_encoding(self):
        """Checks that font encoding is set up correctly to guarantee clean text copy-paste."""
        if 'fontenc' not in self.code:
            self.score -= 5
            self.warnings.append(
                "Font Encoding Warning: '\\usepackage[T1]{fontenc}' not found in the preamble. "
                "Without proper font encoding, some PDF viewers and parsers might extract ligatures (like 'fi', 'fl', 'ff') incorrectly as special symbols."
            )

    def _check_hyperlinks(self):
        """Checks if hyperlinks have clean fallbacks and are parsed cleanly."""
        hrefs = re.findall(r'\\href\{([^}]+)\}\{([^}]+)\}', self.code)
        for url, text in hrefs:
            if '#' in url or '#' in text: # Ignore macro parameter variables
                continue
            if url.startswith('http') and len(text) < 4:
                self.score -= 3
                self.warnings.append(
                    f"Hyperlink Warning: Link with label '{text}' detected. "
                    "If the ATS strips formatting or prints the CV, critical URLs might be lost. "
                    "Make sure important links are descriptive or explicitly typed (e.g. 'github.com/user' instead of just 'GitHub')."
                )

    def print_report(self):
        print("=" * 60)
        print("          LATEX CV ATS COMPLIANCE AUDIT REPORT          ")
        print("=" * 60)
        print(f"File Checked: {os.path.basename(self.filepath)}")
        
        if self.score >= 85:
            score_color = "[EXCELLENT]"
        elif self.score >= 70:
            score_color = "[GOOD - MINOR ISSUES]"
        else:
            score_color = "[CRITICAL ATS COMPATIBILITY RISKS]"
            
        print(f"ATS Compliance Score: {self.score}/100  {score_color}")
        print("-" * 60)
        
        if self.positives:
            print("[+] PASSING CHECKS:")
            for p in self.positives:
                print(f"  * {p}")
            print("-" * 60)
            
        if self.warnings:
            print("[-] WARNINGS & REFACTOR RECOMMENDATIONS:")
            for i, w in enumerate(self.warnings, 1):
                print(f"  {i}. {w}")
        else:
            print("[+] Outstanding! No ATS readability warnings found. Your LaTeX file is beautifully structured.")
        
        print("=" * 60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LaTeX CV ATS Scanner")
    parser.add_argument("tex_file", help="Path to the LaTeX file to analyze")
    args = parser.parse_args()
    
    analyzer = ATSAnalyzer(args.tex_file)
    analyzer.analyze()
    analyzer.print_report()
    
    sys.exit(0 if analyzer.score >= 70 else 1)
