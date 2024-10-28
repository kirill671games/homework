a = int(input())
b = int(input())
def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)
nod(a, b)

