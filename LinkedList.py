from random import randrange


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addv(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printlist(self):
        temp = self.head
        ls = []
        while temp:
            ls.append(temp.data)
            temp = temp.next
        print(ls)

    def selsort(self):
        cur = self.head
        while cur.next is not None:
            min = cur
            cmp = cur.next
            while cmp is not None:
                if cmp.data < min.data:
                    min = cmp
                cmp = cmp.next

            min.data, cur.data = cur.data, min.data
            cur = cur.next


ls = LinkedList()

for i in range (10):
    ls.addv(randrange(50))
ls.printlist()
ls.selsort()
ls.printlist()
