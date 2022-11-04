import sympy
m = [[]]
with open("nutrition1.txt", 'r') as f:
    for _ in range(7):
        m = f.readline()
        m = m[:-1]
        t = m.split('\t')
        print(t)
