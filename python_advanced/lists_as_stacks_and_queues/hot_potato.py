from collections import deque

names = deque(input().split())
moves = int(input()) - 1

while len(names) > 1:
    names.rotate(-moves)
    exited_name = names.popleft()
    print(f"Removed {exited_name}")

print(f"Last is {names.popleft()}")


