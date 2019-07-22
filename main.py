from plot import plot_test3
from kalman_filter import KalmanFilter
import numpy as np

from os import listdir
from os.path import isfile, join

def loadAndPlot(filename, path):
	rssi,average,kalman = np.loadtxt(path+filename, unpack = False, delimiter=',')
	title = "R: 0.01, Q: 3, A: 1, B: 0, C: 1"
	# plot(rssi, average,kalman, "./plots/xample/"+filename+".png", title)

def main():
	path='./csv/simulation/#8/'
	out_path = './plots/simulation/#8/'
	onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

	for f in onlyfiles:
		print(f, path)
		# loadAndPlot(f, path)
		plot_test3(f, path, out_path)

	# plot_test()                                          
	# plot_test3("csv/rssi_60_sec/rssi_38:F9:D3:9B:6E:1E.csv")
	
	# rssi = np.loadtxt("rssi_2.csv", unpack = False, delimiter=',')

	# print(rssi)
	
	# R and Q affect the peaks of the kalman graph. 
  # Its the relationship between R and Q
	# The task is to find good R,Q values

	R = 0.05 # system noise
	Q = 3 # measurement noise

	A = 1
	B = 0
	C = 1

	# kalman = KalmanFilter(R, Q, A, B, C)
	
	# g = []
	#for x in range(len(rssi)):
		#g.append(kalman.filter(rssi[x]))
   
	#k_filtered = np.asarray(g)

	#  title = "R: " + str(R) + ", Q: " + str(Q) + ", A: " + str(A) + ", B: " + str(B) + ", C: " + str(C)
	#plot(rssi, k_filtered, "test_24.png", title)


if __name__ == '__main__':
	main()
