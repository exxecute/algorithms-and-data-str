from math import ceil

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self) -> str:
        return str(self.val)

class FrontMiddleBackQueue:
    def __init__(self):
        self.head: Node = None
        self.size = 0

    def __getLastNode(self) -> Node:
        nodeStep = self.head
        for _ in range(self.size - 1):
            nodeStep = nodeStep.next
        return nodeStep
    
    def __getMiddleNode(self) -> Node:
        nodeStep = self.head

        tempRange = 0
        if self.size % 2 == 0:
            tempRange = ceil(self.size / 2) + 1
        else:
            tempRange = ceil(self.size / 2)
        for _ in range(tempRange - 1):
            nodeStep = nodeStep.next
        return nodeStep

    def pushFront(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
        else:
            node = Node(val)
            lastNode = self.__getLastNode()
            lastNode.next = node
            node.prev = lastNode

        self.size += 1

    def pushMiddle(self, val: int) -> None:
        newNode = Node(val)
        if self.size == 0:
            self.head = newNode
        else:
            nodeStep = self.head
            for _ in range(ceil(self.size / 2)):
                nodeStep = nodeStep.next

            if nodeStep is None:
                self.pushFront(val)
                return
            newNode.next = nodeStep
            newNode.prev = nodeStep.prev
            nodeStep.prev.next = newNode
            nodeStep.prev = newNode
                
        self.size += 1

    def pushBack(self, val: int) -> None:
        if self.size == 0:
            self.head = Node(val)
        else:
            node = self.head
            self.head = Node(val)
            self.head.next = node
            node.prev = self.head

        self.size += 1

    def popFront(self) -> int:
        if self.size == 0:
            return -1
        else:
            lastNode = self.__getLastNode()
            if lastNode is None or lastNode.prev is None:
                return -1
            lastNode.prev.next = None
            self.size -= 1
            return lastNode.val

    def popMiddle(self) -> int:
        if self.size == 0:
            return -1
        else:
            middleNode = self.__getMiddleNode()
            if middleNode.prev is not None:
                middleNode.prev.next = middleNode.next
            if middleNode.next is not None:
                middleNode.next.prev = middleNode.prev
            self.size -= 1
            return middleNode.val

    def popBack(self) -> int:
        if self.size == 0:
            return -1
        else:
            poped: int = self.head.val
            self.head = self.head.next
            self.size -= 1
            return poped
    
    def __str__(self) -> str:
        string: str = ""
        node = self.head
        if node is None:
            return string
        for _ in range(self.size):
            string += str(node.val) + " "
            if node.next is not None:
                node = node.next
        return string
    
# if __name__ == "__main__":
#     methods = ["FrontMiddleBackQueue","popMiddle","popMiddle","pushMiddle","pushMiddle","popMiddle","popMiddle","popMiddle","popBack","popMiddle","popFront","pushBack","popFront","pushMiddle","pushMiddle","popMiddle","popBack","pushFront","popMiddle","pushMiddle","pushMiddle","pushMiddle","popMiddle","pushMiddle","popBack","pushMiddle","popMiddle","popMiddle","popMiddle","popMiddle","popFront","pushMiddle","pushMiddle","pushMiddle","pushFront"]
#     var = [[],[],[],[773222],[279355],[],[],[],[],[],[],[448905],[],[168284],[874541],[],[],[15656],[],[803226],[720129],[626048],[],[860306],[],[630886],[],[],[],[],[],[837735],[414354],[404946],[88719]]
#     operations = []
#     for i in range(len(methods)):
#         operations.append([methods[i], var[i]])
        
#     my_linked_list = FrontMiddleBackQueue()
#     for operation, args in operations:
#         print(operation, args)
#         if operation == "pushFront":
#             my_linked_list.pushFront(args[0])
#         elif operation == "pushMiddle":
#             my_linked_list.pushMiddle(args[0])
#         elif operation == "pushBack":
#             my_linked_list.pushBack(args[0])
#         elif operation == "popFront":
#             print(my_linked_list.popFront())
#         elif operation == "popMiddle":
#             print(my_linked_list.popMiddle())
#         elif operation == "popBack":
#             print(my_linked_list.popBack())
#         print(my_linked_list)
