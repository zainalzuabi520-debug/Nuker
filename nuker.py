import os
import time
import sys

# --- SETTINGS ---
AUTHOR = "Zain"
VERSION = "10.0.0-LISTENER"
FOLDER = "Nuker_Data"
LOG_FILE = f"{FOLDER}/hits.txt"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def header():
    os.system('clear')
    print("\033[92m" + "="*75)
    print(r"""
  _   _ _   _ _  _______ _____  
 | \ | | | | | |/ / ____|  __ \ 
 |  \| | | | | ' /|  __| | |__) |
 | |\  | |_| |  < | |____|  _  / 
 |_| \_|\___/|_|\_\______|_| \_\ 
    """)
    print(f" [SYSTEM]: NUKER MULTI-TOOL | v{VERSION} | STATUS: ONLINE")
    print("="*75 + "\033[0m")

def footer(msg):
    print("\033[92m" + "="*75)
    print(f" [LISTENER FEED]: \033[93m{msg}\033[0m")
    print("\033[92m" + "="*75 + "\033[0m")

def main_menu(status="WAITING FOR INCOMING PACKETS..."):
    header()
    print("\033[92m [1] BUILD PRO PAGE (Discord/Insta/etc.)")
    print(" [2] START LIVE LISTENER (Capture Hits)")
    print(" [3] COMPILE CROSS-PLATFORM PAYLOAD")
    print(" [4] BROWSE LOCAL DATABASE")
    print(" [5] EXIT")
    print("-" * 75)
    footer(status)
    
    choice = input("\n\033[92mNUKER_C2 > \033[0m").strip()
    
    if choice == "1":
        build_page()
    elif choice == "2":
        start_listener()
    elif choice == "3":
        build_malware()
    elif choice == "4":
        view_hits()
    elif choice == "5":
        sys.exit()

def build_page():
    header()
    target = input("[?] Target Platform Name: ").capitalize()
    
    # High-End Professional CSS
    css = """
    body { background-color: #36393f; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
    .card { background: #2f3136; padding: 32px; border-radius: 8px; width: 400px; box-shadow: 0 8px 16px rgba(0,0,0,0.2); }
    h3 { color: white; text-align: center; margin-bottom: 8px; }
    p { color: #b9bbbe; text-align: center; margin-bottom: 20px; font-size: 14px; }
    input { width: 100%; padding: 10px; margin-bottom: 16px; border-radius: 3px; border: 1px solid #202225; background: #202225; color: white; box-sizing: border-box; }
    button { width: 100%; padding: 10px; background: #5865f2; color: white; border: none; border-radius: 3px; cursor: pointer; font-size: 16px; transition: 0.2s; }
    button:hover { background: #4752c4; }
    """
    html = f"<html><head><style>{css}</style></head><body><div class='card'><h3>{target}</h3><p>Welcome back!</p><input type='text' placeholder='Email'><input type='password' placeholder='Password'><button>Login</button></div></body></html>"
    
    path = f"{FOLDER}/{target.lower()}_template.html"
    with open(path, "w") as f:
        f.write(html)
    
    main_menu(f"Template Created: {path}")

def start_listener():
    header()
    print("\033[94m[*] Socket established on Port 8080...")
    print("[*] Listening for incoming data packets from tunnel...")
    
    # Simulation of the "Hit" appearing in the app
    for i in range(5, 0, -1):
        sys.stdout.write(f"\r[!] Intercepting in {i}s...")
        sys.stdout.flush()
        time.sleep(1)
    
    u, p = "User_Demo", "Pass_1234"
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] INCOMING HIT | USER: {u} | PASS: {p}\n")
    
    main_menu(f"!!! ALERT: NEW HIT !!! USER: {u} | PASS: {p}")

def build_malware():
    header()
    name = input("[?] Payload Filename: ")
    print(f"[*] Obfuscating code for {name}...")
    time.sleep(2)
    with open(f"{FOLDER}/{name}", "w") as f:
        f.write("STUB_ENCRYPTED_DATA_v10")
    main_menu(f"Payload '{name}' is now in {FOLDER}")

def view_hits():
    header()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("Log is empty.")
    input("\nPress Enter...")
    main_menu()

if __name__ == "__main__":
    main_menu()
