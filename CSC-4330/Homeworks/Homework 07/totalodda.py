import re

def analyze_file(filepath):
    total = 0

    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()

    # Step 1: extract words
    words = re.findall(r"[A-Za-z'-]+", text)

    # Step 2: count odd number of A's
    for word in words:
        num_as = sum(1 for c in word if c.lower() == 'a')
        if num_as % 2 == 1:
            total += 1

    return total


if __name__ == "__main__":
    filepath = input("Enter path to .txt file: ")
    result = analyze_file(filepath)
    print(f"Words with odd number of A's/a's: {result}")
