import os
import sys
import argparse
import subprocess

# Determine directories
AGENTS_DIR = os.path.dirname(os.path.abspath(__file__))
SKILLS_DIR = os.path.join(AGENTS_DIR, 'skills')

def run_skill(skill_subpath, args):
    script_path = os.path.join(SKILLS_DIR, skill_subpath)
    if not os.path.exists(script_path):
        print(f"[-] Skill runner not found: {script_path}")
        return False
        
    cmd = [sys.executable, script_path] + args
    try:
        result = subprocess.run(cmd, text=True)
        return result.returncode == 0
    except Exception as e:
        print(f"[-] Error invoking skill: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Unified AI Agent Workspace CLI - LaTeX CV Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Agent Operations")

    # Command: compile
    parser_compile = subparsers.add_parser("compile", help="Compile LaTeX CV using installed engines")
    parser_compile.add_argument("file", nargs="?", default="src/my_cv.tex", help="Path to LaTeX source file")
    parser_compile.add_argument("--engine", help="Override engine (e.g. tectonic, pdflatex)")
    parser_compile.add_argument("--no-clean", action="store_true", help="Retain cache logs")

    # Command: analyze-ats
    parser_ats = subparsers.add_parser("analyze-ats", help="Audit resume text searchability and ATS parsing layout")
    parser_ats.add_argument("file", nargs="?", default="src/my_cv.tex", help="Path to LaTeX source file")

    # Command: polish-content
    parser_coach = subparsers.add_parser("polish-content", help="Polish resume bullets against Google XYZ standards")
    parser_coach.add_argument("file", nargs="?", default="src/my_cv.tex", help="Path to LaTeX source file")

    args, extra_args = parser.parse_known_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if args.command == "compile":
        # Pass compiler arguments
        cmd_args = [args.file]
        if args.engine:
            cmd_args += ["--engine", args.engine]
        if args.no_clean:
            cmd_args += ["--no-clean"]
        success = run_skill("latex-compiler/compiler.py", cmd_args)
        sys.exit(0 if success else 1)

    elif args.command == "analyze-ats":
        success = run_skill("ats-analyzer/ats_analyzer.py", [args.file])
        sys.exit(0 if success else 1)

    elif args.command == "polish-content":
        success = run_skill("content-coach/content_coach.py", [args.file])
        sys.exit(0 if success else 1)

if __name__ == '__main__':
    main()
