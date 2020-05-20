class animals():
    weight = []
    country =[]


    def __init__(self, voice, name, weight):
        self.voice_type = voice
        self.animal_name = name
        self.animal_weight = weight
        animals.weight.append(weight)
        animals.country.append(self)

    def feed(self):
        self.eat = 'Покормить животное'

class birds(animals):

    def get_eggs(self):
        self.eggs = 'Собрать яйца'

class cattle(animals):
    def milk(self):
        self.milk = 'Подоить'

class sheep(animals):

    def cut(self):
        self.wool = 'Подстричь'

chicken1 = birds(voice='ko-ko', name='Кукареку', weight=2)
chicken2 = birds(voice='Кукареку', name='Кукареку', weight=3)
goos1 = birds(voice='Гагага', name='Серый', weight=4)
goos2 = birds(voice='Гагага1', name='Белый', weight=5)
cow = cattle(voice='Мууууу', name='Манька', weight=450)
sheep1 = sheep(voice='Беееее', name='Барашек', weight=130)
sheep2 = sheep(voice='Мееее', name='Кудрявая', weight=110)
goat1 = cattle(voice='Мееемеме', name='Рога', weight=99)
goat2 = cattle( voice='Беебебе', name='Копыта', weight=115)
duck = birds(voice='Кря-кря', name='Кряква', weight=3)


for animal in animals.weight:
    animal = max(animals.weight)

print(f'Самое тяжелое животное весит: {animal}')
print(f'Общий вес всех животных = {sum(animals.weight)}')
