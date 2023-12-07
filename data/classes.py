class Class:
    def __init__(self, strength: int, defense: int, stealth: int, agility: int, charisma: int, intelligence: int, luck: int, hp: int):
        self.base_strength = strength
        self.base_defense = defense
        self.base_stealth = stealth
        self.base_agility = agility
        self.base_charisma = charisma
        self.base_int = intelligence
        self.base_luck = luck
        self.base_hp = hp

class Fighter(Class):
    def __init__(self):
        super().__init__(
            7,
            5,
            3,
            4,
            4,
            3,
            4,
            25
        )

class Ranger(Class):
    def __init__(self):
        super().__init__(
            4,
            4,
            5,
            6,
            3,
            4,
            4,
            20
        )

class Thief(Class):
    def __init__(self):
        super().__init__(
            4,
            3,
            6,
            6,
            3,
            5,
            3,
            18
        )

class Guardian(Class):
    def __init__(self):
        super().__init__(
            3,
            12,
            1,
            1,
            4,
            4,
            5,
            40
        )

class Bard(Class):
    def __init__(self):
        super().__init__(
            2,
            3,
            2,
            4,
            10,
            3,
            5,
            15
        )

class Wizard(Class):
    def __init__(self):
        super().__init__(
            3,
            3,
            3,
            5,
            2,
            8,
            6,
            30
        )

class Hero(Class):
    def __init__(self):
        super().__init__(
            5,
            5,
            3,
            3,
            5,
            5,
            4,
            25
        )