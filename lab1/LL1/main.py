

class Node:
    def __init__(self, val: int = 0, next: 'Node' = None):
        self.__next: Node = next 
        self.__val: int = val

    def getNext(self) -> 'Node':
        return self.__next
    
    def getVal(self) -> int:
        return self.__val
    
    def setNext(self, next: 'Node') -> None:
        self.__next = next

class MyLinkedList:
    def __init__(self):
        self.__head: Node = None

    def get(self, index: int) -> int:
        nodeStep: Node = self.__head
        for i in range(index):
            nodeStep = nodeStep.getNext()
            if nodeStep is None:
                return -1
        if nodeStep is None:
            return -1
        return nodeStep.getVal()

    def addAtHead(self, val: int) -> None:
        self.__head: Node = Node(val= val, next= self.__head)

    def addAtTail(self, val: int) -> None:
        nodeStep: Node = self.__head
        if nodeStep is None:
            self.addAtHead(val)
            return
        while nodeStep.getNext() is not None:
            nodeStep = nodeStep.getNext()
        nodeStep.setNext(Node(val))

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        nodeStep = self.__head
        if nodeStep is None:
            return
        for _ in range(index - 1):
            nodeStep = nodeStep.getNext()
            if nodeStep is None:
                return
        if nodeStep is not None:
            nodeStep.setNext(Node(val, nodeStep.getNext()))

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            if self.__head is None:
                return
            self.__head = self.__head.getNext()
        else:
            if self.__head is None:
                return
            previous: Node = self.__head
            for _ in range(index - 1):
                previous = previous.getNext()
                if previous is None:
                    return
            
            if previous.getNext() is None:
                return
            if previous.getNext().getNext() is None:
                previous.setNext(None)
                return
            previous.setNext(previous.getNext().getNext())

    def printList(self) -> None:
        nodeStep: Node = self.__head
        while nodeStep is not None:
            print(nodeStep.getVal(), end="->")
            nodeStep = nodeStep.getNext()

if __name__ == "__main__":
    methods = ["MyLinkedList","addAtIndex","addAtIndex","addAtTail","get","deleteAtIndex","get"]
    var = [[],[2,1],[3,4],[1],[0],[0],[0]]
    operations = []
    for i in range(len(methods)):
        operations.append([methods[i], var[i]])
        # print(operations[i])
        
    my_linked_list = MyLinkedList()
    for operation, args in operations:
        print(operation, args)
        if operation == "addAtHead":
            my_linked_list.addAtHead(args[0])
        elif operation == "addAtTail":
            my_linked_list.addAtTail(args[0])
        elif operation == "addAtIndex":
            my_linked_list.addAtIndex(args[0], args[1])
        elif operation == "get":
            print(my_linked_list.get(args[0]))
        elif operation == "deleteAtIndex":
            my_linked_list.deleteAtIndex(args[0])
        print(my_linked_list.printList())