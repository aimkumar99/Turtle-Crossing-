from turtle import Screen
import time
from scoreboard import Scoreboard
from vehicles import Vehicles
from player import Player
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.tracer(0)

player = Player()
vehicles = Vehicles()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")


game_on = True
while game_on:    
    time.sleep(0.1)
    screen.update()
    vehicles.create_vehicle()
    vehicles.move_vehicles()
    #detect collision with the vehicle
    for vehicle in vehicles.all_vehicles:
        if player.distance(vehicle) < 20:
            game_on = False
            scoreboard.game_over()
    #detect if the player crossed finish line
    if player.reached_finish_line():
        player.goto_start_position()
        vehicles.increase_vehicle_speed()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()



screen.exitonclick()