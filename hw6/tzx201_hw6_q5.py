"""
tzx201_hw6_q5
"""

from DoublyLinkedList import DoublyLinkedList

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    """
    def merge_sublists(lst1, lst2):
        if lst1.is_empty():
            new_lst = DoublyLinkedList()
            for elem in lst2:
                new_lst.add_last(elem)
            return new_lst
        elif lst2.is_empty():
            new_lst = DoublyLinkedList()
            for elem in lst2:
                new_lst.add_last(elem)
            return new_lst
        else:
            val1 = lst1.header.next.data
            val2 = lst2.header.next.data
            print(val1, val2)
            if val1 < val2:
                rem = lst1.delete_first()
                rest = merge_sublists(lst1, lst2)
                rest.add_first(rem)
                lst1.add_first(rem)
                #print(rest)
                return rest
            else:
                rem = lst2.delete_first()
                rest = merge_sublists(lst1, lst2)
                rest.add_first(rem)
                lst2.add_first(rem)
                #print(rest)
                return rest
    return merge_sublists(srt_lnk_lst1, srt_lnk_lst2)
    """
    def merge_sublists(node1, node2):
        if node1.next == None: # or node1.next.data == None
            other_rest = DoublyLinkedList()
            while node2.data != None:
                other_rest.add_last(node2.data)
                node2 = node2.next
            if node1.data is not None:
                other_rest.add_first(node1.data)
            return other_rest
        elif node2.next == None: # or node2.next.data == None
            other_rest = DoublyLinkedList()
            while node1.data != None:
                other_rest.add_last(node1.data)
                node1 = node1.next
            if node2.data is not None:
                other_rest.add_first(node2.data)
            return other_rest
        else:
            val1 = node1.data
            val2 = node2.data
            if val1 < val2:
                merge_rest = merge_sublists(node1.next, node2)
                merge_rest.add_first(val1)
                return merge_rest
            else:
                merge_rest = merge_sublists(node1, node2.next)
                merge_rest.add_first(val2)
                return merge_rest
    return merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next)




def main():
    lst1 = DoublyLinkedList()
    lst1.add_last(1)
    lst1.add_last(3)
    lst1.add_last(5)
    lst1.add_last(6)
    lst1.add_last(8)
    lst2 = DoublyLinkedList()
    lst2.add_last(2)
    lst2.add_last(3)
    lst2.add_last(5)
    lst2.add_last(10)
    lst2.add_last(15)
    lst2.add_last(18)
    #works but fucks up the input lists
    #nvm i think it works now
    lst3 = merge_linked_lists(lst1, lst2)
    #print(lst1, lst2)
    print(lst3)
    lst4 = DoublyLinkedList()
    lst5 = DoublyLinkedList()
    lst4.add_last(9)
    lst5.add_last(8)
    lst5.add_last(9)
    lst5.add_last(10)
    lst6 = merge_linked_lists(lst4, lst5)
    print(lst6)

if __name__ == "__main__":
    main()
