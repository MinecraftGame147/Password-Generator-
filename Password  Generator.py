import itertools
import random
import string
import os
import platform
from colorama import init, Fore, Style

# فعال کردن colorama (مخصوص ویندوز)
init(autoreset=True)

banner = r"""
███╗░░░███╗░█████╗░  ░██████╗
████╗░████║██╔══██╗  ██╔════╝
██╔████╔██║███████║  ╚█████╗░
██║╚██╔╝██║██╔══██║  ░╚═══██╗
██║░╚═╝░██║██║░░██║  ██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝  ╚═════╝░
       [ M G - Minecraft Game Discord: https://discord.gg/W5gdZyaq]
"""

print(Fore.GREEN + banner + Style.RESET_ALL)

def reverse_words(words):
    return [w[::-1] for w in words]

def add_random_noise(word, count=1):
    for _ in range(count):
        pos = random.randint(0, len(word))
        rand_char = random.choice(string.ascii_letters + string.digits)
        word = word[:pos] + rand_char + word[pos:]
    return word

def random_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_-=+"
    return ''.join(random.choice(chars) for _ in range(length))

first_name = input(Fore.CYAN + "First name: " + Style.RESET_ALL)
last_name = input(Fore.CYAN + "Last name: " + Style.RESET_ALL)
birth_year = input(Fore.CYAN + "Birth year: " + Style.RESET_ALL)
birth_day = input(Fore.CYAN + "Day or month: " + Style.RESET_ALL)
extras = input(Fore.CYAN + "Extra words or symbols (comma separated): " + Style.RESET_ALL)
extra_words = [x.strip() for x in extras.split(",") if x.strip()]

use_reverse = input(Fore.YELLOW + "Include reversed words? (y/n): " + Style.RESET_ALL).lower() == "y"
add_noise = input(Fore.YELLOW + "Add random letters/numbers? (y/n): " + Style.RESET_ALL).lower() == "y"
min_len = int(input(Fore.MAGENTA + "Min password length: " + Style.RESET_ALL))
max_len = int(input(Fore.MAGENTA + "Max password length: " + Style.RESET_ALL))
max_passwords = int(input(Fore.MAGENTA + "How many passwords to generate: " + Style.RESET_ALL))

specials = ['!', '@', '#', '$', '%', '&', '.', '_', '-', '*']
base_words = [first_name, last_name, birth_year, birth_day] + extra_words

if use_reverse:
    base_words += reverse_words(base_words)

passwords = set()
for i in range(2, 4):
    for combo in itertools.permutations(base_words, i):
        for sep in ["", *specials]:
            joined = sep.join(combo)
            for variant in [joined, joined.lower(), joined.upper(), joined.capitalize()]:
                if min_len <= len(variant) <= max_len:
                    passwords.add(variant)
                if add_noise:
                    noisy = add_random_noise(variant, random.randint(1, 2))
                    if min_len <= len(noisy) <= max_len:
                        passwords.add(noisy)

while len(passwords) < max_passwords:
    passwords.add(random_password(random.randint(min_len, max_len)))

final_list = list(passwords)[:max_passwords]
output_file = "password_list0.txt"

with open(output_file, "w") as f:
    for pwd in final_list:
        f.write(pwd + "\n")
    f.write("\n" + banner + "\n")
    f.write("\n---\nDiscord Support: https://discord.gg/W5gdZyaq\n")

# باز کردن فایل خروجی با برنامه پیش‌فرض سیستم
if platform.system() == "Windows":
    os.system(f"notepad {output_file}")
elif platform.system() == "Linux":
    os.system(f"xdg-open {output_file}")
elif platform.system() == "Darwin":  # macOS
    os.system(f"open {output_file}")
else:
    print(f"Open the file manually: {output_file}")
