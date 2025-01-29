import os

def scan_files_for_keyword(directory, keyword):
    
    found_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if keyword in content:
                        found_files.append(file_path)
                        print(f"[+] '{keyword}' found in: {file_path}")
            except (UnicodeDecodeError, PermissionError):
                continue

    if not found_files:
        print(f"[-] '{keyword}' not found in any files.")
    else:
        print(f"\n[+] Scan complete. Found '{keyword}' in {len(found_files)} file(s).")

if __name__ == "__main__":
    directory_to_scan = input("Taranacak dizini girin: ")
    keyword_to_search = input("Aramak istediğiniz kelimeyi girin: ")

    scan_files_for_keyword(directory_to_scan, keyword_to_search)