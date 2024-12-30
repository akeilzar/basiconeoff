
# additive synth macro for audacity pipe into text file and serve

import math

# audacity sine waves

# values
v = [440 * i for i in [math.sin(x*(math.ceil((9*x**2)/8))) for x in range(10)]]

# type
t = "Sine"
# t = "Square"
# t = "Saw"
# t = "Triangle"

# frequencies
for f in v:
	if f > 0:
		print(f)
