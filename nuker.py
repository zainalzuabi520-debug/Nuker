import os
import time
import sys
import random
import string

# --- CONFIGURATION ---
AUTHOR = "Zain"
VERSION = "6.1.0-CLEAN"
FOLDER_NAME = "Nuker_Data"
LOG_FILE = f"{FOLDER_NAME}/passwords.txt"

# --- INITIALIZE FOLDER ---
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def header():
    clear()
    print("\033[92m" + "="*70)
    print("  _   _ _   _ _  _______ _____     __  __ ______  _____          ")
    print(" | \ | | | | | |/ / ____|  __ \   |  \/  |  ____|/ ____|   /\    ")
    print(" |  \| | | | | ' /|  __| | |__) |  | \  / | |__  | |  __   /  \   ")
    print(" | |\  | |_| |  < | |____|  _  /   | |\/| |  __| | | |_ | / /\ \  ")
    print(" |_| \_|\___/|_|\_\______|_| \_\   |_|  |_||____| \____|/_/  \_\ ")
    print("="*70)
    print(f" [SYSTEM]: NUKER FINAL C2 | v{VERSION}")
    print(f" [CREDIT]: made by {AUTHOR}")
    print("="*70 + "\033[0m")

def footer(msg="WAITING FOR COMMAND..."):
    print("\033[92m" + "="*70)
    print(f" [LAST CAPTURE]: \033[93m{msg}\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")

def main_menu(status="Ready"):
    header()
    print("\033[92m [1] SOCIAL MODULE (50+ Templates)")
    print(" [2] GAMING MODULE (30+ Templates)")
    print(" [3] EMAIL MODULE  (25+ Templates)")
    print(" [4] VIEW SAVED DATA (passwords.txt)")
    print(" [5] EXIT")
    print("-" * 70)
    footer(status)
    
    cmd = input("\033[92mNUKER_C2 > \033[0m").strip()
    
    if cmd in ["1", "2", "3"]:
        run_module(cmd)
    elif cmd == "4":
        view_data()
    elif cmd == "5":
        sys.exit()
    else:
        main_menu("Invalid Command")

def run_module(choice):
    header()
    platform = input("\033[92m[?] ENTER PLATFORM NAME: \033[0m")
    target = input("\033[92m[?] TARGET USERNAME/EMAIL: \033[0m")
    
    print(f"\n[*] Deploying {platform} Tunnel...")
    time.sleep(1.5)
    
    link = f"https://{platform.lower()}-secure-access.nuker.io/login"
    print(f"[*] PUBLIC LINK: \033[93m{link}\033[0m")
    
    # Generate random fake password for the display
    fake_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    status_update = f"CAP: [{target}] | PLAT: [{platform}] | PWD: [{fake_pass}]"
    
    with open(LOG_FILE, "a") as f:
        f.write(f"TIME: {time.ctime()} | PLAT: {platform} | USER: {target} | PWD: {fake_pass}\n")
    
    input("\n[!] DATA LOGGED. Press Enter to return...")
    main_menu(status_update)

def view_data():
    header()
    print(f"\033[92m--- DATABASE ENTRIES ---\033[0m\n")
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("No data found.")
    input("\nPress Enter...")
    main_menu()

if __name__ == "__main__":
    main_menu()
