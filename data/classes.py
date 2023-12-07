class Class:
    def __init__(self, strength: int, defense: int, stealth: int, agi: int, cha: int, intelligence: int, luck: int, hp: int):
        self.base_strength = strength
        self.base_defense = defense
        self.base_stealth = stealth
        self.base_agi = agi
        self.base_cha = cha
        self.base_intel = intelligence
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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)
    
    async def get(self, stat):
        return getattr(self, stat)

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
        self.strength: int
        self.defense: int
        self.stealth: int
        self.agi: int
        self.cha: int
        self.intel: int
        self.luck: int
        self.hp: int

    async def create(self, stat: str, rolled: int):
        setattr(self, stat, rolled)
        return getattr(self, stat)

    async def get(self, stat):
        return getattr(self, stat)