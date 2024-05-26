


class Node:

    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None






if __name__ == '__main__':

    linked_list = LinkedList()


    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)


    linked_list.head.next = second
    second.next = third
    third.next = fourth


    while linked_list.head != None:
        if linked_list.head.next != None:
            print(linked_list.head.item, end="-->")

        else:
            print(linked_list.head.item, end=" ")

        linked_list.head = linked_list.head.next

def reverse():
    linked_list.head = fourth
    two = third
    three = second
    four = linked_list.head



    linked_list.head.next = two
    two.next = three
    three.next = four

    while linked_list.head != None:
        if linked_list.head.next != None:
            print(linked_list.head.item, end="-->")

        else:
            print(linked_list.head.item, end=" ")

        linked_list.head = linked_list.head.next


reverse()