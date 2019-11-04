from collections import defaultdict



class Histogram:
    def __init__(self):
        self.unique_words = 0
        self.num_words = 0
        self.hist = defaultdict(lambda: _incrememnt_unique())

    def _incrememnt_unique(self):
        self.unique_words += 1
        return 0

    @staticmethod
    def _open_file(filepath):
        f = open(filepath, 'r')
        for line in f:
            for word in line:
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
            running_sum += freq / num_words
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

    def _add(self, new_node, current_node=None):
        if current_node is None:
            current_node = self.root

        if new_node.freq < current_node.freq:
            if current_node.left is not None:
                self._add(new_node, current_node.left)

            else:
                current_node.left = new_node

        else:
            if current_node.right is not None:
                self._add(new_node, current_node.right)

            else:
                current_node.right = new_node


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
            self._add(node)

