class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0: return None
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0


class Solution:
    _lookup = {
        ']': '[',
        '}': '{',
        ')': '('
    }


    def isValid(self, s: str) -> bool:
        if len(s) in [0,1]: return False
        self.stack = Stack()
        for each in s:
            if each in self._lookup:
                # pop and verify
                if self._lookup[each] != self.stack.pop():
                    return False
            else:
                self.stack.push(each)
        if not self.stack.is_empty():
            return False
        return True