list = []

def add_nums(list):
    number = int(input("enter number to add in the list: "))
    while number != -1:
        number = int(input("enter another number or enter -1 to quit: "))
        list.append(number)
    return list

def max(list):
    max = list[0]

    for i in range (1,len(list)):
        if list[i] > max:
            max = list[i]
    return max

add_nums(list)
print("the maximum number in the list is ", max(list))






