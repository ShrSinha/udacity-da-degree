from linkedlist import Element,LinkedList

# Test cases
# Set up some Elements
e1 = Element(1.1)
e2 = Element(1.1)
e3 = Element(2.1)
e4 = Element(3.1)

# Start setting up a LinkedList
linkedl = LinkedList(e1)
linkedl.append(e2)
linkedl.append(e3)
linkedl.append(e4)

# Test get_element
#print(linkedl.get_element(1).value,linkedl.head.value)
#print(linkedl.get_element(2).value,linkedl.head.next.value)
#print(linkedl.get_element(3).value,linkedl.head.next.next.value)
print(linkedl.get_element(4).value,linkedl.head.next.next.next.value)
#print(linkedl.get_element(5).value,linkedl.head.next.next.next.next.value)

# Test delete
# Test delete
linkedl.delete_all(1.1)
# Should print 2 now
print("Should print 2 now: {}".format(linkedl.get_element(1).value))
# Should print 3 now
print("Should print 3 now: {}".format(linkedl.get_element(2).value))
