def get_initials(first_name: str, last_name: str) -> str:
    return first_name[0] + last_name[0]


def total_marks(marks: list[int]) -> int:
    return sum(marks)


initials: str = get_initials("Sam", "Lee")
total: int = total_marks([18, 15, 20])
average: float = total / 3
print(initials, total, average)
