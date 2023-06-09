"""cs1134 lab 14 coding"""

from ChainingHashTableMap import ChainingHashTableMap
from DoublyLinkedList import DoublyLinkedList
#1a: most_frequent
def most_frequent(lst):
    if len(lst) == 0:
        raise Exception("List is empty")
    freq = ChainingHashTableMap()
    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    max = freq[lst[0]]
    for num in lst:
        if freq[num] > max:
            max = num
    return max

def q1a_test():
    lst = [5,9,2,9,0,5,9,7]
    print(most_frequent(lst))
#q1a_test()

#1b: first_unique
def first_unique(lst):
    if len(lst) == 0:
        raise Exception("List is empty")
    freq = ChainingHashTableMap()
    for num in lst:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    for num in lst:
        if freq[num] == 1:
            return num
    return None #no unique numbers
        
def q1b_test():
    lst = [5,9,2,9,0,5,9,7]
    print(first_unique(lst))
#q1b_test()

#1c: worst extra space complexity is O(n) no matter what the input list is

#2: two_sum
def two_sum(lst, target):
    num_ind = ChainingHashTableMap()
    for i in range(len(lst)):
        num_ind[lst[i]] = i
    for num1 in lst:
        #is it valid if a singular number is equal to the target number
        # if num1 == target:
        #     return (num1, None)
        num2 = target - num1
        #Doesn't let the same index be returned twice
        #Cut the second half of the next line to change that
        if num2 in num_ind and num_ind[num1] != num_ind[num2]:
                return (num_ind[num1], num_ind[num2])
    return (None, None)

def q2_test():
    lst = [-2, 11, 15, 21, 20, 7]
    print(two_sum(lst, 22))
#q2_test()

#3: Playlist ADT
class PlayList():
    def __init__(self):
        self.songs = ChainingHashTableMap()
        self.order = DoublyLinkedList()
    def add_song(self, song_name):
        new_node = self.order.add_last(song_name)
        self.songs[song_name] = new_node
    def add_song_after(self, song_name, new_song_name):
        if song_name not in self.songs:
            raise KeyError("song_name not in playlist")
        add_after = self.songs[song_name]
        new_node = self.order.add_after(add_after, new_song_name)
        self.songs[new_song_name] = new_node
    def play_song(self, song_name):
        if song_name not in self.songs:
            raise KeyError("song_name not in playlist")
        print("Playing", song_name)
    def play_list(self):
        for song in self.order:
            print("Playing", song)

def q3_test():
    p1 = PlayList( )
    p1.add_song("Jana Gana Mana") 
    p1.add_song("Kimi Ga Yo") 
    p1.add_song("The Star-Spangled Banner") 
    p1.add_song("March of the Volunteers") 
    p1.add_song_after("The Star-Spangled Banner", "La Marcha Real")
    p1.add_song_after("Kimi Ga Yo", "Aegukga") 
    p1.add_song("Arise, O Compatriots")
    p1.add_song("Chant de Ralliement") 
    p1.add_song_after("Chant de Ralliement", "Himno Nacional Mexicano")
    p1.add_song_after("Jana Gana Mana", "God Save The Queen")

    p1.play_song("The Star-Spangled Banner")
    p1.play_song("Jana Gana Mana")

    p1.play_list( )
q3_test()

#vitamin help
def mad(num, N):
    p = 107
    a = 1
    b = 2
    val = ((a*num + b)%p)%(N*2)
    return val

def nums():
    #print(37,mad(37,7))
    print(47,mad(47,7))
    print(51,mad(51,7))
    print(65,mad(65,7))
    print(104,mad(104,7))
    print(8,mad(8,7))
    print(5,mad(5,7))
    print(10,mad(10,7))
    print(7,mad(7,7))
#nums()
