def check_straight(i, j, line_len, lines):
    total = 0
    if j + 3 < line_len and lines[i][j + 1] == 'M' and lines[i][j + 2] == 'A' and lines[i][j + 3] == 'S':
        total += 1

    if j - 3 >= 0 and lines[i][j - 1] == 'M' and lines[i][j - 2] == 'A' and lines[i][j - 3] == 'S':
        total += 1

    if i + 3 < len(lines) and lines[i + 1][j] == 'M' and lines[i + 2][j] == 'A' and lines[i + 3][j] == 'S':
        total += 1

    if i - 3 >= 0 and lines[i - 1][j] == 'M' and lines[i - 2][j] == 'A' and lines[i - 3][j] == 'S':
        total += 1

    return total

def check_diagonal(i, j, line_len, lines):
    total = 0
    if i + 3 < len(lines) and j + 3 < line_len and lines[i + 1][j + 1] == 'M' and lines[i + 2][j + 2] == 'A' and lines[i + 3][j + 3] == 'S':
        total += 1

    if i - 3 >= 0 and j - 3 >= 0 and lines[i - 1][j - 1] == 'M' and lines[i - 2][j - 2] == 'A' and lines[i - 3][j - 3] == 'S':
        total += 1

    if i + 3 < len(lines) and j - 3 >= 0 and lines[i + 1][j - 1] == 'M' and lines[i + 2][j - 2] == 'A' and lines[i + 3][j - 3] == 'S':
        total += 1

    if i - 3 >= 0 and j + 3 < line_len and lines[i - 1][j + 1] == 'M' and lines[i - 2][j + 2] == 'A' and lines[i - 3][j + 3] == 'S':
        total += 1

    return total


if __name__ == '__main__':
    file_in = open('Fourth Input.txt', 'r')
    lines = file_in.read().split('\n')
    total = 0
    
    for i in range(len(lines)):
        line_len = len(lines[i])
        for j in range(0, line_len):
            if lines[i][j] != 'X':
                continue
            
            total += check_straight(i, j, line_len, lines) + check_diagonal(i, j, line_len, lines)
            
    print(total)
