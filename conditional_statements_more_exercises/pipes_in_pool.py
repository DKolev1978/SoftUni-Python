v = int(input())        #• Първият ред съдържа числото V – Обем на басейна в литри – цяло число в интервала [1…10000].
p1 = int(input())       #• Вторият ред съдържа числото P1 – дебит на първата тръба за час – цяло число в интервала [1…5000].
p2 = int(input())       #• Третият ред съдържа числото P2 – дебит на втората тръба за час– цяло число в интервала [1…5000].
h = float(input())      #• Четвъртият ред съдържа числото H – часовете които работникът отсъства – реално число в интервала [1.0…24.00]

p1_full = p1 * h
p2_full = p2 * h
pool_full = (p1_full + p2_full)

if v >= pool_full:
    print(f"The pool is {pool_full / v * 100:.2f}% full. Pipe 1: {p1_full /pool_full * 100:.2f}%. Pipe 2: {p2_full / pool_full * 100:.2f}%.")
elif v < pool_full:
    print(f"For {h} hours the pool overflows with {pool_full - v:.2f} liters.")


