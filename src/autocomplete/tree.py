from .node import TernaryNode


class TernaryTree:

    root = None
    
    def insert(self, value):
        value = value.replace('\n', '').strip()
        if self.root is None:
            self.root = TernaryNode(value[0])
            value = value[1:]
        self.__insert(self.root, value)

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
            default = []
            if node.is_end_of_string:
                default.append(word)
            
            if node.has_child():
                combinations = self.__get_combinations_from_node(node.equal)
                return default + [word + item for item in combinations]
            
            return default
        return []
    
    def __get_node(self, node, word):
        '''
            While the last letter isn't reache, the function is called
            again until find the node with last letter.
            If doesn't find the node with expected letter,
            the function will return `None`.
        '''
        if node.character == word[0]:
            if len(word) == 1:
                return node
            return self.__get_node(node.equal, word[1:])
        elif node.character > word[0]:
            return self.__get_node(node.left, word)
        elif node.character < word[0]:
            return self.__get_node(node.right, word)
        return None
    
    def __get_combinations_from_node(self, node, prefix='', words=['']):
        if node.is_end_of_string and node.has_child():
            words.append(words[-1])

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
            words = self.__get_combinations_from_node(node.equal, words=words)
        
        final = left + right + words
        return [item for item in final if item != '']

    def __insert(self, node, word):
        is_end = len(word) == 1

        # If node doesn't have the `equal` pointer, it'll receive a new
        # node with letter -> `word[0]`
        if node.equal is None:
            if not is_end and node.character == word[0]:
                self.__insert(node, word[1:])
            else:
                node.equal = TernaryNode(word[0], is_end)
                if not is_end:
                    self.__insert(node.equal, word[1:])
        elif node.character == word[0]: # EQUAL
            if not is_end:
                self.__insert(node.equal, word[1:])
            if node.is_end_of_string == False:
                node.is_end_of_string = is_end
        elif node.character > word[0]: # TO LEFT
            if node.left is None:
                node.left = TernaryNode(word[0], is_end)
                word = word[1:]           
            if not is_end:
                self.__insert(node.left, word)
        elif node.character < word[0]: # TO RIGHT
            if node.right is None:
                node.right = TernaryNode(word[0], is_end)
                word = word[1:]
            
            if not is_end:
                self.__insert(node.right, word)
