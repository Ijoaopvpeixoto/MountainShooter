from Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, positio0n: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

