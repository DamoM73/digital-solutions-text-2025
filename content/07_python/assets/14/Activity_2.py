def add_odd_parity(bits: str) -> str:
    if bits.count("1") % 2 == 0:
        return bits + "1"
    return bits + "0"


def check_odd_parity(bits: str) -> bool:
    return bits.count("1") % 2 == 1


for letter in "Hi":
    bits = format(ord(letter), "07b")
    sent = add_odd_parity(bits)
    print(f"{letter} -> {bits} -> {sent} {check_odd_parity(sent)}")
