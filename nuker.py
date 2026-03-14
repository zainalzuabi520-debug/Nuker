import os
import time
import sys

# --- CONFIG ---
AUTHOR = "Zain"
VERSION = "8.5.0-MANUAL"
FOLDER = "Nuker_Data"
LOG_FILE = f"{FOLDER}/passwords.txt"

# Create the master folder if it doesn't exist
if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def header():
    os.system('clear')
    print("\033[92m" + "="*70)
    print(r"""
  _   _ _   _ _  _______ _____  
 | \ | | | | | |/ / ____|  __ \ 
 |  \| | | | | ' /|  __| | |__) |
 | |\  | |_| |  < | |____|  _  / 
 |_| \_|\___/|_|\_\______|_| \_\ 
    """)
    print(f" [C2 PANEL]: v{VERSION} | [DEV]: {AUTHOR}")
    print("="*70 + "\033[0m")

def footer(msg):
    print("\033[92m" + "="*70)
    print(f" [LIVE LOG]: \033[93m{msg}\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")

def main_menu(status="SYSTEM READY"):
    header()
    print("\033[92m [1] MANUALLY CAPTURE HIT (Enter User/Pass)")
    print(" [2] GENERATE EMAIL HTML (Creates .html file)")
    print(" [3] BUILD PAYLOAD (.EXE Simulation)")
    print(" [4] BROWSE FOLDER (View all created files)")
    print(" [5] EXIT")
    print("-" * 70)
    footer(status)
    
    choice = input("\n\033[92mNUKER > \033[0m").strip()
    
    if choice == "1":
        manual_hit()
    elif choice == "2":
        make_email()
    elif choice == "3":
        make_payload()
    elif choice == "4":
        list_files()
    elif choice == "5":
        sys.exit()

def manual_hit():
    header()
    plat = input("[?] Platform Name: ")
    user = input("[?] Target Username: ")
    pw = input("[?] Target Password: ")
    
    # Writing to the log file so it is saved
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {plat} | USER: {user} | PASS: {pw}\n")
    
    main_menu(f"SUCCESS: Captured {user} on {plat}")

def make_email():
    header()
    name = input("[?] Name for HTML file (e.g., login): ")
    path = f"{FOLDER}/{name}.html"
    
    # Writing actual HTML content to the file
    content = f"<html><body><h2>{name.upper()} LOGIN</h2><input type='text' placeholder='Username'><br><input type='password' placeholder='Password'><br><button>Login</button></body></html>"
    with open(path, "w") as f:
        f.write(content)
    
    print(f"\n\033[92m[!] File created: {path}\033[0m")
    time.sleep(2)
    main_menu(f"Created {name}.html in Nuker_Data")

def make_payload():
    header()
    name = input("[?] Payload Name (e.g., exploit.exe): ")
    path = f"{FOLDER}/{name}"
    
    print("[*] Compiling...")
    time.sleep(2)
    
    # Writing a simulated binary string to the file
    with open(path, "w") as f:
        f.write("BINARY_DATA_OBFUSCATED_v8.5")
    
    print(f"\n\033[92m[!] File created: {path}\033[0m")
    time.sleep(2)
    main_menu(f"Saved {name} to Nuker_Data")

def list_files():
    header()
    print(f"\033[92m--- DIRECTORY: ./{FOLDER} ---\033[0m")
    for item in os.listdir(FOLDER):
        print(f" [+] {item}")
    input("\nPress Enter to return...")
    main_menu()

if __name__ == "__main__":
    main_menu()
