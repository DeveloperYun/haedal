line = int(input("다이아몬드 상부 줄 수 : "))

for x in range(1, line):
    print(" " * (line - x) + "*" * (2 * x - 1))

for y in range(line, 0, -1):
    print(" " * (line - y) + "*" * (2 * y - 1))5