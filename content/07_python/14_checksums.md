# Checksums

:::{dropdown} Learning Goals
By the end of this section you will:
- know how to calculate and check a simple sum checksum in Python
- know how to add and check a parity bit
- know how to validate a number with the Luhn check digit algorithm
- know how to use CRC32 and SHA-256 checksums to check that a file hasn't changed
:::

A **checksum** is a small value calculated from a block of data. The sender calculates the checksum and sends it with the data. The receiver does the same calculation on the data it receives. If the two checksums match, the data is assumed to be correct. If they don't, the data has been changed. The theory is on the [Data Security Management](../05_data_transmission/04_security_management.md#check-sums) page.

Checksums protect the **integrity** of data: they tell us when data has changed. They don't stop anyone reading the data (that's [encryption](./12_encryption.md)), and they don't fix errors, they only detect them.

All the tools on this page are built into Python, so there is nothing to install.

## Sum checksums

### The simple checksum

The Data Security Management page adds up the numbers and keeps the last digit (mod 10). Let's code that example:

:::{code} python
:linenos:
def simple_checksum(numbers: list[int]) -> int:
    return sum(numbers) % 10


sent_data = [12, 7, 5, 20]
sent_checksum = simple_checksum(sent_data)
print(f"Sent: {sent_data}, checksum {sent_checksum}")

received_data = [12, 7, 6, 20]
received_checksum = simple_checksum(received_data)
print(f"Received: {received_data}, checksum {received_checksum}")

if received_checksum == sent_checksum:
    print("Checksums match: data is correct")
else:
    print("Checksums don't match: data is corrupted")
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 1&ndash;2** &rarr; `sum()` adds up the numbers, and `% 10` keeps the remainder after dividing by 10, which is the last digit
- **lines 5&ndash;7** &rarr; the sender calculates the checksum of the data it sends
- **lines 9&ndash;11** &rarr; the receiver calculates the checksum of the data it receives. One number has changed from 5 to 6
- **lines 13&ndash;16** &rarr; compares the two checksums
:::

Output:

:::{code} text
Sent: [12, 7, 5, 20], checksum 4
Received: [12, 7, 6, 20], checksum 5
Checksums don't match: data is corrupted
:::

### Checksums on text

Computers send text as bytes, and each byte is a number from 0 to 255. So we can use the same idea on a message: add up the bytes and keep the remainder after dividing by 256, which keeps the checksum to one byte.

:::{code} python
:linenos:
def byte_checksum(message: str) -> int:
    return sum(message.encode()) % 256


print(byte_checksum("Meet at 3pm"))
print(byte_checksum("Meet at 4pm"))
print(byte_checksum("Mete at 3pm"))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 2** &rarr; `.encode()` turns the message into bytes. `sum()` adds the byte values, and `% 256` keeps the result between 0 and 255
- **line 5** &rarr; the original message
- **line 6** &rarr; one character changed (3 to 4)
- **line 7** &rarr; two characters swapped (`et` to `te`)
:::

Output:

:::{code} text
176
177
176
:::

Changing one character changed the checksum, so that error is detected. But swapping two characters gives the **same** checksum, because addition doesn't care about order. The receiver would think `"Mete at 3pm"` is correct.

:::{attention} Stop and Think
:class: dropdown
A sum checksum can't detect two characters swapping places. What other errors could it miss? Think about two changes that cancel each other out.
:::

## Parity bits

A **parity bit** is a one-bit checksum added to a group of bits. With **even parity**, the parity bit is chosen so the total number of 1s is even.

In Python, we can store bits as a string of `"0"` and `"1"` characters, which makes them easy to count and print.

:::{code} python
:linenos:
def add_even_parity(bits: str) -> str:
    if bits.count("1") % 2 == 0:
        return bits + "0"
    return bits + "1"


def check_even_parity(bits: str) -> bool:
    return bits.count("1") % 2 == 0


def flip_bit(bits: str, position: int) -> str:
    flipped = "1" if bits[position] == "0" else "0"
    return bits[:position] + flipped + bits[position + 1 :]


bits = format(ord("D"), "07b")
sent = add_even_parity(bits)
print(f"D -> {bits} -> sent as {sent}")

one_error = flip_bit(sent, 2)
two_errors = flip_bit(one_error, 5)

print(f"No errors:  {sent} {check_even_parity(sent)}")
print(f"One error:  {one_error} {check_even_parity(one_error)}")
print(f"Two errors: {two_errors} {check_even_parity(two_errors)}")
:::

