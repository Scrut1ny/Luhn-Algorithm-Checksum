import os, time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_luhn(card_num: str) -> bool:
    if not card_num.isdigit(): return False
    total, odd_even = 0, len(card_num) & 1
    for i, digit in enumerate(map(int, card_num)):
        if i % 2 == odd_even:
            digit *= 2
            if digit > 9: digit -= 9
        total += digit
    return total % 10 == 0

while True:
    try:
        clear_screen()
        pan = input("Enter PAN (13-19 digits): ").replace(' ', '')
        if not pan.isdigit() or not 13 <= len(pan) <= 19:
            clear_screen(); print(f"[\033[91merror\033[0m] Invalid PAN"); time.sleep(2); continue
        clear_screen(); print(f"\033[{'41' if not is_valid_luhn(pan) else '42'}m{'INVALID' if not is_valid_luhn(pan) else 'VALID'} PAN\033[0m : {pan}"); time.sleep(3)
    except KeyboardInterrupt:
        clear_screen(); break
