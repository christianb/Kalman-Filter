from plot import plot
from kalman_filter import KalmanFilter
import numpy as np

def main():
	rssi = np.loadtxt("rssi_2.csv", unpack = False, delimiter=',')

	# print(rssi)
	
	# R and Q affect the peaks of the kalman graph. 
  # Its the relationship between R and Q
	# The task is to find good R,Q values

	R = 0.05 # system noise
	Q = 3 # measurement noise

	A = 1
	B = 0
	C = 1

	kalman = KalmanFilter(R, Q, A, B, C)
	
	g = []
	for x in range(len(rssi)):
		g.append(kalman.filter(rssi[x]))
   
	k_filtered = np.asarray(g)

	title = "R: " + str(R) + ", Q: " + str(Q) + ", A: " + str(A) + ", B: " + str(B) + ", C: " + str(C)
	plot(rssi, k_filtered, "test_24.png", title)


if __name__ == '__main__':
	main()
