class Pokemon:
    def __init__(self, name, primary_type, max_hp)->None:
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp     = max_hp

    def __str__(self) -> str:
        return f"{self.name} ({self.primary_type}): {self.hp}/{self.max_hp}"

    def feed(self):
        if self.hp < self.max_hp:
            self.hp += 1
            print(f'{self.name} has now {self.hp} health.')
        else:
            print(f"{self.name}'s health is full")

    def battle(self, other):
        print(f"Battle: {self.name}, {other.name}")
        resBat = self.typewheel(self.primary_type, other.primary_type)
        print(f'Result of battle: {self.name} get\'s a {resBat}')

        if resBat == 'loss':
            self.hp -= 5
        if resBat == 'win':
            other.hp -= 10

    @staticmethod
    def typewheel(type1, type2):
        result = {0:"loss", 1:"win",-1:"tie"}
        game_map = {"water": 0, "fire":1, "grass":2}

        wl_matrix = [
            [-1, 1, 0],   # water
            [0, -1, 1],   # fire
            [1, 0, -1]    # grass
        ]
        res = result[wl_matrix[game_map[type1]][game_map[type2]]]
        return res


if __name__=="__main__":
    pass