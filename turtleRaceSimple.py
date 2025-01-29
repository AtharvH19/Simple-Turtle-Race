import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_racer_count():
    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers

def setup_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racing')
    screen.bgcolor('lightblue')

def draw_track():
    track_drawer = turtle.Turtle()
    track_drawer.speed(0)
    track_drawer.penup()
    track_drawer.goto(-WIDTH//2 + 30, -HEIGHT//2 + 20)
    track_drawer.pendown()
    track_drawer.goto(-WIDTH//2 + 30, HEIGHT//2 - 20)
    track_drawer.penup()
    track_drawer.goto(WIDTH//2 - 30, -HEIGHT//2 + 20)
    track_drawer.pendown()
    track_drawer.goto(WIDTH//2 - 30, HEIGHT//2 - 20)
    track_drawer.hideturtle()

def create_turtles(colors):
    turtles = []
    spacing_y = HEIGHT // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.speed(3)
        racer.penup()
        racer.goto(-WIDTH//2 + 40, -HEIGHT//2 + (i + 1) * spacing_y)
        racer.pendown()
        turtles.append(racer)
    return turtles

def start_race(turtles):
    while True:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= WIDTH // 2 - 40:
                return racer.color()[0]

racers = get_racer_count()
setup_screen()
draw_track()
random.shuffle(COLORS)
race_colors = COLORS[:racers]
turtle_list = create_turtles(race_colors)
winner = start_race(turtle_list)

print(f"The winner is the {winner} turtle! 🏆🐢")
time.sleep(5)
