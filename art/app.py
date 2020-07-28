from sense_hat import SenseHat
import json, time
from PIL import Image

# Configure Sense HAT and load images

sense = SenseHat()

sense.clear()

with open("art.json", "r") as color_file:
	colors = json.load(color_file)

# Set initial pixel values

viewing = 0
sense.set_pixels(colors[0]["matrix"][0:64])

playing = True

print("""
Welcome to the James Pixel Art Gallery!

Press the left and right buttons on the Sense HAT joystick to view the gallery.

Press the middle button to save an image.

Press the up or down button to exit.
""")

def save_file(color):
	filename = str(color["name"]) + ".png"

	image = Image.new('RGB', (8, 8))
	convert_to_tuple = [tuple(item) for item in color["matrix"][0:64]]
	image.putdata(convert_to_tuple)

	image.save(filename)
	image.show()

	print("Image saved to {}.".format(filename))

# Scroll through gallery

while playing == True:
	for event in sense.stick.get_events():
		if event.direction == "right" and event.action == "pressed":
			# Check if there is another item in the list. If not, reset counter.
			if (viewing + 1) < len(colors):
				sense.clear()

				sense.set_pixels(colors[viewing + 1]["matrix"][0:64])
				viewing += 1
			else:
				viewing = 0
				sense.set_pixels(colors[viewing]["matrix"][0:64])
			print("Now viewing {}".format(colors[viewing]["name"]))

		elif event.direction == "left" and event.action == "pressed":
			if (viewing - 1) == -1:
				sense.clear()

				viewing = len(colors) - 1

				sense.set_pixels(colors[viewing]["matrix"][0:64])
			else:
				sense.set_pixels(colors[viewing - 1]["matrix"][0:64])
				viewing -= 1
			print("Now viewing {}".format(colors[viewing]["name"]))

		elif event.direction == "middle" and event.action == "pressed":
			save_file(colors[viewing])

		elif (event.direction == "up" and event.action == "pressed") or (event.direction == "down" and event.action == "pressed"):
			print("Thanks for viewing the gallery!")
			sense.clear()
			playing = False
