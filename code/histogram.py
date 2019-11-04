import random

from collections import defaultdict, deque



class Histogram:
    def __init__(self):
        self.unique_words = 0
        self.num_words = 0
        self.hist = defaultdict(lambda: self._increment_unique())

    def __len__(self):
        return self.unique_words

    def _increment_unique(self):
        self.unique_words += 1
        return 0

    @staticmethod
    def _open_file(filepath):
        f = open(filepath, 'r')
        for line in f:
            for word in line.split():
                yield word

    def build_histogram(self, filepath):
        for word in self._open_file(filepath):
            self.num_words += 1
            self.hist[word] += 1

    def get_frequency(self, word):
        return self.hist[word]

    def get_ordered(self):
        running_sum = 0.0
        for word, freq in self.hist.items():
            running_sum += freq / self.num_words
            yield word, running_sum


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


    def build_tree(self, hist):
        '''
        Building a semi balanced tree (current implementation) by sorting from
        lowest extremes to highest. Using a double ended queue to switch
        between pulling a max and a min and adding them to another deque which
        I am using as a stack. Then I'll pop from the stack one at a time to
        build the tree.

        '''
        queue = deque(hist.get_ordered())
        stack = deque()
        if len(queue) % 2 != 0:
            stack.append(queue.pop())

        while len(queue) > 0:
            stack.appendleft(queue.popleft())
            stack.appendleft(queue.pop())

        if self.root is None:
            self.root = Node(*stack.popleft())

        for word, freq in stack:
            node = Node(word, freq)
            self.length += 1
            self.add(node)

