import os
import subprocess
import shutil
import sys
import argparse

def get_available_engines():
    """Checks the system PATH and workspace bin/ for available LaTeX engines."""
    engines = ['pdflatex', 'xelatex', 'lualatex', 'tectonic', 'latexmk']
    available = []
    
    # Check workspace bin/tectonic.exe
    local_tectonic = os.path.join(os.getcwd(), 'bin', 'tectonic.exe')
    if os.path.exists(local_tectonic):
        available.append('tectonic_local')
        
    for eng in engines:
        if shutil.which(eng) is not None:
            available.append(eng)
    return available

def compile_latex(tex_file, engine=None, clean=True):
    """Compiles a latex file using the first available engine or a specified one."""
    if not os.path.exists(tex_file):
        print(f"[-] Error: File not found: {tex_file}")
        return False

    available = get_available_engines()
    if not available:
        print("[-] Error: No LaTeX compilers found in your PATH or local bin/.")
        print("    Please install MikTeX, TeX Live, or Tectonic and try again.")
        print("    MikTeX: https://miktex.org/")
        print("    Tectonic (Recommended & Light): https://tectonic-typesetting.github.io/")
        return False

    if engine:
        if engine not in available:
            print(f"[-] Warning: Specified engine '{engine}' is not installed. Falling back.")
            engine = available[0]
    else:
        # Preference order
        pref = ['tectonic_local', 'tectonic', 'latexmk', 'xelatex', 'pdflatex', 'lualatex']
        selected = None
        for p in pref:
            if p in available:
                selected = p
                break
        engine = selected or available[0]

    print(f"[+] Using LaTeX Engine: '{engine}' to compile '{tex_file}'...")
    
    success = False
    try:
        if engine == 'tectonic_local':
            local_tectonic = os.path.join(os.getcwd(), 'bin', 'tectonic.exe')
            cmd = [local_tectonic, tex_file]
        elif engine == 'tectonic':
            cmd = ['tectonic', tex_file]
        elif engine == 'latexmk':
            cmd = ['latexmk', '-pdf', '-interaction=nonstopmode', tex_file]
        else:
            cmd = [engine, '-interaction=nonstopmode', tex_file]

        # Run compilation
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        if result.returncode == 0:
            print("[+] CV compiled successfully!")
            success = True
        else:
            print(f"[-] Compilation failed with return code {result.returncode}.")
            print("--- Compiler Output ---")
            print(result.stdout[-1000:]) # Print last 1000 chars of output
            print("-----------------------")
    except Exception as e:
        print(f"[-] Error running compiler: {e}")
        return False

    if success and clean:
        cleanup_aux_files(tex_file)

    return success

def cleanup_aux_files(tex_file):
    """Removes standard LaTeX auxiliary files to keep workspace tidy."""
    base_name = os.path.splitext(tex_file)[0]
    extensions = ['.aux', '.log', '.out', '.toc', '.synctex.gz', '.fls', '.fdb_latexmk']
    cleaned = []
    for ext in extensions:
        file_path = base_name + ext
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                cleaned.append(ext)
            except Exception as e:
                pass
    if cleaned:
        print(f"[+] Cleaned up auxiliary files: {', '.join(cleaned)}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LaTeX CV Compiler Tool")
    parser.add_argument("tex_file", help="Path to the LaTeX file to compile")
    parser.add_argument("--engine", help="Force a specific compiler (e.g. pdflatex, xelatex, tectonic)")
    parser.add_argument("--no-clean", action="store_true", help="Do not clean up auxiliary files after build")
    
    args = parser.parse_args()
    success = compile_latex(args.tex_file, engine=args.engine, clean=not args.no_clean)
    sys.exit(0 if success else 1)
