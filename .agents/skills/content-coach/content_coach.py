import os
import re
import sys
import argparse

ACTION_VERBS = {
    # English Action Verbs & Present-Tense counterparts
    'engineered', 'developed', 'built', 'architected', 'spearheaded', 'led', 'managed',
    'optimized', 'streamlined', 'designed', 'automated', 'refactored', 'implemented', 
    'pioneered', 'directed', 'coordinated', 'mentored', 'accelerated', 'launched',
    'increased', 'decreased', 'reduced', 'saved', 'generated', 'cultivated', 'established',
    'formulated', 'analyzed', 'investigated', 'conducted', 'deployed', 'integrated',
    'supported', 'performed', 'delivered', 'facilitated', 'configured', 'handled',
    'partnered', 'conducted', 'provide', 'manage', 'monitor', 'implement', 'partner',
    'support', 'configure', 'perform', 'deliver', 'facilitate', 'handle',
    'assisted', 'assist', 'coordinate', 'automate',
    
    # Vietnamese Action Verbs & Compound Prefixes
    'quản lý', 'triển khai', 'thiết kế', 'xây dựng', 'phát triển', 'tích hợp', 'thiết lập', 
    'tối ưu', 'tối ưu hóa', 'giám sát', 'khắc phục', 'bảo trì', 'vận hành', 'hỗ trợ', 
    'tổ chức', 'đào tạo', 'chủ động', 'trực tiếp', 'nghiên cứu', 'phối hợp', 'lắp đặt', 
    'tham gia', 'xử lý', 'bảo dưỡng',
    
    # Vietnamese Single-Syllable Action Prefixes (for space-split compatibility)
    'quản', 'triển', 'thiết', 'xây', 'phát', 'tích', 'tối', 'giám', 'khắc', 'bảo', 
    'vận', 'hỗ', 'tổ', 'đào', 'chủ', 'trực', 'nghiên', 'phối', 'lắp', 'tham', 'xử', 'cài'
}

FORBIDDEN_PRONOUNS = {'i', 'me', 'my', 'we', 'our', 'us', 'you', 'your'}

