# This program includes finding the -ve or +ve number with the time complexity of 0(1) (Normal approach)


has = [[0 for i in range(2)] for j in range(10)]

def insert(container):

    for index,value in enumerate(container):
        print(index,value)

        if value >= 0:
            has[value][0] = 1

        else:
            has[abs(value)][1] = 1


def search(key):
    if key >= 0:
        return has[key][0] == 1

    else:
        return has[abs(key)][1] == 1


insert([-1,9,-5,-8,-5,-2])
print(has)
x = 8
if search(x) == 1:
    print("present")

else:
    print("Not present")


