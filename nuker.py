import os
import time
import sys

AUTHOR = "Zain"
VERSION = "9.0.0-ULTRA-HD"
FOLDER = "Nuker_Data"
LOG_FILE = f"{FOLDER}/captured_hits.txt"

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
    print(f" [INTERFACE]: v{VERSION} | [DEV]: {AUTHOR}")
    print("="*70 + "\033[0m")

def footer(msg):
    print("\033[92m" + "="*70)
    print(f" [LAST HIT]: \033[93m{msg}\033[0m")
    print("\033[92m" + "="*70 + "\033[0m")

def main_menu(status="READY FOR DEPLOYMENT"):
    header()
    print("\033[92m [1] GENERATE PRO LOGIN PAGE (Discord/Insta/etc.)")
    print(" [2] BUILD PAYLOAD (Cross-Platform Sim)")
    print(" [3] VIEW CAPTURED DATA (Hit Log)")
    print(" [4] EXIT")
    print("-" * 70)
    footer(status)
    
    cmd = input("\n\033[92mNUKER_C2 > \033[0m").strip()
    
    if cmd == "1":
        generate_pro_page()
    elif cmd == "2":
        build_payload()
    elif cmd == "3":
        view_hits()
    elif cmd == "4":
        sys.exit()

def generate_pro_page():
    header()
    target = input("[?] Target Platform (e.g., Discord): ").capitalize()
    
    # Modern CSS for a dark-mode professional look
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ background: #2f3136; color: white; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; }}
            .login-box {{ background: #36393f; padding: 40px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0,0,0,0.2); width: 350px; text-align: center; }}
            h2 {{ margin-bottom: 20px; }}
            input {{ width: 100%; padding: 10px; margin: 10px 0; border-radius: 3px; border: none; background: #202225; color: white; }}
            button {{ width: 100%; padding: 10px; background: #5865f2; border: none; color: white; font-weight: bold; cursor: pointer; border-radius: 3px; }}
        </style>
    </head>
    <body>
        <div class='login-box'>
            <h2>{target} Login</h2>
            <input type='text' placeholder='Email or Phone'>
            <input type='password' placeholder='Password'>
            <button>Login</button>
        </div>
    </body>
    </html>
    """
    
    file_path = f"{FOLDER}/{target.lower()}_login.html"
    with open(file_path, "w") as f:
        f.write(html_content)
    
    print(f"\n\033[92m[!] SUCCESS: {target} page generated at {file_path}")
    
    # Simulating the hit immediately for your video
    user = input("[?] (Simulate Hit) Enter Username to show: ")
    pw = input("[?] (Simulate Hit) Enter Password to show: ")
    
    with open(LOG_FILE, "a") as f:
        f.write(f"[{time.ctime()}] {target} | USER: {user} | PASS: {pw}\n")
    
    input("\nPress Enter to update the Command Bar...")
    main_menu(f"CAPTURED: {user} | PASS: {pw}")

def build_payload():
    header()
    print("[1] Windows (.EXE)")
    print("[2] Android (.APK)")
    print("[3] iPhone (.IPA - Simulation)")
    plat_choice = input("\n[?] Select Platform: ")
    
    ext = ".exe" if plat_choice == "1" else ".apk" if plat_choice == "2" else ".ipa"
    name = f"payload_v9{ext}"
    
    print(f"[*] Compiling {name}...")
    time.sleep(2)
    
    with open(f"{FOLDER}/{name}", "w") as f:
        f.write("STUB_DATA_v9_ENCRYPTED")
        
    main_menu(f"Payload '{name}' generated in folder.")

def view_hits():
    header()
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            print(f.read())
    else:
        print("No hits captured yet.")
    input("\nPress Enter...")
    main_menu()

if __name__ == "__main__":
    main_menu()
