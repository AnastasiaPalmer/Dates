import shelve

"""
Створіть клас героя для RPG-гри. У нього повинні бути характеристики (ім’я, HP, AC, STR, DEX і т.д.) 
та інвентар з предметами в ньому (можуть бути просто назви, або повноцінні 
об’єкти з описом (у вигляді екземплярів класів)). Найдайте йому методи save та load. Відповідно, 
перший буде сереалізувати його характеристики, а другий – десереалізувати
"""


class RPG_character:
    def __init__(self, name, HP, AC, STR=50, DEX=5):
        self.name = name
        self.HP = HP
        self.AC = AC
        self.STR = STR
        self.DEX = DEX

    def save(self):
        with shelve.open("char.db", "c") as char:
            char["HP"] = self.HP
            char['name'] = self.name

    def load(self):
        with shelve.open("char.db", "r") as char:
            for key in char.keys():
                print(key, char[key])
                if key == "HP":
                    self.HP = char[key]
                if key == "AC":
                    self.AC = char[key]
                if key == "name":
                    self.name = char[key]
                if key == "DEX":
                    self.DEX = char[key]

    def __repr__(self):
        return "Character [ name:{}, HP:{}, AC:{}, DEX:{} ]".format(self.name, self.HP, self.AC, self.DEX)


hero = RPG_character('Buba', 100, 200)
hero.save()

son = RPG_character('Beba', 200, 300)
print(son)
son.load()
print(son)
