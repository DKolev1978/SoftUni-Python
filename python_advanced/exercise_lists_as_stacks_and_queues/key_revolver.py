from collections import deque

bullet_price = int(input())
size_of_the_gun_barrel = int(input())

bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])

reward = int(input())

bullets_in_mag = size_of_the_gun_barrel
bullets_shot = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()

    if bullet <= lock:
        print("Bang!")
    else:
        print("Ping!")
        locks.appendleft(lock)

    bullets_in_mag -= 1
    bullets_shot += 1

    if bullets_in_mag == 0 and bullets:
        bullets_in_mag = size_of_the_gun_barrel if len(bullets) >= size_of_the_gun_barrel else len(bullets)
        print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    earned_money = abs((bullet_price * bullets_shot) - reward)
    print(f"{len(bullets)} bullets left. Earned ${earned_money}")