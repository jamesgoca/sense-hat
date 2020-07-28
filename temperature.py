from sense_hat import SenseHat
import time

sense = SenseHat()

temperatures = []

temp = sense.get_temperature()
pressure = sense.get_pressure()
humidify = sense.get_humidity()

for i in range(0, 64):
	temp = sense.get_temperature()
	if temp < 30:
		temperatures.append((255, 0, 255))
	elif temp < 40:
		temperatures.append((255, 0, 0))
	elif temp < 50:
		temperatures.append((111, 111, 111))
	else:
		temperatures.append((0, 255, 0))
	time.sleep(1)

temperatures = [i for i in temperatures] + [(0, 0, 0) for i in range(len(temperatures), 64)]

print(temperatures)

sense.set_pixels(temperatures)