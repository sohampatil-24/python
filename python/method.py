class MathOperation:
    def add(self, *args):
        result = 0
        for num in args:
            result += num
        print("Sum:", result)

obj = MathOperation()
obj.add()
obj.add(5)
obj.add(5, 10)
obj.add(5, 10, 15)

