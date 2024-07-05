import os
import platform
import subprocess
from colorama import Fore, Style, init
from tqdm import tqdm
import requests

init(autoreset=True)

def is_android():
    """Check if the script is running on an Android device."""
    if platform.system() != 'Linux':
        return False
    try:
        with open('/system/build.prop') as f:
            return 'ro.build.version.release' in f.read()
    except FileNotFoundError:
        return False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner_lines = [
        "  ____             _   ____                                         ",
        " / ___| ___   __ _| |_| __ ) _   _ _ __   __ ____ ___  ___ _ __ ___ ",
        "| |  _ / _ \\\\ / _` | __|  _ \\\\| | | | '_ \\\\ / _` / __/ __|/ _ \\\\ '__/ __|",
        "| |_| | (_) | (_| | |_| |_) | |_| | |_) | (_| \\\\__ \\\\__ \\\\  __/ |  \\\\__ \\\\",
        " \\\\____|\\\\___/ \\\\__,_|\\\\__|____/ \\\\__, | .__/ \\\\__,_|___/___/\\\\___|_|  |___/",
        "                             |___/|_|                                ",
        "                          \xe2\x80\xba Made By Neyoshi! \xe2\x80\xb9                         "
    ]
    
    def get_gradient_color(step, max_steps, start_color, end_color):
        start_r, start_g, start_b = start_color
        end_r, end_g, end_b = end_color
        ratio = step / max_steps
        r = int(start_r + (end_r - start_r) * ratio)
        g = int(start_g + (end_g - start_g) * ratio)
        b = int(start_b + (end_b - start_b) * ratio)
        return f'\\033[38;2;{r};{g};{b}m'

    start_color = (229, 118, 154)
    end_color = (255, 204, 214)

    for i, line in enumerate(banner_lines):
        color = get_gradient_color(i, len(banner_lines) - 1, start_color, end_color)
        print(color + line + Fore.RESET)

def check_install_packages():
    required_packages = ['requests', 'colorama', 'tqdm']
    installed_packages = subprocess.check_output(['pip', 'list']).decode('utf-8')

    for package in required_packages:
        if package not in installed_packages:
            print(f"\xe2\x80\xba [ INFO ] -- Installing {package}...")
            subprocess.check_call(['pip', 'install', package])

def bypass_key(username):
    base_url = "https://healthy-marmoset-teaching.ngrok-free.app/?username="
    url = f"{base_url}{username}"
    headers = {
        'Authorization': 'Bearer Neyoshi'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response_data = response.json()
        key = response_data.get('key', 'No key found')
        status_code = response.status_code
    except requests.RequestException as e:
        key = str(e)
        status_code = e.response.status_code if e.response else 500
    
    return status_code, key

def read_usernames_from_file(filename):
    try:
        with open(filename, 'r') as file:
            usernames = [line.strip() for line in file.readlines()]
        return usernames
    except FileNotFoundError:
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        print(f"{Fore.RED}\xe2\x80\xba [ Error ]: File {filename} not found! Creating the file...{Fore.RESET}")
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        open(filename, 'w').close()
        return []

def save_bypassed_to_file(bypassed_list, filename):
    with open(filename, 'w') as file:
        for entry in bypassed_list:
            file.write(entry + '\
')

def main():
    if not is_android():
        print(f"{Fore.RED}\xe2\x80\xba [ Error ]: This script can only be run on Android devices.{Fore.RESET}")
        return
    
    check_install_packages()
    clear_console()
    print_banner()

    print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ INFO ] -- {Fore.RESET}{Fore.LIGHTWHITE_EX}Welcome to the auto key delta tool! | Shouko - Anti-Intelligent Units!{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ INFO ] -- {Fore.RESET}{Fore.LIGHTWHITE_EX}Create file 'usernames.txt' & 'bypassed.txt'!{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ INFO ] -- {Fore.RESET}{Fore.LIGHTWHITE_EX}Enter your username account in 'usernames.txt'!{Fore.RESET}")
    print(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ INFO ] -- {Fore.RESET}{Fore.LIGHTWHITE_EX}After launching, wait until the tool finishes then check the file 'bypassed.txt' to get the delta key!{Fore.RESET}")
    print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
    input(f"{Fore.LIGHTBLACK_EX}\xe2\x80\xba Press Enter to start...{Fore.RESET}")

    clear_console()
    print_banner()

    input_filename = 'usernames.txt'
    output_filename = 'bypassed.txt'
    
    if not os.path.exists(input_filename):
        open(input_filename, 'w').close()
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        print(f"{Fore.LIGHTYELLOW_EX}\xe2\x80\xba [ INFO ] -- {Fore.RESET}Created {input_filename} file. Please add usernames to it and restart the tool.")
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        input(f"{Fore.LIGHTBLACK_EX}\xe2\x80\xba Press Enter to exit...{Fore.RESET}")
        clear_console()
        return
    if not os.path.exists(output_filename):
        open(output_filename, 'w').close()

    users_to_bypass = read_usernames_from_file(input_filename)
    if not users_to_bypass:
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        print(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ Error ] -- {Fore.RESET}No usernames found in {input_filename}.")
        print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
        input(f"{Fore.LIGHTBLACK_EX}\xe2\x80\xba Press Enter to exit...{Fore.RESET}")
        clear_console()
        return

    total_users = len(users_to_bypass)

    print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}\xe2\x80\xba [ INFO ] -- Total usernames: {Fore.RESET}{total_users}")
    print(f"{Fore.LIGHTYELLOW_EX}\xe2\x80\xba [ LOADING ] -- Starting the process...{Fore.RESET}")

    bypassed_results = []

    for username in tqdm(users_to_bypass, desc="\xe2\x80\xba [ Processing ]", unit="user", ncols=100, miniters=1, bar_format='{l_bar}{bar}{r_bar}'):
        status_code, key = bypass_key(username)
        if status_code != 500:
            result = f"{username} - {key}"
            bypassed_results.append(result)
        if status_code == 200:
            tqdm.write(f"{Fore.LIGHTGREEN_EX}\xe2\x80\xba [ SUCCESS ] -- Successfully: {Fore.RESET}{username} - Key: {key}")
        else:
            tqdm.write(f"{Fore.LIGHTRED_EX}\xe2\x80\xba [ FAILED ] -- Failed: {Fore.RESET}{username}{Fore.LIGHTRED_EX}, Status Code: {Fore.RESET}{status_code}")
    
    save_bypassed_to_file(bypassed_results, output_filename)

    clear_console()
    print_banner()
    print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
    print(f"{Fore.LIGHTYELLOW_EX}\xe2\x80\xba [ INFO ] -- Total usernames: {Fore.RESET}{total_users}")
    print(f"{Fore.LIGHTGREEN_EX}\xe2\x80\xba [ SUCCESS ] -- Process completed!{Fore.RESET}")
    print(f"{Fore.LIGHTBLUE_EX}\xe2\x80\xba [ DISCORD ] -- Join our Discord at {Fore.RESET}https://discord.gg/shoukohub")
    print(f"{Fore.LIGHTWHITE_EX}{'-' * 75}{Fore.RESET}")
    input(f"{Fore.LIGHTBLACK_EX}\xe2\x80\xba Press Enter to exit...{Fore.RESET}")
    clear_console()

if __name__ == "__main__":
    main()
