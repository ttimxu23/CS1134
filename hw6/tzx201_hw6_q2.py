"""
tzx201_hw6_q2
"""

from DoublyLinkedList import DoublyLinkedList

class Integer:
    def __init__(self, num_str):
        self.num = DoublyLinkedList()
        for digit in num_str:
            digit = int(digit)
            self.num.add_last(digit)
    def __repr__(self):
        out = ""
        for digit in self.num:
            out += str(digit)
        if len(out) > 0:

            while out[0] == '0' and len(out) > 1:
                out = out[1:]
        return out
    def __add__(self, other):
        sum = Integer("")
        curs1 = self.num.trailer.prev
        curs2 = other.num.trailer.prev
        carry = 0
        while curs1 != self.num.header and curs2 != other.num.header:
            tot = curs1.data + curs2.data + carry
            if tot >= 10:
                tot %= 10
                carry = 1
            else:
                carry = 0
            sum.num.add_first(tot)
            curs1 = curs1.prev
            curs2 = curs2.prev
        while curs1 != self.num.header:
            tot = curs1.data + carry
            carry = tot//10
            tot %= 10
            sum.num.add_first(tot)
            curs1 = curs1.prev
        while curs2 != other.num.header:
            tot = curs2.data + carry
            carry = tot//10
            tot %= 10
            sum.num.add_first(tot)
            curs2 = curs2.prev
        if carry > 0:
            sum.num.add_first(carry)
        return sum
    def __mul__(self, other):
        total = Integer("")
        zeroes = 0
        top_curs = self.num.trailer.prev
        bot_curs = other.num.trailer.prev
        while bot_curs != other.num.header:
            layer_tot = Integer("0"*zeroes)
            carry = 0
            while top_curs != self.num.header:
                curr = (top_curs.data * bot_curs.data) + carry
                if curr >= 10:
                    carry = curr//10
                    curr %= 10
                else:
                    carry = 0
                #print(curr)
                layer_tot.num.add_first(curr)
                top_curs = top_curs.prev
            if carry != 0:
                layer_tot.num.add_first(carry)
            top_curs = self.num.trailer.prev
            #print("layer total:", layer_tot)
            total = total + layer_tot
            zeroes += 1
            bot_curs = bot_curs.prev
        return total

    

def main():
    n1 = Integer("600")
    n2 = Integer("000")
    n3 = n1 * n2
    print(n3)

if __name__ == "__main__":
    main()

