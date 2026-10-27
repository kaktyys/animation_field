import random


class StarModel:
    def __init__(self, width: int, height: int, max_depth: int):
        self.width = width
        self.height = height
        self.max_depth = max_depth
        self.x = 0
        self.y = 0
        self.z = 0
        self.color = ""
        self.reset(initial=True)

    def reset(self, initial: bool = False):
        self.x = random.randint(-self.width * 2, self.width * 2)
        self.y = random.randint(-self.height * 2, self.height * 2)
        self.z = random.randint(10, self.max_depth) if initial else self.max_depth

        colors = ["#FFFFFF", "#E0F7FA", "#B2EBF2", "#FFF9C4", "#FFECB3", "#FFCDD2"]
        self.color = random.choice(colors)

    def update(self, speed: int):
        self.z -= speed
        if self.z <= 0:
            self.reset(initial=False)
