import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def is_valid_luhn(card_num: str) -> bool:
    try:
        if not card_num.isdigit():
            raise ValueError(f"[\033[91merror\033[0m] Invalid characters in card number")

        total = 0
        num_digits = len(card_num)
        odd_even = num_digits & 1

        for i, digit in enumerate([int(x) for x in card_num]):
            if i % 2 == odd_even:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit

        return total % 10 == 0
    except ValueError:
        return False

while True:
    try:
        clear_screen()
        pan = input("Enter PAN (13-19 digits): ").replace(' ', '').strip()
        if not pan.isdigit() or len(pan) < 13 or len(pan) > 19:
            clear_screen()
            print(f"[\033[91merror\033[0m] Invalid PAN")
            time.sleep(2)
            continue

        if not is_valid_luhn(pan):
            clear_screen()
            print(f"- \033[91mFailed\033[0m Luhn Algorithm checksum\n\n\033[41mINVALID PAN\033[0m : {pan}")
            time.sleep(3)
            continue

        clear_screen()
        print(f"\033[42mVALID PAN\033[0m : {pan}")
        time.sleep(3)
        continue
    except KeyboardInterrupt:
        clear_screen()
        break