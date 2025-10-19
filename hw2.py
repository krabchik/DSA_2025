class OneWayNode:
    def __init__(self, data = 0):
        self.data = data
        self.next: 'OneWayNode | None' = None

class TwoWayNode(OneWayNode):
    def __init__(self, data = 0):
        self.previous: 'TwoWayNode | None' = None
        super().__init__(data)

class Stack:
    def __init__(self):
        self.head: OneWayNode | None = None

    def push(self, data):
        new = OneWayNode(data)
        new.next = self.head
        self.head = new

    def pop(self):
        if not self.head:
            return None
        head = self.head
        self.head = self.head.next
        return head.data

    def peek(self):
        return self.head.data

    def is_empty(self) -> bool:
        return self.head is None

class Queue:
    def __init__(self):
        self.head: TwoWayNode = TwoWayNode()
        self.tail: TwoWayNode = TwoWayNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, value):
        new_node = TwoWayNode(value)
        new_node.next = self.head.next
        new_node.previous = self.head
        self.head.next.previous = new_node
        self.head.next = new_node

    def pop(self):
        if self.head.next == self.tail:
            return None
        pop_result = self.tail.previous
        self.tail.previous = pop_result.previous
        pop_result.previous.next = pop_result.next
        pop_result.next = None
        pop_result.previous = None
        return pop_result.data

    def peek(self):
        return self.tail.previous.data

    def is_empty(self) -> bool:
        return self.head.next == self.tail

def nodes_to_list(head: OneWayNode | None) -> list:
    list_ = []
    while head:
        list_.append(head.data)
        head = head.next
    return list_

def has_cycle(head: OneWayNode) -> bool:
    if not head or not head.next:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

def reverse(head: OneWayNode) -> OneWayNode | None:
    prev = None
    current = head
    while current:
        next_ = current.next
        current.next = prev
        prev = current
        current = next_
    head = prev
    return head

def get_middle_node(head: OneWayNode | None) -> OneWayNode | None:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def remove_element_by_data(head: OneWayNode, data) -> OneWayNode:
    dummy = OneWayNode()
    dummy.next = head
    prev = dummy
    cur = head
    while cur:
        if cur.data == data:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next

def str_is_original_queue(original: str, new: str) -> bool:
    q = Queue()
    for el in original:
        q.push(el)

    for el in new:
        if q.peek() == el:
            q.pop()
    return q.is_empty()

def str_is_original_pointers(original: str, new: str) -> bool:
    i = 0
    j = 0
    len_original = len(original)
    len_new = len(new)
    while i < len_original and j < len_new:
        if new[j] == original[i]:
            i += 1
        j += 1
    return i == len_original

def is_palindrome_stack(s: str) -> bool:
    stack = Stack()
    for char in s:
        stack.push(char)
    for char in s:
        if char != stack.pop():
            return False
    return True

def is_palindrome_pointers(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def merge_sorted(first: OneWayNode, second: OneWayNode) -> OneWayNode:
    dummy = current = OneWayNode()
    while first and second:
        if first.data < second.data:
            current.next = first
            current = first
            first = first.next
        else:
            current.next = second
            current = second
            second = second.next
    extra_elements = first or second
    while extra_elements:
        current.next = extra_elements
        current = extra_elements
        extra_elements = extra_elements.next
    return dummy.next

def test_list_has_cycle():
    # No cycle (1 -> 2 -> 3)
    head = OneWayNode(1)
    head.next = OneWayNode(2)
    head.next.next = OneWayNode(3)
    assert not has_cycle(head)

    # Has cycle (1 -> 2 -> 3 -> 2)
    head.next.next.next = head.next
    assert has_cycle(head)

def test_reverse():
    head = OneWayNode(1)
    head.next = OneWayNode(2)
    head.next.next = OneWayNode(3)
    straight_list = nodes_to_list(head) # 1 2 3

    head = reverse(head) # Reverses in-place but returns new head
    reversed_list = nodes_to_list(head) # 3 2 1

    assert straight_list == reversed_list[::-1]

def test_get_middle_node():
    assert get_middle_node(None) is None

    head = OneWayNode(1)
    head.next = OneWayNode(2)
    head.next.next = OneWayNode(3)
    middle_node = get_middle_node(head)
    assert middle_node == head.next
    assert middle_node.data == 2

    head.next.next.next = OneWayNode(4)
    middle_node = get_middle_node(head)
    assert middle_node == head.next.next
    assert middle_node.data == 3

def test_remove_element_by_data():
    head = OneWayNode(1)
    head.next = OneWayNode(2)
    head.next.next = OneWayNode(3)

    head = remove_element_by_data(head, 4)
    assert nodes_to_list(head) == [1, 2, 3]

    head = remove_element_by_data(head, 2)
    assert nodes_to_list(head) == [1, 3]

    head = remove_element_by_data(head, 1)
    assert nodes_to_list(head) == [3]

    head = remove_element_by_data(head, 3)
    assert nodes_to_list(head) == []

    head = remove_element_by_data(head, 5)
    assert nodes_to_list(head) == []

def test_str_is_original():
    assert str_is_original_queue    ('abc', '-a--b---c----') == True
    assert str_is_original_pointers ('abc', '-a--b---c----') == True

    assert str_is_original_queue    ('abc', '-a--b---e----') == False
    assert str_is_original_pointers ('abc', '-a--b---e----') == False

def test_is_palindrome():
    assert is_palindrome_stack    ('abc')   == False
    assert is_palindrome_pointers ('abc')   == False

    assert is_palindrome_stack    ('abcba') == True
    assert is_palindrome_pointers ('abcba') == True

def test_merge_sorted():
    # first - 1 3 4 6
    first = OneWayNode(1)
    first.next = OneWayNode(3)
    first.next.next = OneWayNode(4)
    first.next.next.next = OneWayNode(6)

    # second - 1 2 5 7 8
    second = OneWayNode(1)
    second.next = OneWayNode(2)
    second.next.next = OneWayNode(5)
    second.next.next.next = OneWayNode(7)
    second.next.next.next.next = OneWayNode(8)

    merged = merge_sorted(first, second)
    assert nodes_to_list(merged) == [1, 1, 2, 3, 4, 5, 6, 7, 8]

def test_all():
    functions_to_test = [
        test_list_has_cycle,
        test_reverse,
        test_get_middle_node,
        test_remove_element_by_data,
        test_str_is_original,
        test_is_palindrome,
        test_merge_sorted
    ]
    for test_func in functions_to_test:
        test_func()


if __name__ == '__main__':
    test_all()