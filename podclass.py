class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.fed = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False

class Mammal(Animal):
    def eat(self, food: Plant):
        if isinstance(food, Fruit):
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")

class Predator(Animal):
    def eat(self, food: Plant):
        if isinstance(food, Flower):
            print(f"{self.name} не стал есть {food.name}")
        else:
            print(f"{self.name} съел {food.name}")
        self.alive = False

class Flower(Plant):
    pass

class Fruit(Plant):
    self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Что произошло: Хищник попытался съесть цветок и погиб,
# млекопитающее съело фрукт и насытилось.
