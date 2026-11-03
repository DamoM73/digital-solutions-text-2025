def luhn_check(number: str) -> bool:
    digits = [int(digit) for digit in number if digit.isdigit()]
    total = 0
    for position, digit in enumerate(reversed(digits)):
        if position % 2 == 1:
            digit = digit * 2
            if digit > 9:
                digit = digit - 9
        total += digit
    return total % 10 == 0


def generate_check_digit(number: str) -> int:
    for check_digit in range(10):
        if luhn_check(number + str(check_digit)):
            return check_digit
    raise ValueError("no check digit found")


print(generate_check_digit("7992739871"))
print(generate_check_digit("453914880343646"))