class ContentAgent:
    def __init__(self, filepath):
        self.filepath = filepath
        self.bullets = []
        self.reports = []

    def load_bullets(self):
        """Extracts all resumeItem blocks and item lists from custom environments."""
        if not os.path.exists(self.filepath):
            print(f"[-] File '{self.filepath}' not found.")
            return False

        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Extract \resumeItem{...}
        matches = re.findall(r'\\resumeItem\{((?:[^{}]|\{[^{}]*\})*)\}', content, re.DOTALL)
        self.bullets = [m.strip().replace('\n', ' ') for m in matches]

        # 2. Extract \item ... inside rSubsection environments
        rsubsection_matches = re.findall(r'\\begin\{rSubsection\}(.*?)\\end\{rSubsection\}', content, re.DOTALL)
        for rsub in rsubsection_matches:
            items = re.findall(r'\\item\s+([^\\]*(?:\\(?!item)[^\\]*)*)', rsub, re.DOTALL)
            for it in items:
                cleaned = it.strip().replace('\n', ' ')
                cleaned = re.sub(r'\s+', ' ', cleaned).strip()
                if cleaned:
                    self.bullets.append(cleaned)

        # 3. Extract \item ... inside experience/extracurricular rSection lists
        rsection_matches = re.findall(r'\\begin\{rSection\}\{([^}]+)\}(.*?)\\end\{rSection\}', content, re.DOTALL)
        for name, body in rsection_matches:
            if 'tabular' not in body and 'rSubsection' not in body:
                items = re.findall(r'\\item\s+([^\\]*(?:\\(?!item)[^\\]*)*)', body, re.DOTALL)
                for it in items:
                    cleaned = it.strip().replace('\n', ' ')
                    cleaned = re.sub(r'\\hfill.*$', '', cleaned).strip() # strip out trailing dates/hfills
                    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
                    if cleaned:
                        self.bullets.append(cleaned)

        return True

    def analyze_bullets(self):
        """Analyzes each bullet point against standards and compiles a feedback report."""
        self.load_bullets()
        if not self.bullets:
            print("[-] No resume bullet points found (\\resumeItem{...}) to analyze.")
            return []

        self.reports = []
        for i, bullet in enumerate(self.bullets, 1):
            feedback = {
                'id': i,
                'original': bullet,
                'score': 100,
                'suggestions': [],
                'is_strong': True
            }

            clean_text = re.sub(r'\\[a-zA-Z]+', '', bullet) 
            clean_text = re.sub(r'[{}\[\]%]', '', clean_text) 
            words = [w.lower().strip('.,:;()""') for w in clean_text.split()]
            words = [w for w in words if w]

            if not words:
                continue

            found_pronouns = [w for w in words if w in FORBIDDEN_PRONOUNS]
            if found_pronouns:
                feedback['score'] -= 20
                feedback['suggestions'].append(
                    f"Pronoun Warning: Avoid personal pronouns ({', '.join(set(found_pronouns))}). "
                    "Resumes should always be written in the implicit third-person passive."
                )
                feedback['is_strong'] = False

            first_word = words[0]
            if first_word not in ACTION_VERBS:
                feedback['score'] -= 15
                feedback['suggestions'].append(
                    f"Weak Start: The bullet starts with '{bullet.split()[0]}'. "
                    "Always start accomplishment bullets with a strong, active verb in the past tense (e.g., Engineered, Spearheaded, Optimized)."
                )
                feedback['is_strong'] = False

            has_metric = any(re.search(r'\d+|%', w) for w in words)
            has_metric = has_metric or any(w in ['million', 'billion', 'percent', 'k', 'k$', 'm$', 'api'] for w in words)
            
            if not has_metric:
                feedback['score'] -= 15
                feedback['suggestions'].append(
                    "Missing Metric: This statement lacks a quantifiable number, percentage, or currency figure. "
                    "Use the STAR/XYZ formula to prove your impact."
                )
                feedback['is_strong'] = False

            word_count = len(words)
            if word_count > 35:
                feedback['score'] -= 10
                feedback['suggestions'].append(
                    f"Too Long: Bullet is {word_count} words. "
                    "Aim for exactly 1-2 lines in the PDF. Condense your phrasing."
                )
                feedback['is_strong'] = False
            elif word_count < 8:
                feedback['score'] -= 10
                feedback['suggestions'].append(
                    f"Too Short: Bullet is only {word_count} words. "
                    "This statement is likely too vague. Expand on the action taken and the result achieved."
                )
                feedback['is_strong'] = False

            feedback['score'] = max(0, feedback['score'])
            self.reports.append(feedback)

        return self.reports

    def print_analysis(self):
        self.analyze_bullets()
        if not self.reports:
            return

        print("=" * 60)
        print("         RESUME BULLET POINT IMPROVEMENT REPORT         ")
        print("=" * 60)
        print(f"Analyzing {len(self.reports)} bullet points inside: {os.path.basename(self.filepath)}\n")

        weak_count = 0
        for r in self.reports:
            if not r['is_strong']:
                weak_count += 1
                print(f"[Bullet #{r['id']}] Score: {r['score']}/100")
                print(f"  Content: \"{r['original'][:100]}...\"" if len(r['original']) > 100 else f"  Content: \"{r['original']}\"")
                print("  Suggestions for improvement:")
                for sugg in r['suggestions']:
                    print(f"    * {sugg}")
                print("-" * 60)

        if weak_count == 0:
            print("[+] Phenomenal work! All bullet points are extremely strong, action-oriented, and contain key metrics.")
        else:
            print(f"[!] Coach Summary: Found {weak_count} bullet points that can be polished for higher impact.")
        print("=" * 60)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LaTeX CV Content Coach")
    parser.add_argument("tex_file", help="Path to the LaTeX file to analyze")
    args = parser.parse_args()
    
    coach = ContentAgent(args.tex_file)
    coach.print_analysis()
