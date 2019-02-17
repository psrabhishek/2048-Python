from math import log
from random import randint

mat = [[0 for i in range(4)] for j in range(4)]
score = 0


def merge(count):
    global mat, score
    for i in range(count):
        mat = list(zip(*mat[::-1]))
    result = []
    for nums in mat:
        prev = None
        store = []
        for next_ in nums:
            if not next_:
                continue
            if prev is None:
                prev = next_
            elif prev == next_:
                score += prev
                store.append(prev + next_)
                prev = None
            else:
                store.append(prev)
                prev = next_
        if prev is not None:
            store.append(prev)
        store.extend([0] * (4 - len(store)))
        result.append(store)
    for i in range(-count % 4):
        result = list(zip(*result[::-1]))
        mat = list(zip(*mat[::-1]))
    mat = [list(i) for i in mat]
    result = [list(i) for i in result]
    if result != mat:
        mat = result
        insert_num()
    else:
        zeros = 0
        for i in mat:
            zeros += i.count(0)
        if zeros == 0:
            print("Game Over\t Score =", score)
            exit(0)


def rearrange(ip):
    count = {'w': 3, 'a': 0, 's': 1, 'd': 2}
    if ip in count:
        merge(count[ip])
    else:
        print("w|S|A|D only")


def print_mat():
    print("+" + "-" * 35 + "+")
    for i in mat:
        c = "|"
        for j in i:
            print("|{:4d}".format(j), end="    ")
        if i == mat[-1]:
            c = "+"
        print("|\n" + c + "-" * 35 + c)
    print("Score =", score)


def insert_num():
    global mat, sore
    zeros = []
    for i in mat:
        for j in i:
            if j == 0:
                zeros.append((mat.index(i), i.index(j)))
    if len(zeros) == 0:
        print("Game Over\t Score =",score)
        exit(0)
    pos = zeros[randint(0, len(zeros)-1)]
    high = max(max(mat, key=lambda x: max(x)))
    if high != 0:
        high = log(high, 2)
    else:
        high = 1
    mat[pos[0]][pos[1]] = 2**randint(1, high)


def main():
    print("Controls:\tW - Up | S - Down | A - Left | D - Right ")
    insert_num()
    while True:
        print_mat()  # printing the Matrix even if there is no change for players convinience
        ch = input("=>").lower()
        rearrange(ch)


if __name__ == "__main__":
    main()
