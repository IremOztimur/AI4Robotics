import math

def pdf(stdev, x, mean):
	return (1.0 / (stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - mean) / stdev) ** 2)

print(pdf(2, 8, 10))
