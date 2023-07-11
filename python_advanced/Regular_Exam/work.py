# result = [x for x in "sometext" if x == "e"]
# result = [x for x in "sometext" if x == "e" else -1]
result = [x if x == "e" else -1 for x in "sometext"]

print(result)