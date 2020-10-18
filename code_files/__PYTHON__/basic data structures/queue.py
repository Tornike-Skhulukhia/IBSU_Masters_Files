'''
    We do not need it in Python, but...
'''

class queue:
    def __init__(self):
        self._data = []
        self._top = 0
        self._bottom = 0

    def __len__(self):
        return self._top - self._bottom

    def __repr__(self):
        return f"<Queue: [{', '.join([str(i) for i in self._data[self._bottom:self._top]])}]>"

    def push(self, item):
        self._top += 1
        self._data += [item]

    def pop(self):
        if self._top == self._bottom: raise Exception('queue has 0 elements')

        first_item = self._data[self._bottom]
        self._bottom += 1

        return first_item



# # test
queue = queue()

print("1)", queue)
assert len(queue) == 0

queue.push(89)
queue.push(False)
queue.push("I am in queue :)")
queue.push(120)

assert len(queue) == 4
print("2)", queue)


queue.pop()
queue.pop()

assert len(queue) == 2
print("3)", queue)

