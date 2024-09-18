class House :
    def __init__(self, name , number_of_floors):
        self.name = name
        self.namber_of_floors = number_of_floors
    def __len__(self):
        return self.namber_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.namber_of_floors}"
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
class House :
        def __add__(self, namber_of_floors):
            sefl.namber_of_floors += 1
            return self
        def __eq__(self, other):
            self = other
            return True

        def __lt__(self, other):
            self < other
            return True

        def __le__(self, other):
            self <= other
            return True

        def __gt__(self, other):
            self > other
            return True

        def __ge__(self, other):
            self >= other
            return True

        def __ne__(self, other):
            self != other
            return True

    # def __int__(self, value):
    #     def __add__(self, value):
    #         sefl.value += 1
    #         return self
print(h1 == h2) # __eq__
h1 = 10 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + 20 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__