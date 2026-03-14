import os
import time
import sys
import random
import string

# --- SETTINGS ---
AUTHOR = "Zain"
VERSION = "7.5.0-ULTRA"
FOLDER = "Nuker_Data"
DB = f"{FOLDER}/passwords.txt"

# Ensure folder is ready
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

def cmd_bar(msg):
    """This is the bottom bar that shows the captured User/Pass"""
    print("\033[92m" + "="*70)
    print(f" [LIVE FEED]: \033[93m{msg}\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")

def main(status="SYSTEM IDLE - WAITING FOR TARGET"):
    header()
    print("\033[92m [1] DEPLOY PHISH-LINK (100+ Platforms)")
    print(" [2] DEPLOY EMAIL-LURE (Direct Template)")
    print(" [3] COMPILE MALWARE (Full Device Control Sim)")
    print(" [4] VIEW DATABASE (All Leaked Creds)")
    print(" [5] EXIT")
    print("-" * 70)
    cmd_bar(status)
    
    choice = input("\033[92mNUKER > \033[0m").strip()
    
    if choice == "1" or choice == "2":
        run_capture(choice)
    elif choice == "3":
        run_malware()
    elif choice == "4":
        view_db()
    elif choice == "5":
        sys.exit()

def run_capture(type_id):
    header()
    mode = "LINK" if type_id == "1" else "EMAIL"
    plat = input(f"\033[92m[?] SELECT PLATFORM (e.g. Roblox/Discord): \033[0m")
    
    print(f"\n[*] Generating {plat} {mode}...")
    time.sleep(1.5)
    
    # Simulating the captured data
    u = f"User_{random.randint(10,99)}"
    p = "".join(random.choices(string.ascii_letters + string.digits, k=10))
    
    # Save to the one folder
    with open(DB, "a") as f:
        f.write(f"[{time.ctime()}] {plat} | USER: {u} | PASS: {p}\n")
    
    # Return to menu with the "Live Message" showing User/Pass
    main(f"NEW HIT! PLAT: {plat} | USER: {u} | PASS: {p}")

def run_malware():
    header()
    print("\033[92m[*] BUILDING REMOTE ACCESS PAYLOAD...")
    for i in range(1, 11):
        time.sleep(0.3)
        sys.stdout.write(f"\r    Status: [{'#'*i}{'.'*(10-i)}] {i*10}%")
        sys.stdout.flush()
    
    print(f"\n\n\033[92m[!] SUCCESS: Malware 'nuker_payload.exe' saved to {FOLDER}/")
    input("\nPress Enter to return...")
    main("MALWARE COMPILED - READY TO SEND")

def view_db():
    header()
    print("\033[92m--- FULL CAPTURE LOGS ---\033[0m\n")
    if os.path.exists(DB):
        with open(DB, "r") as f:
            print(f.read())
    else:
        print("No data in folder yet.")
    input("\nPress Enter...")
    main()

if __name__ == "__main__":
    main()
