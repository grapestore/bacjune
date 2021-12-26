# 큐 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Que:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __bool__(self):
        if self.__size:
            return True
        else:
            return False

    def size(self):
        return self.__size

    def append(self, arg):
        arg = Node(arg)
        if not self.__size:
            self.head = arg
            self.tail = arg
        else:
            self.tail.next = arg
            self.tail = self.tail.next
        self.__size += 1

    def pop(self):
        if not self.__size:
            return IndexError
        else:
            r = self.head.data
            self.head = self.head.next
            self.__size -= 1
            return r

    def display(self):
        string = ""
        tem = self.head
        while tem:
            string += str(tem.data)
            string += ", "
            tem = tem.next
        string = string.rstrip(", ")
        string += ""
        return string
