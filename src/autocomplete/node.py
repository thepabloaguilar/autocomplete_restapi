class TernaryNode:

    left = None
    equal = None
    right = None
    is_end_of_string = False

    def __init__(self, character, is_end_of_string=False):
        self.character = character
        self.is_end_of_string = is_end_of_string
    
    def has_child(self):
        return bool(self.left or self.equal or self.right)

    def __str__(self):
        return self.character
    
    def __repr__(self):
        return f'<Character: "{self.character}" EOS: "{self.is_end_of_string}">'
