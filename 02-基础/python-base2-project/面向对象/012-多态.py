"""
多态
"""


class Animal:

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("汪汪汪")


class Cat(Animal):

    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)  # 与 dog.speak() 结果一致
make_noise(cat)  # 与 cat.speak() 结果一致


class AC:
    def cool_wind(self):
        # 制冷
        pass

    def hot_wind(self):
        # 制热
        pass

    def swing_l_r(self):
        # 左右摆风
        pass


class Meidi_AC(AC):
    def cool_wind(self):
        # 制冷
        print("media空调制冷")

    def hot_wind(self):
        # 制热
        print("美的空调制热")

    def swing_l_r(self):
        # 左右摆风
        print("美的空调左右摆风")


class Haier_AC(AC):
    def cool_wind(self):
        # 制冷
        print("海尔空调制冷")

    def hot_wind(self):
        # 制热
        print("海尔空调制热")

    def swing_l_r(self):
        # 左右摆风
        print("海尔空调左右摆风")


def make_cool(brand: AC):
    brand.cool_wind()


haier_ac = Haier_AC()
meidi_ac = Meidi_AC()
make_cool(haier_ac)
make_cool((meidi_ac))






