##################################################################
#   SCROLL DOWN - UNIMPLEMENTED MEMBERS AT THE BOTTOM OF SCRIPT 
##################################################################

from NodeModule import Node

# Singly linked list implementation
class DsList:
    # DsList constructor
    def __init__(self):
        self.head = None
        
    def format_value(self,value):
        if type(value) == str:
            return f"'{value}'"
        else:
            return f"{value}"

    # format print output
    def __str__(self):
        print_string = ""
        if self.head == None:
            return "[]"
        
        print_string += "["
        node = self.head
        print_string += f"{self.format_value(node.data)}"
        while node.next:
            node = node.next
            print_string += f", {self.format_value(node.data)}"
        
        print_string += "]"
        return print_string

    # insert element at a specific index
    def insert(self, index, value):
        node = self.head
        count = 0    

        if index == 0:
            self.head = Node(value)
            self.head.next = node
            return
        
        while node:
            if count == index - 1:
                node_next = node.next
                node.next = Node(value)
                node.next.next = node_next
                return
            node = node.next
            count += 1

    # +remove+ element at a specific index
    def remove(self, index):
        node = self.head
        count = 0    
        if node == None:
            return
        
        if index == 0:
            if node.next:
                self.head = node.next
                return
            else:
                self.head = None
        if index == (len(self) - 1):
            while node:
                if count + 1 == index:
                    node.next = None
                    return
                node = node.next
                count+=1
        else:
            while node:
                if count == index - 1:
                    node.next = node.next.next
                    return
                node = node.next
                count += 1

##########################################################
# Complete the DsList members below
##########################################################

    # Append data to the end of the list
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        current_node = self.head
        pass

    # count of nodes
    def __len__(self):
        pass
    
    # retrieve value of specific element 
    def __getitem__(self, index):
        pass

    # +set data of specific element 
    def __setitem__(self, index, value):
        pass

    # provide +ability to use DsList in a loop
    def __iter__(self):
        pass

    # pro+vid+e ability to add two DsLists together
    # ds_list3 = ds_list1 + ds_list2
    def __add__(self, other):
        pass
        
    # provide ability to u+-se the IN operator. e.g. if 'abc' in letters:
    def __contains__(self, value):
        pass
    
    # delete all elements
    def clear(self):
        pass


      