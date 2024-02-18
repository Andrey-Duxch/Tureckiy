def rook(start_point, end_point):
    if start_point[0] == end_point[0] or start_point[1] == end_point[1]:
        return True
    return False
def bishop(start_point, end_point):
    if abs(start_point[0] - end_point[0]) == abs(start_point[1] - end_point[1]):
        return True
    return False
def queen(start_point, end_point):
    if start_point[0] == end_point[0] or start_point[1] == end_point[1] or abs(start_point[0] - end_point[0]) == abs(start_point[1] - end_point[1]):
        return True
    return False
def knight(start_point, end_point):
    if (abs(start_point[0] - end_point[0]) == 1 and abs(start_point[1] - end_point[1]) == 2) or (abs(start_point[0] - end_point[0]) == 2 and abs(start_point[1] - end_point[1]) == 1):
        return True
    return False
def main():
    word = input("Для какой фигуры выполнить проверку?\n>>".lower())
    a, b = map(int, input(f"Введите начальное положение для фигуры {word}:").split())
    c, d = map(int, input(f"Введите конечное положение для фигуры {word}:").split())
    answer = ""
    if word == "ладья":
        answer = rook((a, b), (c, d))
    elif word == "слон":
        answer = bishop((a, b), (c, d))
    elif word == "ферзь":
        answer = queen((a, b), (c, d))
    elif word == "конь":
        answer = knight((a, b), (c, d))
    if answer:
        print(f"Ход для фигуры {word} возможен.")
    else:
        print(f"Ход для фигуры {word} не возможен.")
main()