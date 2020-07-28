from sense_hat import SenseHat
import os
import random
import time
import json

sense = SenseHat()

sense.clear()

def get_scores():
	if os.path.exists("scores.json"):
		with open("scores.json") as file:
			data = json.load(file)
			print(data)
			print("Most recent score:")
			print(data[-1]["name"] + ": " + data[-1]["points"])
	else:
		print("You have no recorded scores.")

def save_game_data(points, scores):
	name = input("What is your name?")

	data = {
		"name": name,
		"points": points
	}

	if os.path.exists("scores.json"):
		mode = 'a'
	else:
		mode = 'w'

	scores.append(data)

	with open("scores.json", mode) as file:
		json.dump(scores, file)

def change_position(position, direction):
	sense.set_pixel(position[0], position[1], 0, 0, 0)

	if direction == "down":
		new_position = [position[0], position[1] + 1]
	elif direction == "up":
		new_position = [position[0], position[1] - 1]
	elif direction == "left":
		new_position = [position[0] - 1, position[1]]
	else:
		new_position = [position[0] + 1, position[1]]

	if new_position[0] > 7:
		new_position = [0, new_position[1]]
	elif new_position[1] > 7:
		new_position = [new_position[0], 1]

	sense.set_pixel(new_position[0], new_position[1], 255, 255, 255)

	return new_position

def set_food(position):
	first = [i for i in range(0, position[0])] + [i for i in range(position[0] + 1, 7)]
	second = [i for i in range(0, position[1])] + [i for i in range(position[1] + 1, 7)]

	food = [random.choice(first), random.choice(second)]

	random_number = random.randint(0, 3)

	if random_number == 2:
		sense.set_pixel(food[0], food[1], 160, 32, 240)
		is_bonus = True
	else:
		sense.set_pixel(food[0], food[1], 255, 165, 0)
		is_bonus = False

	return food, is_bonus

def check_food(position, food, points, is_bonus):
	if position[0] == food[0] and position[1] == food[1]:
		if is_bonus == True:
			points = points + 10
		else:
			points = points + 1

		if points == 1:
			print("You now have {} point!".format(points))
		else:
			print("You now have {} points!".format(points))

		food, is_bonus = set_food(position)

	return points, food, is_bonus

position = [4, 4]

points = 0

start_time = time.time()

playing = True
warning = False
is_bonus = False

print("Welcome to Pixel Eater!")
scores = get_scores()

sense.show_letter("3")
time.sleep(1)
sense.show_letter("2")
time.sleep(1)
sense.show_letter("1")
time.sleep(1)

sense.clear()

sense.set_pixel(position[0], position[1], 255, 255, 255)

food = set_food(position)

while time.time() < start_time + 60:
	if round(time.time(), 0) == round(start_time + 50, 0) and warning == False:
		print("You have 10 seconds left!")
		warning = True

	for event in sense.stick.get_events():
		direction = event.direction
		action = event.action
		if action == "pressed" and direction == "middle":
			sense.clear()
			print("You scored {} points.".format(points))
			print("Thanks for playing!")
		elif action == "pressed":
			position = change_position(position, direction)
			points, food, is_bonus = check_food(position, food, points, is_bonus)

sense.clear()
sense.show_message("Game Over!")

save_game_data(points. scores)
sense.clear()
