'''
    We do not need it in Python, but...
'''

class Stack:
    def __init__(self):
        self._data = []
        self._top = 0

    def __len__(self):
        return self._top

    def __repr__(self):
        return f"<Stack: [{', '.join([str(i) for i in self._data[:self._top]])}]>"

    def push(self, item):
        self._top += 1
        self._data += [item]

    def pop(self):
        if self._top == 0: raise Exception('Stack has 0 elements')

        self._top -= 1
        last_item = self._data[-1]
        self._data  = self._data[:-1]

        return last_item




# # test
stack = Stack()

print("1)", stack)
assert len(stack) == 0

stack.push(89)
stack.push(False)
stack.push("I am in stack :)")
stack.push(120)

assert len(stack) == 4
print("2)", stack)


stack.pop()
stack.pop()

assert len(stack) == 2
print("3)", stack)

