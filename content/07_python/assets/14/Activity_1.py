def simple_checksum(numbers: list[int]) -> int:
    return sum(numbers) % 10


sent_checksum = simple_checksum([3, 14, 15, 92])
print(f"Sent checksum: {sent_checksum}")

received_messages = [
    [3, 14, 15, 92],
    [3, 14, 16, 92],
    [3, 15, 14, 92],
]

for message in received_messages:
    if simple_checksum(message) == sent_checksum:
        print(f"{message}: correct")
    else:
        print(f"{message}: corrupted")
