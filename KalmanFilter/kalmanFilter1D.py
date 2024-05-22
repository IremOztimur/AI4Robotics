'''
The state is updated with the new measurement.
The state is then predicted based on the motion.
'''

def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motions = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

for measurement, motion in zip(measurements, motions):
	mu, sig = update(mu, sig, measurement, measurement_sig)
	mu, sig = predict(mu, sig, motion, motion_sig)

print("Final value of Mean is {}\nFinal value of Sigma is {}".format(mu, sig))