:::{important} Explanation of Code
:class: dropdown
- **lines 1&ndash;4** &rarr; counts the 1s. If there's already an even number, the parity bit is `0`. If there's an odd number, the parity bit is `1` to make it even
- **lines 7&ndash;8** &rarr; the data is correct if the number of 1s, including the parity bit, is even
- **lines 11&ndash;13** &rarr; simulates a transmission error by changing one bit. The string is rebuilt from the bits before `position`, the flipped bit, and the bits after it
- **line 16** &rarr; `ord("D")` gives the character code 68, and `format(..., "07b")` writes it as 7 binary digits
- **line 17** &rarr; adds the parity bit
- **lines 20&ndash;21** &rarr; makes a copy with one bit flipped, then a copy with two bits flipped
- **lines 23&ndash;25** &rarr; checks each version
:::

Output:

:::{code} text
D -> 1000100 -> sent as 10001000
No errors:  10001000 True
One error:  10101000 False
Two errors: 10101100 True
:::

One flipped bit is detected. But when two bits flip, the number of 1s is even again, so the error isn't detected. A parity bit can only detect an **odd** number of errors.

## Check digits

A **check digit** is a checksum that is part of a number. The last digit of a credit card number, for example, is a check digit calculated from the other digits. It catches typing mistakes, such as one wrong digit or two digits swapped, before the number is even sent.

Credit card numbers use the **Luhn algorithm**:

1. starting from the right, double every second digit
2. if doubling gives a number over 9, subtract 9
3. add up all the digits
4. the number is valid if the total ends in 0 (`total % 10 == 0`)

:::{code} python
:linenos:
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


print(luhn_check("7992 7398 713"))
print(luhn_check("7992 7398 714"))
print(luhn_check("7992 7389 713"))
:::

:::{important} Explanation of Code
:class: dropdown
- **line 1** &rarr; the number is a string, so it can include spaces and leading zeros
- **line 2** &rarr; a list comprehension that keeps only the digits and converts each one to an `int`
- **line 4** &rarr; `reversed()` starts from the right-hand digit. `enumerate()` gives each digit's position, starting at 0
- **line 5** &rarr; positions 1, 3, 5 … are every second digit from the right
- **lines 6&ndash;8** &rarr; doubles the digit, and subtracts 9 if the result is over 9
- **line 9** &rarr; adds the digit to the total
- **line 10** &rarr; the number is valid if the total is divisible by 10
- **line 13** &rarr; a valid number
- **line 14** &rarr; the last digit is wrong
- **line 15** &rarr; two digits have been swapped (98 to 89)
:::

Output:

:::{code} text
True
False
False
:::

:::{hint} Where check digits are used
:class: dropdown
The Luhn algorithm is used for credit and debit card numbers, and for the IMEI number that identifies every mobile phone. Other check digit systems are used in ISBNs (book numbers), barcodes and Australian Tax File Numbers. A valid check digit doesn't mean the number is real, only that it was typed correctly.
:::

## File checksums

To check that a whole file hasn't changed, we calculate a checksum of the file's bytes. Two common choices are:

- **CRC32** (cyclic redundancy check) &rarr; a fast 32-bit checksum designed to catch accidental errors, such as a damaged download or a faulty disk. Python's built-in `zlib` module calculates it
- **SHA-256** &rarr; the hash function from the [Hashing](./13_hashing.md) page. It is slower, but it is designed so that no one can change a file and keep the same hash, so it also detects deliberate tampering

:::{code} python
:linenos:
import hashlib
import zlib
from pathlib import Path


