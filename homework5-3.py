class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    #def __str__(self):
    #    return (self.name, self.number_of_floors)

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors and self.name == other.name

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        return self.__add__(value)

    def __radd__(self, value):
        return self.__add__(value)

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
h3 = House('ЖК Платан', 20)
print(str(f'Название: {h1.name}, кол-во этажей: {h1.number_of_floors}'))
print(str(f'Название: {h2.name}, кол-во этажей: {h2.number_of_floors}'))
print(h1 == h2)
h3 = h1 + 10
print(h3) # С этого момента какие-то результаты получаются, но что это значит?
print(h1 == h3)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)

print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)
