import os
import time
import sys

# --- PERMANENT CONFIG ---
VERSION = "4.2.5-PRIVATE"
AUTHOR = "Zain"
LOG_FILE = "passwords.txt"

# This is the Whitelist you asked for - saved forever in the code
WHITELIST = [
    "Admin", 
    "DeveloperThecrew", 
    "Player_3", 
    "Player_4"
]

def clear():
    os.system('clear')

def header():
    clear()
    print("\033[92m") # Neon Green
    print("="*60)
    print("  _   _ _   _ _  _______ _____  ")
    print(" | \ | | | | | |/ / ____|  __ \ ")
    print(" |  \| | | | | ' /|  __| | |__) |")
    print(" | |\  | |_| |  < | |____|  _  / ")
    print(" |_| \_|\___/|_|\_\______|_| \_\ ")
    print("="*60)
    print(f" [SYSTEM]: NUKER C2 INTERFACE | v{VERSION}")
    print(f" [CREDIT]: made by {AUTHOR}")
    print("="*60)

def main_menu():
    header()
    print(f"\033[93m[!] ACTIVE SESSION: {WHITELIST[0]} (Whitelisted)\033[92m")
    print("-" * 60)
    print("[1] DEPLOY PHISH LURE (Email/Link)")
    print("[2] COMPILE MALWARE PAYLOAD")
    print("[3] VIEW CAPTURED DATA (passwords.txt)")
    print("[4] MANAGE WHITELIST (4 Players)")
    print("[5] EXIT")
    print("-" * 60)
    
    choice = input("\nNUKER > ")
    
    if choice == "1":
        deploy_lure()
    elif choice == "2":
        build_malware()
    elif choice == "3":
        view_logs()
    elif choice == "4":
        show_whitelist()
    elif choice == "5":
        sys.exit()
    else:
        main_menu()

def deploy_lure():
    header()
    print("[*] SELECTING TEMPLATE...")
    time.sleep(0.5)
    print("    [A] Discord Nitro | [B] Instagram | [C] Roblox")
    opt = input("\nTYPE > ").upper()
    target = input("[?] Enter Target Email/ID: ")
    
    print("\n[*] GENERATING ENCRYPTED LINK...")
    # This is the link logic you were looking for
    link = f"http://nuker-server.io/auth?id={int(time.time())}"
    print(f"[*] LINK CREATED: {link}")
    time.sleep(1)
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] TARGET: {target} | LINK: {link}\n")
    
    print(f"\n\033[97m[!] DATA SENT TO {LOG_FILE}\033[92m")
    input("\nPress Enter...")
    main_menu()

def build_malware():
    header()
    fname = input("[?] Malware Filename (e.g. nuker.exe): ")
    print(f"\n[*] INJECTING PAYLOAD INTO {fname}...")
    for i in range(1, 11):
        time.sleep(0.2)
        sys.stdout.write(f"\r    PROGRESS: [{'#' * i}{'.' * (10-i)}] {i*10}%")
        sys.stdout.flush()
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] BUILD: {fname} SUCCESSFUL\n")
        
    print(f"\n\n\033[97m[!] {fname} COMPILED IN /builds/\033[92m")
    input("\nPress Enter...")
    main_menu()

def view_logs():
    header()
    print(f"--- DATABASE ({LOG_FILE}) ---")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("Empty.")
    input("\nPress Enter...")
    main_menu()

def show_whitelist():
    header()
    print("--- NUKER AUTHORIZED USERS ---")
    for i, user in enumerate(WHITELIST, 1):
        status = "ONLINE" if i <= 2 else "OFFLINE"
        print(f"[{i}] {user.ljust(20)} | STATUS: {status}")
    print("-" * 60)
    print("[!] 4/4 Player Slots Allocated.")
    input("\nPress Enter to return...")
    main_menu()

if __name__ == "__main__":
    main_menu()
