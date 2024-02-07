from turtle import Turtle
import random
COLORS = ["red", "orange", "blue", "yellow", "green", "purple"]
INITIAL_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
UPPER_RANGE = 5
class Vehicles(Turtle):
    def __init__(self):
        super().__init__()
        self.all_vehicles = []
        self.vehicle_speed = INITIAL_MOVE_DISTANCE
        self.upper_range = UPPER_RANGE

    def create_vehicle(self):
        random_number = random.randint(0, self.upper_range)
        if random_number==0:
            self.hideturtle()
            new_vehicle = Vehicles()
            new_vehicle.penup()
            new_vehicle.shape("square")
            new_vehicle.shapesize(stretch_wid=1, stretch_len=2)
            new_vehicle.color(random.choice(COLORS))
            new_vehicle.goto(300, random.randint(-230, 230))
            self.all_vehicles.append(new_vehicle)
            
            
    def move_vehicles(self):
        for vehicle in self.all_vehicles:
            vehicle.setheading(180)
            vehicle.forward(self.vehicle_speed)
    def increase_vehicle_speed(self):
        self.vehicle_speed += MOVE_INCREMENT
        if self.upper_range > 1:
            self.upper_range -= 1
