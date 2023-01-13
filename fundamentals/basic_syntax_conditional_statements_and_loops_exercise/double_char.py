while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue

    reverted_text = ""
    for ch in text:
        reverted_text += 2 * ch
    print(reverted_text)