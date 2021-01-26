from random import randrange

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def printlist(self):
        temp = self.head
        ll = []
        while temp:
            ll.append(temp.data)
            temp = temp.next
        print(ll)

    def reverse(self):
        def _reverse(temp):
            if temp is None:
                return
            else:
                _reverse(temp.next)
                print(temp.data)

        _reverse(self.head)

    def selsort(self):
        prevcur = None
        cur = self.head
        while cur.next is not None:
            prevmin = cur
            min = cur.data
            minpos = cur
            ismin = cur.next
            while ismin is not None:
                if ismin.data < min:
                    min = ismin.data
                    minpos = ismin
                prevmin = ismin
                ismin = ismin.next
            self.swap(cur, prevcur, ismin, prevmin)
            #minpos.data, cur.data = cur.data, minpos.data
            prevcur = cur
            cur = cur.next

    def swap(self, cur, prevcur, ismin, prevmin):
        # If x is not head of linked list
        if prevcur is not None:
            prevcur.next = ismin
        else:  # make y the new head
            self.head = ismin

        # If y is not head of linked list
        if prevmin is not None:
            prevmin.next = cur
        else:  # make x the new head
            self.head = cur

        # Swap next pointers
        temp = cur.next
        cur.next = ismin.next
        ismin.next = temp


list0 = LinkedList()

for i in range(10):
    list0.insert(randrange(50))

list0.printlist()
list0.selsort()
list0.printlist()
