from .node import TernaryNode


class TernaryTree:

    root = None
    
    def insert(self, value):
        value = value.replace('\n', '').strip()
        self.root = self.__insert(self.root, value)

    def search(self, word):
        '''
            Will search for a node with the path to it is equal to the
            characters sequence in the word.
            If the search return a Node, we will get all possible
            combinations, after that, will append the `word` as prefix in
            each combination found.
        '''
        node = self.__get_node(self.root, word)
        if node:
            _node = TernaryNode(node.character, node.is_end_of_string)
            _node.equal = node.equal

            if not word:
                _node.left = node.left
                _node.right = node.right
            else:
                word = word[:-1]

            if _node.has_child():
                combinations = self.__get_combinations_from_node(
                                        _node, prefix='', words=[''])
                return [word + item for item in combinations]
        return []
    
    def __get_node(self, node, word):
        '''
            While the last letter isn't reached, the function is called
            again until find the node with last letter.
            If doesn't find the node with expected letter,
            the function will return `None`.
        '''
        if not word:
            return node
        elif node.character == word[0]:
            if len(word) == 1:
                return node
            return self.__get_node(node.equal, word[1:])
        elif node.character > word[0] and node.left:
            return self.__get_node(node.left, word)
        elif node.character < word[0] and node.right:
            return self.__get_node(node.right, word)
        return None
    
    def __get_combinations_from_node(self, node, prefix='', words=['']):
        left = ['']
        if node.left is not None:
            left = self.__get_combinations_from_node(
                node.left,
                prefix or words[-1],
                left)

        right = ['']
        if node.right is not None:
            right = self.__get_combinations_from_node(
                node.right,
                prefix or words[-1],
                right)
        
        words[-1] += prefix + node.character
        if node.equal is not None:
            if node.is_end_of_string and node.has_child():
                words.append(words[-1])
            words = self.__get_combinations_from_node(node.equal, words=words)
        
        final = left + right + words
        return [item for item in final if item != '']

    def __insert(self, node, word):
        is_end = len(word) == 1
        if node is None:
            node = TernaryNode(word[0], is_end)
            if not is_end:
                node.equal = self.__insert(node.equal, word[1:])
            return node
        elif node.character == word[0]: # EQUAL
            if not is_end:
                node.equal = self.__insert(node.equal, word[1:])
            node.is_end_of_string = is_end if not node.is_end_of_string else True
            return node
        elif node.character > word[0]: # TO LEFT
            node.left = self.__insert(node.left, word)
            return node
        elif node.character < word[0]: # TO RIGHT
            node.right = self.__insert(node.right, word)
            return node
    
    def __call__(self, word):
        return self.search(word)
