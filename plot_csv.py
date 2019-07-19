import numpy as np
import matplotlib.pyplot as plt

# returns a gausian measurments around rssi value

def plot():

	data = np.loadtxt('rssi.csv', unpack = False, delimiter=',')
	print(data)
	
#plt.figure()
	#plt.plot(x_axis, rssi, 'bo', label='RSSI')
	#plt.plot(x_axis, average, 'g', label='average')
	#plt.plot(x_axis, kalman, 'r', label='kalman')
	#plt.legend()
	#plt.show()	


def main():
	plot()
	


if __name__ == '__main__':
	main()
