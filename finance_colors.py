from sense_hat import SenseHat
from colorzero import Color
import os
import csv
import time

sense = SenseHat()
sense.clear()

class Transaction():
	def __init__(self, date, description, amount, balance):
		self.date = date
		self.description = description
		self.amount = float(amount)
		self.balance = balance

full_colors = []

cwd = os.getcwd()

months = os.listdir(os.path.join(cwd, "finances"))

# Sort in numerical order

months.sort()

for m in months:
	transactions = []

	with open(os.path.join(cwd, "finances", m)) as file:
		read_file = csv.reader(file, delimiter=",")
		count = 0
		for r in read_file:
			if count != 0 and r[5] and r[1] == "DEB":
				new_transaction = Transaction(r[0], r[4], r[5], r[7])
				transactions.append(new_transaction)
			count += 1

	colors = []

	white = Color("white").rgb_bytes
	red = Color("red").rgb_bytes
	orange = Color("orange").rgb_bytes
	blue = Color("blue").rgb_bytes
	green = Color("green").rgb_bytes
	indigo = Color("indigo").rgb_bytes

	for t in transactions:
		if t.amount < 5.00:
			colors.append([indigo[0], indigo[1], indigo[2]])
		elif t.amount < 10.00:
			colors.append([blue[0], blue[1], blue[2]])
		elif t.amount < 20.00:
			colors.append([green[0], green[1], green[2]])
		elif t.amount < 30.00:
			colors.append([orange[0], orange[1], orange[2]])
		elif t.amount > 100.00:
			colors.append([red[0], red[1], red[2]])
		else:
			colors.append([white[0], white[1], white[2]])

	fill_matrix = colors + [[0, 0, 0] for i in range(len(colors), 64)]

	print(fill_matrix)

	if len(fill_matrix) > 64:
		matrix1 = fill_matrix[0:64]
		matrix2 = fill_matrix[64:len(fill_matrix)] + [[0, 0, 0] for i in range(len(fill_matrix) - 64, 64)]

		full_colors.append([m + " #1", matrix1])
		full_colors.append([m + " #2", matrix2])
	else:
		full_colors.append([m, fill_matrix[0:64]])

for fc in full_colors:
	print("Showing {}".format(fc[0].replace(".csv", "")))

	sense.set_pixels(fc[1])
	time.sleep(3)
	sense.clear()
	time.sleep(2)

# Continue on
# Order by date
