#Zachary Zawaideh
#11/5/17
#Computer Programming


def name_print():
    name= input("What is your word?: ")
    index= -1
    while index >= (-1 * len(name)):
        last = name[index]
        print(last)
        index= index -1

name_print()
