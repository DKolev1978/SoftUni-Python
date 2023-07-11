from collections import deque

tools = deque([int(tool) for tool in input().split()])
substances = deque([int(substance) for substance in input().split()])
challenges = deque([int(challenge) for challenge in input().split()])

while tools and substances:
    cur_tool = tools.popleft()
    cur_substance = substances.pop()

    multiply_tool_cur_substance = cur_tool * cur_substance

    for challenge in challenges:
        if challenge == multiply_tool_cur_substance:
            challenges.remove(challenge)
            break
    else:
        cur_tool += 1
        tools.append(cur_tool)
        cur_substance -= 1
        if cur_substance > 0:
            substances.append(cur_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join(str(tool) for tool in tools)}")
if substances:
    print(f"Substances: {', '.join(str(sub) for sub in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(ch) for ch in challenges)}")

