import sys

a=0
g=0
t=0
c=0

for seq in sys.argv:
    for x in list(seq):
        match x:
            case "A": a+=1
            case "G": g+=1
            case "C": c+=1
            case "G": g+=1

print("A:", a)
print("G:", g)
print("T:", t)
print("C:", c)
