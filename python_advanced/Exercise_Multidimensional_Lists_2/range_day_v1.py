def move(direction, steps):  # създаваме фунцкия move, първи параметър посоката и втори стъпките int
    r = position_shooter[0] + (directions[direction][0] * steps)  # намираме реда и колоната като умножаваме стойностите от
    c = position_shooter[1] + (directions[direction][1] * steps)  # посоката по стъпките и събираме с текущите координати

    if not (0 <= r < n and 0 <= c < n):  # проверяваме дали позицията, на която искаме да стъпим е валидна
        return position_shooter  # ако не е, връщаме текущата позиция
    if play_matix[r][c] == 'x':  # проверяваме дали на позицията, на която искаме да стъпим има мишена
        return position_shooter  # ако да, връщаме текущата позиция

    return [r, c]  # връщаме новата позиция


def shoot(direction):  # създаваме фунцкия shoot, параметър посоката на стрелба
    r = position_shooter[0] + directions[direction][0]  # намираме реда и колоната като събираме координатите от посоката
    c = position_shooter[1] + directions[direction][1]  # с тези, на които се намираме

    while 0 <= r < n and 0 <= c < n:  # развъртаме цикъл докато координатите са валидни
        if play_matix[r][c] == 'x':  # проверяваме дали куршума е достигнал мишена
            play_matix[r][c] = '.'  # ако да, заменяме х с точка
            return [r, c]  # връщаме позицията на улучената мишена

        r += directions[direction][0]  # събираме координатите от посоката
        c += directions[direction][1]  # с тези, на които се намира куршума


n = 5
play_matix = []

targets = 0  # създаваме променлива, в която да пазим броя на мишените в полето
targets_hit = 0  # създаваме променлива, в която да пазим броя на уцелените мишени
hit_positions = []  # създаваме променлива, в която да пазим координатите на уцелените мишени

position_shooter = []  # създаваме променлива, в която да пазим позицията ни

directions = {  # създаваме променлива, в която да пазим посоките
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):  # развъртаме цикъл за всеки ред, за да прочетем матрицата
    play_matix.append(input().split())  # прочитаме ред от конзолата, разделяме го по спейс и го добавяме към матрицата

    if 'A' in play_matix[row]:  # проверяваме дали нашата позиция се намира на този ред
        position_shooter = [row, play_matix[row].index('A')]  # запазваме нашата позиция

    targets += play_matix[row].count('x')  # увеличаваме броя на мишените с броя им на реда

for _ in range(int(input())):  # развъртаме цикъл за очаквания брой команди
    command_info = input().split()  # прочитаме командата и я разделяме по спейс

    if command_info[0] == 'move':  # проверяваме дали командата е move
        position_shooter = move(command_info[1], int(command_info[2]))  # извикваме функцията move, стъпките стават int
    elif command_info[0] == 'shoot':  # проверяваме дали командата е shoot
        target_down_pos = shoot(command_info[1])  # извикваме функцията shoot, параметър е посоката

        if target_down_pos:  # проверяваме дали сме свалили мишена
            hit_positions.append(target_down_pos)  # добавяме позицията на свалената мишена
            targets_hit += 1  # увеличаваме броя на свалените мишени с 1

        if targets_hit == targets:  # проверяваме дали всички мишени са свалени
            print(f'Training completed! All {targets} targets hit.')  # принтираме, че успешно сме завършили обучението
            break  # прекратяваме цикъла

if targets_hit < targets:  # проверяваме дали са останали мишени
    print(f'Training not completed! {targets - targets_hit} targets left.')  # принтираме неуспешно завършено обучение

print(*hit_positions, sep="\n")  # принтираме позициите на свалените мишени