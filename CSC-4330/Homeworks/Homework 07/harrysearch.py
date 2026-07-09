def analyze_file(filepath):
    lines_with_harry = 0
    total_harry_count = 0

    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            count_in_line = line.count("Harry")
            
            if count_in_line > 0:
                lines_with_harry += 1
            
            total_harry_count += count_in_line

    return lines_with_harry, total_harry_count


if __name__ == "__main__":
    filepath = input("Enter path to .txt file: ")
    
    lines, total = analyze_file(filepath)
    
    print(f"(a) Lines containing 'Harry': {lines}")
    print(f"(b) Total instances of 'Harry': {total}")

    # Optional sanity check
    if lines <= total:
        print("Check passed ✔")
    else:
        print("Check failed ❌")
