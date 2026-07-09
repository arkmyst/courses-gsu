import re

def analyze_file(filepath):
    total_had_count = 0

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # Step 1: remove punctuation (keep letters + spaces)
            cleaned_line = re.sub(r"[^A-Za-z\s]", " ", line)

            # Step 2: find whole word "had" (case-insensitive)
            matches = re.findall(r"\bhad\b", cleaned_line, flags=re.IGNORECASE)

            total_had_count += len(matches)

    return total_had_count


if __name__ == "__main__":
    filepath = input("Enter path to .txt file: ")

    total = analyze_file(filepath)

    print(f"Total instances of the word 'had': {total}")
