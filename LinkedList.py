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

ls.addv(10)
ls.addv(23)
ls.addv(1)
ls.addv(6)
ls.addv(90)
ls.addv(4)
ls.addv(1)
ls.addv(10)
ls.addv(15)


ls.printlist()

ls.selsort()

ls.printlist()
