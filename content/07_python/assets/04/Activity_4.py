def average(scores: list[int]) -> float:
    return sum(scores) / len(scores)


def count_words(words: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    return counts


print(average([70, 85, 90]))
print(count_words(["red", "blue", "red"]))
