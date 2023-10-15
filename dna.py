import sys

a=0
g=0
t=0
c=0
dnaArgs=[]

match sys.argv:
    case [_, "version"]:
        print("version 1.0")
        quit()
    case seqs:
        dnaArgs = seqs[1:]

# some other comment
# multiple args handling
for seq in dnaArgs:
    for x in list(seq):
        match x:
            case "A": a+=1
            case "G": g+=1
            case "C": c+=1
            case "G": g+=1

print("x")
print("y")
print("A:", a)
print("G:", g)
print("T:", t)
print("C:", c)
