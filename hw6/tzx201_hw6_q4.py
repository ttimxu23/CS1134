"""
tzx201_hw6_q4
"""

from DoublyLinkedList import DoublyLinkedList

#a: shallow copy
def copy_linked_list(lnk_lst):
    new_lst = DoublyLinkedList()
    for elem in lnk_lst:
        new_lst.add_last(elem)
    return new_lst

def test_a():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)
    lnk_lst2 = copy_linked_list(lnk_lst1)
    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data) #shld be 10

#test_a()

#b: deep copy
def deep_copy_linked_list(lnk_lst):
    new_lst = DoublyLinkedList()
    for elem in lnk_lst:
        if type(elem) == int:
            new_lst.add_last(elem)
        else:
            new_lst.add_last(deep_copy_linked_list(elem))
    return new_lst

def test_b():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)
    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)

#test_b()

