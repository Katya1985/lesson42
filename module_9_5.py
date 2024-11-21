class StepValueError(ValueError):
    pass
class Iterator():
    # start - целое число, с которого начинается итерация.
    # stop - целое число, на котором заканчивается итерация.
    # step - шаг, с которым совершается итерация.
    # pointer - указывает на текущее число в итерации (изначально start)
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
    # __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
    def __iter__(self):
        self.pointer = self.start
        return self
    # __next__ - метод, увеличивающий атрибут pointer на step
    def __next__(self):

        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current = self.pointer
        self.pointer += self.step
        return current

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()