def file_checksums(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    crc = format(zlib.crc32(data), "08x")
    sha = hashlib.sha256(data).hexdigest()
    return crc, sha


report = Path("data/report.txt")

report.write_bytes(b"Term 4 results are ready.")
crc, sha = file_checksums(report)
print(f"CRC32:   {crc}")
print(f"SHA-256: {sha}")

report.write_bytes(b"Term 4 results are ready!")
crc, sha = file_checksums(report)
print(f"CRC32:   {crc}")
print(f"SHA-256: {sha}")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 2** &rarr; imports Python's built-in `zlib` module, which includes CRC32
- **line 7** &rarr; reads the whole file as bytes. Checksums always work on the exact bytes in the file
- **line 8** &rarr; `zlib.crc32()` returns a number. `format(..., "08x")` writes it as 8 hexadecimal characters, which is how CRC32 values are usually shown
- **line 9** &rarr; calculates the SHA-256 hash of the file
- **line 10** &rarr; returns both checksums as a tuple
- **line 13** &rarr; the file **report.txt** in our **data** folder
- **lines 15&ndash;18** &rarr; writes the file and prints its checksums
- **lines 20&ndash;23** &rarr; changes one character (`.` to `!`) and prints the checksums again
:::

Output:

:::{code} text
CRC32:   5014ec25
SHA-256: ee7e9563cb4afc60e9bf6e8b6d14c79d97d66a68a4459ea3e0f9cbeb55d2801e
CRC32:   c0abf1b4
SHA-256: 4fe8785e500201b750e27889b45c7df1283494ffe8b4cce1e640597bc0cbad17
:::

Changing one character changed both checksums completely.

### Verifying a download

Software websites often publish a SHA-256 checksum next to each download. After downloading, we calculate the file's checksum and compare it with the published one. If they match, the file arrived complete and hasn't been tampered with.

:::{code} python
:linenos:
import hashlib
from pathlib import Path

published_sha256 = "ee7e9563cb4afc60e9bf6e8b6d14c79d97d66a68a4459ea3e0f9cbeb55d2801e"

download = Path("data/report.txt")
actual_sha256 = hashlib.sha256(download.read_bytes()).hexdigest()

if actual_sha256 == published_sha256:
    print("File verified: it matches the published checksum")
else:
    print("Warning: the file doesn't match the published checksum")
:::

:::{important} Explanation of Code
:class: dropdown
- **line 4** &rarr; the checksum published by the website. Here it is the checksum of the original **report.txt**
- **line 7** &rarr; calculates the checksum of the file we have
- **lines 9&ndash;12** &rarr; compares the two checksums
:::

The last example left **report.txt** with the `!` version, so the output is:

:::{code} text
Warning: the file doesn't match the published checksum
:::

If we change the `!` in **report.txt** back to `.` and save it, the output becomes:

:::{code} text
File verified: it matches the published checksum
:::

:::{caution} Line endings change checksums
:class: dropdown
Windows and macOS end lines of text differently. Some tools, including Git, can change the line endings when they copy a text file, which changes its checksum even though the text looks the same. Checksums compare the exact bytes, so always calculate them on the file exactly as it was published.
:::

## Summary

| Method | Detects | Misses | Python |
| --- | --- | --- | --- |
| Sum checksum | most single changes | swapped values, changes that cancel out | `sum(data) % 10` or `% 256` |
| Parity bit | an odd number of flipped bits | an even number of flipped bits | `bits.count("1") % 2` |
| Luhn check digit | one wrong digit, most swapped neighbours | some swaps, such as 09 and 90 | the `luhn_check()` function |
| CRC32 | accidental errors in files and network data | deliberate changes | `zlib.crc32(data)` |
| SHA-256 | any change, including deliberate tampering | nothing in practice | `hashlib.sha256(data).hexdigest()` |

:::{seealso} Checksum Activities
:class: dropdown
**Activity 1: Checking received messages**

A sender sends `[3, 14, 15, 92]` with a simple mod 10 checksum. Use `simple_checksum()` to check each of these received messages and print whether it is correct or corrupted:

```python
received_messages = [
    [3, 14, 15, 92],
    [3, 14, 16, 92],
    [3, 15, 14, 92],
]
```

Expected Output:

```text
Sent checksum: 4
[3, 14, 15, 92]: correct
[3, 14, 16, 92]: corrupted
[3, 15, 14, 92]: correct
```

The third message isn't the same as the one sent. Why does the checksum say it is correct?

---

**Activity 2: Odd parity**

With **odd parity**, the parity bit makes the total number of 1s odd. Write `add_odd_parity()` and `check_odd_parity()` functions, then use them to send each letter of `"Hi"` as 7 bits plus a parity bit.

Expected Output:

```text
H -> 1001000 -> 10010001 True
i -> 1101001 -> 11010011 True
```

---

**Activity 3: Generate a check digit**

Write a `generate_check_digit()` function that takes a number without its check digit and returns the digit (0&ndash;9) that makes it pass `luhn_check()`. Test it on these two numbers:

```python
print(generate_check_digit("7992739871"))
print(generate_check_digit("453914880343646"))
```

Expected Output:

```text
3
7
```

---

**Activity 4: Find identical files**

Write a program that creates three files in our **data** folder: **a.txt** containing `Hello`, **b.txt** containing `Hello`, and **c.txt** containing `hello`. Use SHA-256 checksums to compare every pair of files and print whether they are identical.

Expected Output:

```text
a.txt and b.txt are identical
a.txt and c.txt are different
b.txt and c.txt are different
```
:::
