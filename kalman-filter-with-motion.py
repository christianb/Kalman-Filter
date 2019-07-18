import random
import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter(object):

	def __init__(self, r, q, b = 0): 
		self.R = r 
		self.Q = q
		self.x = 0.0
		self.A = 1
		self.B = b # Control vector
		self.C = 1
		self.cov = 0.0

	# predicts the next value
	# u - control
	def predict(self, u = 0):
		return (self.A * float(self.x)) + (self.B * u)

	def uncertainty(self):
		return ((self.A * float(self.cov)) * self.A) + self.R

	# filter
	def filter(self, measurement, u=0):
		if (self.x == 0.0):
			# print("x == 0.0")
			self.x = (1 / self.C) * measurement
			# print("x = ", self.x)
			self.cov = (1 / self.C) * self.Q * (1 / self.C)
			# print("cov = ", self.cov)
		else:
			predX = self.predict(u)
			# print("predX = ", predX)

			predCov = self.uncertainty()
			# print("predCov = ", predCov, (" uncertainty"))

			# Kalman Gain
			k_gain = predCov * self.C * (1 / ((self.C * predCov * self.C) + self.Q))
			# k_gain = 2.0 / 3.0
			# print("k_gain = ", k_gain)

			# Correction
			self.x = predX + k_gain * (measurement - (self.C * predX))
			# print("corrected x = ", self.x)
			self.cov = predCov - (k_gain * self.C * predCov)
			# print("corrected cov = ", self.cov)

		# print ("filter result = ", self.x)
		return self.x

# returns a gausian measurments around rssi value
def measurments(rssi, x_axis):
	sigma = 3

	g = []
	for x in x_axis:
		rnd_gaus = random.gauss(rssi,sigma)
		g.append(rnd_gaus)

	return np.asarray(g)
 
def plot(x_axis, values, filtered, filtered_with_motion):
	plt.figure()
	plt.plot(x_axis, values, 'bo', label='RSSI')
	plt.plot(x_axis, filtered, 'r', label='kalman')
	plt.plot(x_axis, filtered_with_motion, 'g', 'kalman with motion')
	plt.legend()
	plt.show()	

# two motionn, up, down, up
def move_array(x_axis):
	l = [0,0,0,1,1,1,2,2,1,1,     
1,0,0,0,0,0,0,0,0,0,
0,0,0,-1,-1,-1,-2,-2,-1,-1,
-1,0,0,0,0,0,0,0,0,0,
0,0,1,1,1,2,3,2,1,1,     
1,0,0,0,0,0,0,0,0,0,
0,0,-1,-1,-1,-2,-3,-2,-1,-1,
-1,0,0,0,0,0,0,0,0,0,
]

	print("size move_array", len(l))

	return np.asarray(l)

def main():
	# R models the process noise and describes how noisy our system internally is. Or, in other words, how much noise can we expect from the system itself? As our system is constant we can set this to a (very) low value.
	R = 0.01#

	# R models the process noise and describes how noisy our system internally is. Or, in other words, how much noise can we expect from the system itself? As our system is constant we can set this to a (very) low value.
	Q = 3

	# In real life scenario’s you usually make an estimate of R and Q based on measurements or domain knowledge. For this example we assume we know the noise levels.
	
	B = 0.5

	kalman_with_motion = KalmanFilter(R, Q, B)
	kalman_plain = KalmanFilter(R,Q,0)

	# define a range of x values
	x_axis = np.arange(0, 40, 0.5)
	# print("x_axis.ndim: ", x_axis.ndim)
	# print("x_axis.shape: ", x_axis.shape)
	
	RSSI = -73
	measurements = measurments(RSSI, x_axis)
	# print("size measurements: ", len(measurements))

	moveing = move_array(x_axis)
	# print("size moveing: ", len(moveing))

	filtered_with_motion = []
	filtered = []
	print("size x_axis: ", len(x_axis))
	for n in range(len(x_axis)):
		print("n: ",n)
		# print("moveing[",n,"]: ", moveing[n])
		# print("measurements[",n,"]: ", measurements[n])
		result_motion = kalman_with_motion.filter(measurements[n], moveing[n])
		# print(result_motion)
		filtered_with_motion.append(result_motion)

		result = kalman_plain.filter(measurements[n], moveing[n])
		# print(result)
		filtered.append(result)

	plot(x_axis, measurements, filtered, filtered_with_motion)
	


if __name__ == '__main__':
	main()
