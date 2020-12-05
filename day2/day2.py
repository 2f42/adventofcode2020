def is_valid1(minimum : int, maximum : int, char : str, s : str) -> bool:
    count = 0
    for c in s:
        if c == char:
            count += 1
            if count > maximum:
                return False
    if count < minimum:
        return False
    return True

def is_valid2(pos1 : int, pos2: int, char : str, s : str) -> bool:
    count = int(s[pos1-1] == char) + int(s[pos2-1] == char)
    return count == 1

def main():
    count = 0
    with open("input.txt") as f:
        for line in f.readlines():
            sp = line.replace("-", " ").replace(":", " ").split()
            count += int(is_valid2(int(sp[0]), int(sp[1]), sp[2], sp[3]))
    print(count)

main()
