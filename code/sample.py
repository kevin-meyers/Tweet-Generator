import random

from collections import deque

class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.right = None
        self.left = None


class WordFreqTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, new_node):
        current = self.root

        while True:
            if new_node.freq < current.freq:
                if current.left is None:
                    current.left = new_node
                    break

                else:
                    current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    break

                else:
                    current = current.right

    def __len__(self):
        return self.length


    def _find_word(self, val, node):
        if val < node.freq:
            if node.left is None:
                return node.word

            self._find_word(val, node.left)

        else:
            if node.right is None:
                return node.word

            self._find_word(val, node.right)


    def sample(self):
        rand = random.random()
        if self.root is None:
            raise ValueError('Tree not built yet, try build_tree')

        current = self.root
        while True:
            if rand < current.freq:
                if current.left is None:
                    return current.word

                current = current.left

            else:
                if current.right is None:
                    return current.word

                current = current.right


    def build_tree(self, sorted_words_freq_tuple):
        '''
        Building a semi balanced tree (current implementation) by sorting from
        lowest extremes to highest. Using a double ended queue to switch
        between pulling a max and a min and adding them to another deque which
        I am using as a stack. Then I'll pop from the stack one at a time to
        build the tree.

        '''
        queue = deque(sorted_words_freq_tuple)
        stack = deque()

        if len(queue) % 2 != 0:
            stack.appendleft(queue.pop())


        while len(queue) > 0:
            stack.appendleft(queue.popleft())
            stack.appendleft(queue.pop())

        if self.root is None:
            self.root = Node(*stack.popleft())

        for num, (word, freq) in enumerate(stack):
            node = Node(word, freq)
            self.length += 1
            self.add(node)
