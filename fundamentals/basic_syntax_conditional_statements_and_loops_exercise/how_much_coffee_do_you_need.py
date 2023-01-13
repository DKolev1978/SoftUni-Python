counter = 0
while True:
    text = input()
    if text == "END":
        break

    if text == "coding" or text == "dog" or text == "cat" or text == "movie":
        counter += 1
    elif text == "CODING" or text == "DOG" or text == "CAT" or text == "MOVIE":
        counter += 2
if counter > 5:
    print("You need extra sleep")
else:
    print(counter)


