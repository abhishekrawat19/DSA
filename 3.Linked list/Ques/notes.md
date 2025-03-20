# Linked List in Python

## 1. Basic Structure of a Singly Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data  # Data stored in node
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node) of the linked list

    def append(self, data):
        """Add a node at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        """Add a node at the beginning"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        """Delete the first occurrence of a node with the given key"""
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def display(self):
        """Print the linked list"""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
```

## 2. Reverse a Linked List
```python
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # New head
```

## 3. Detect Cycle in a Linked List (Floyd’s Cycle Detection)
```python
def has_cycle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## 4. Find Middle of Linked List
```python
def find_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data  # Middle node's data
```

## 5. Merge Two Sorted Linked Lists
```python
def merge_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    if l1.data < l2.data:
        l1.next = merge_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_lists(l1, l2.next)
        return l2
```

