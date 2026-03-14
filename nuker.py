import os
import time
import sys
import random
import string

AUTHOR = "Zain"
VERSION = "6.5.0-PRO"
FOLDER_NAME = "Nuker_Data"
LOG_FILE = f"{FOLDER_NAME}/passwords.txt"

# Ensure the data folder exists
if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def draw_logo():
    """This is your Terminal Logo."""
    print("\033[92m") # Neon Green
    print(r"""
  _   _ _   _ _  _______ _____  
 | \ | | | | | |/ / ____|  __ \ 
 |  \| | | | | ' /|  __| | |__) |
 | |\  | |_| |  < | |____|  _  / 
 |_| \_|\___/|_|\_\______|_| \_\ 
    """)
    print("="*60)
    print(f" [SYSTEM]: NUKER C2 INTERFACE | v{VERSION}")
    print(f" [CREDIT]: MADE BY {AUTHOR}")
    print("="*60 + "\033[0m")

def main_menu(last_action="Waiting for command..."):
    draw_logo()
    print("\033[92m [1] DEPLOY PHISH LURE (100+ Platforms)")
    print(" [2] COMPILE MALWARE PAYLOAD")
    print(" [3] VIEW SAVED LEAKS (passwords.txt)")
    print(" [4] DELETE ALL SAVED DATA")
    print(" [5] EXIT")
    print("-" * 60)
    print(f"\033[93m [LAST EVENT]: {last_action}\033[0m")
    
    cmd = input("\n\033[92mNUKER_C2 > \033[0m").strip()
    
    if cmd == "1":
        run_phish()
    elif cmd == "2":
        run_malware()
    elif cmd == "3":
        view_data()
    elif cmd == "4":
        confirm_delete()
    elif cmd == "5":
        sys.exit()
    else:
        main_menu("Invalid command entered.")

def run_phish():
    draw_logo()
    platform = input("\033[92m[?] TARGET PLATFORM (e.g. Roblox): \033[0m")
    target = input("\033[92m[?] TARGET EMAIL/USER: \033[0m")
    
    print("\n[*] Initializing Tunnel...")
    time.sleep(1)
    
    # This is the 'Leak' logic—it generates and SAVES data
    fake_pass = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    link = f"https://{platform.lower()}-security-access.nuker.io/auth"
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {platform} | User: {target} | PWD: {fake_pass}\n")
    
    print(f"[*] PUBLIC LINK: \033[93m{link}\033[0m")
    input("\n[!] DATA CAPTURED. Press Enter to return to main menu...")
    main_menu(f"Leaked {platform} credentials for {target}")

def run_malware():
    draw_logo()
    print("[*] BUILDING MALWARE PAYLOAD...")
    for i in range(1, 11):
        time.sleep(0.2)
        sys.stdout.write(f"\r    Encryption: [{'#'*i}{'.'*(10-i)}] {i*10}%")
        sys.stdout.flush()
    print(f"\n\n\033[92m[!] Success: payload_v{VERSION}.exe generated.\033[0m")
    input("\nPress Enter...")
    main_menu("Malware Compilation Successful")

def view_data():
    draw_logo()
    print(f"\033[92m--- DATABASE: ./{LOG_FILE} ---\033[0m\n")
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("Database is currently empty.")
    input("\nPress Enter...")
    main_menu()

def confirm_delete():
    draw_logo()
    confirm = input("\033[91m[!] ARE YOU SURE? THIS DELETES ALL LEAKS (y/n): \033[0m")
    if confirm.lower() == 'y':
        if os.path.exists(LOG_FILE):
            os.remove(LOG_FILE)
        main_menu("All data wiped successfully.")
    else:
        main_menu("Wipe cancelled.")

if __name__ == "__main__":
    main_menu()
