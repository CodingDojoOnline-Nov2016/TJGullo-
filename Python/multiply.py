#Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

a = [2,4,10,16]
def multiply():
    a = [2,4,10,16]
    newList = []
    for i in a:
        newList.append(i*5)
    print newList

multiply()

def multiply2(lst, num):
    list1 = []
    for i in lst:
        list1.append(i*num)
    print list1

multiply2(a, 5)
