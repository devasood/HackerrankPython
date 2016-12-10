
def checklambda(f, given):
    flag = False;
    for char in given:
        if f(char):
            flag = True
            break
    print(flag)
