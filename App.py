from LinkedList import LinkedList;

linkedList = LinkedList();

linkedList.insertEnd(12);
linkedList.insertEnd(122);
linkedList.insertEnd(3);
linkedList.insertEnd(31);

linkedList.traverseList();
print("-------------------")
linkedList.insertStart(43);
linkedList.traverseList();
print("-------------------")

linkedList.remove(3);
linkedList.traverseList();

#linkedList.insertEnd(85);
