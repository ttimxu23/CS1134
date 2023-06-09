"""
tzx201_hw6_q3
"""

from DoublyLinkedList import DoublyLinkedList

class CompactString:
    def __init__(self, orig_str):
        self.str = DoublyLinkedList()
        count = 0
        for i in range(len(orig_str)):
            if i == 0:
                char = orig_str[i]
                count = 1
            else:
                if orig_str[i] == orig_str[i-1]:
                    count += 1
                    if i == len(orig_str) - 1:
                        self.str.add_last((char, count))
                else:
                    self.str.add_last((char, count))
                    char = orig_str[i]
                    count = 1
                    if i == len(orig_str) - 1:
                        self.str.add_last((char, count))
    def __add__(self, other):
        res = CompactString("")
        for tup in self.str:
            res.str.add_last(tup)
        if self.str.trailer.prev.data[0] == other.str.header.next.data[0]:
            char = self.str.trailer.prev.data[0]
            count = self.str.trailer.prev.data[1] + other.str.header.next.data[1]
            res.str.delete_last()
            res.str.add_last((char, count))
            other.str.delete_first()
        for tup in other.str:
            res.str.add_last(tup)
        return res
    def __lt__(self, other):
        curs1 = self.str.header.next
        curs2 = other.str.header.next
        count1 = 0
        count2 = 0
        just_moved = 0
        while curs1 != self.str.trailer and curs2 != other.str.trailer:
            char1 = curs1.data[0]
            char2 = curs2.data[0]
            if just_moved == 0:
                count1 += curs1.data[1]
                count2 += curs2.data[1]
            elif just_moved == 1:
                count1 += curs1.data[1]
            else:
                count2 += curs2.data[1]
            if ord(char1) < ord(char2):
                return True
            elif ord(char1) > ord(char2):
                return False
            if count1 > count2:
                curs2 = curs2.next
                just_moved = 2
            elif count2 > count1:
                curs1 = curs1.next
                just_moved = 1
            else:
                curs1 = curs1.next
                curs2 = curs2.next
                just_moved = 0
        #not sure if this covers every edge case
        if count1 < count2:
            return True
        return False
    def __le__(self, other):
        return not (other < self)
    def __gt__(self, other):
        return (other < self)
    def __ge__(self, other):
        return not (self < other)
    def __repr__(self):
        out = ""
        for elem in self.str:
            out += elem[0] * elem[1]
        return out

        



def main():
    word1 = CompactString("aaaaabbbaaaccc")
    word2 = CompactString("cccddddeeffg")
    word3 = word1 + word2
    print(word1 >= word2) #False
    print(word1 > word3) # False
    print(word2 > word3) #True
    print(word3.str)
    word4 = CompactString("aaabbcc")
    word5 = CompactString("aabbccc")
    print(word4 < word5) #True
    print(word5 < word4) #False
    word6 = CompactString("aaabbbcccc")
    word7 = CompactString("aaabbbccc")
    print(word6 <= word7) #False
    word8 = CompactString("New York")
    word9 = CompactString("New Jersey")
    print(word8.str)
    print(word9 >= word8) #False
    print(word9 >= word9) #True
    print(word9)
    print(word1)

if __name__ == "__main__":
    main()
    
            
            