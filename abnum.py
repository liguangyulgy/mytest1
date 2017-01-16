class AbNum:
    def __init__(self, state):
        self.a, self.right = state.split('==', 2)
        self.left = self.a.split('+')
        self.right = self.right.strip()
        self.left = [a.strip() for a in self.left]
        if len(self.left) < 1 or len(self.right) < 1:
            raise Exception

    def show(self):
        print('left', self.left, 'right', self.right)

    def check(self, left, right):
        sum = 0
        for n in left:
            sum += int(n)
        if sum == int(right):
            return True
        else:
            return False
