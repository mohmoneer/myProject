
from ursina import *
from random import randint

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = 'cube'
        self.color = color.black
        self.scale = 0.05
        self.position = (0, 0, -0.03)
        self.collider = 'box'
        self.dx = 0
        self.dy = 0
        self.eaten = 0

    def update(self):
        global body, text
        self.x += time.dt * self.dx
        self.y += time.dt * self.dy

        # Collision with apple

        if self.intersects(apple):
            Audio('apple_bite.wav')
            self.eaten += 1
            text.y = -1
            text = Text(text=f"Apple Eaten: {self.eaten}", position=(0, 0.3), origin=(0, 0),
                        scale=1.5, color=color.yellow, background=True)

            apple.x = randint(-4, 4) * 0.1
            apple.y = randint(-4, 4) * 0.1

            new_body = Entity(parent=field, model='cube', z=-0.029, color=color.green, scale=0.05)

            body.append(new_body)

        # Move the end segments first in range
        for i in range(len(body) - 1, 0, -1):
            body[i].position = body[i - 1].position

        # First segment
        if len(body) > 0:
            body[0].x = self.x
            body[0].y = self.y

        # Boundary checking
        if abs(self.x) > 0.47 or abs(self.y) > 0.47:
            Audio('whistle.wav')
            for segment in body:
                segment.position = (10, 10)
            body = []
            self.eaten = 0
            print_on_screen("You crashed!", position=(0, 0), origin=(0, 0), scale=2, duration=2)

            self.position = (0, 0)
            self.dx = 0
            self.dy = 0

    def input(self, key):
        if key == "right arrow":
            self.dx = 0.3
            self.dy = 0
        if key == "left arrow":
            self.dx = -0.3
            self.dy = 0
        if key == "up arrow":
            self.dx = 0
            self.dy = 0.3
        if key == "down arrow":
            self.dx = 0
            self.dy = -0.3

class Player2(Entity):
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = 'cube'
        self.color = color.white
        self.scale = 0.05
        self.position = (0, 0, -0.03)
        self.collider = 'box'
        self.dx = 0
        self.dy = 0
        self.eaten = 0

    def update(self):
        global body, text
        self.x += time.dt * self.dx
        self.y += time.dt * self.dy

        # Collision with apple
        hit_info = self.intersects(apple)
        if hit_info.hit:
            Audio('apple_bite.wav')
            self.eaten += 1
            text.y = -1
            text = Text(text=f"Apple Eaten: {self.eaten}", position=(0, 0.3), origin=(0, 0),
                        scale=1.5, color=color.yellow, background=True)

            apple.x = randint(-4, 4) * 0.1
            apple.y = randint(-4, 4) * 0.1

            new_body = Entity(parent=field, model='cube', z=-0.029, color=color.green, scale=0.05)

            body.append(new_body)

        # Move the end segments first in range
        for i in range(len(body) - 1, 0, -1):
            body[i].position = body[i - 1].position

        # First segment
        if len(body) > 0:
            body[0].x = self.x

            body[0].y = self.y

        # Boundary checking
        if abs(self.x) > 0.47 or abs(self.y) > 0.47:
            Audio('whistle.wav')
            for segment in body:
                segment.position = (10, 10)
            body = []
            self.eaten = 0
            print_on_screen("You crashed!", position=(0, 0), origin=(0, 0), scale=2, duration=2)

            self.position = (0, 0)
            self.dx = 0
            self.dy = 0

    def input(self, key):
        if key == "d":
            self.dx = 0.3
            self.dy = 0
        if key == "a":
            self.dx = -0.3
            self.dy = 0
        if key == "w":
            self.dx = 0
            self.dy = 0.3
        if key == "s":
            self.dx = 0
            self.dy = -0.3

app = Ursina()

field = Entity(model='quad', scale=(10, 10), texture='grass', collider='box')
player = Player()
player2 = Player2()
apple = Entity(parent=field, model='sphere', color=color.red, scale=0.05, position=(0.2, -0.2, -0.03))
body = []
text = Text(text="Apple Eaten: 0", position=(0, 0.3), origin=(0, 0), scale=1.5, color=color.yellow, background=True)

def update():
    player.update()
    player2.update()

def input(key):
    player.input(key)
    player2.input(key)

app.run()

