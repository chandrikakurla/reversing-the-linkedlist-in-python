#node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#linkedlist class
class LinkedList:
    def __init__(self):
        self.head=None
    #function to push the newnodes into linkedlist
    def push(self,newnode):
        if self.head is None:
            self.head=newnode
            return
        temp=self.head
        self.head=newnode
        newnode.next=temp
    #function for printing linkedlist elements
    def printllist(self):
        currentnode=self.head
        if currentnode is None:
            print("linkedlist is empty")
            return
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode=currentnode.next
    #function to reverse linkedlist
    def rev_llist(self):
        previousnode=None
        nextnode=None
        currentnode=self.head
        if self.head is None:
            return
        while(currentnode is not None):
            nextnode=currentnode.next
            currentnode.next=previousnode
            previousnode=currentnode
            currentnode=nextnode
        self.head=previousnode
        
if __name__ == "__main__":
    llist=LinkedList()
    firstnode=Node(1)
    secondnode=Node(2)
    thirdnode=Node(3)
    fourthnode=Node(4)
    fifthnode=Node(5)
    llist.push(firstnode)
    llist.push(secondnode)
    llist.push(thirdnode)
    llist.push(fourthnode)
    llist.push(fifthnode)
    print("linkedlist before swapping")
    llist.printllist()
    llist.rev_llist()
    print("linkedlist after swapping")
    llist.printllist()  

    

            




