#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        self.count = 0
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def replace(self, old_item, new_item):
        """O(1) to O(n) same as find"""
        current = self.head
        while current:
            if current.data == old_item:
                current.data == new_item

            current = current.next

        if current is None:
            raise ValueError(f'Item not found: {old_item}')


    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) Just calls self.count"""
        return self.count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) always 1 because tail is stored"""

        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node

        self.count += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Same as append but with head"""

        node = Node(item)
        if self.is_empty():
            self.head = node
            self.tail = node

        else:
            self.head.previous = node
            node.next = self.head
            self.head = node

        self.count += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) it could be at the beginning
        TODO: Worst case running time: O(n) at the end of the list"""
        current = self.head
        while current:
            if quality(current.data):
                return current.data

            current = current.next


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) same as find
        TODO: Worst case running time: O(n) same as find"""

        current = self.head
        while current:
            if current.data == item:
                break

            current = current.next

        if current is None:
            raise ValueError(f'Item not found: {item}')

        if current.previous is None:
            self.head = current.next

        else:
            current.previous.next = None

        if current.next is None:
            self.tail = current.previous

        else:
            current.next.previous = None

        if current.previous and current.next:
            current.previous.next = current.next
            current.next.previous = current.previous

        self.count -= 1


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))



if __name__ == '__main__':
    test_linked_list()
