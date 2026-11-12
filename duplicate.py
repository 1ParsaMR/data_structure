# Parsa Rafiei

print("=====Welcome to duplicate finder=====")

def dup(x):
    if (len(x) % 2 == 0):
        if (len(x) == 0):
            return True
        elif (x[:len(x)//2] == x[len(x)//2:]):
            x = x[1:len(x)//2]
            return dup(x)
        else:
            return False
    else:
        return False

if dup(input("please enter your string: ")):
    print("It's a duplicate")
else:
    print("Not a duplicate")