class Reverse:
    def __init__(self, s=""):
        if not s:
            s = input("Enter a string to reverse: ")
        self.s = s

    def get_reversed(self):
        return self.s[::-1]

rev_obj = Reverse()
print("Reversed string:", rev_obj.get_reversed())