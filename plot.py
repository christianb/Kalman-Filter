import numpy as np
import matplotlib.pyplot as plt

def plot_csv(filename):	
	data = np.loadtxt("csv/"+filename+".csv", unpack = False, delimiter=',')

	rssi = data[0]
	average = data[1]
	kalman = data[2]
	
	x_axis = np.arange(0, len(rssi), 1)

	plt.figure()
	plt.ylabel("RSSI in dB")
	plt.plot(x_axis, rssi, 'bo', label='raw')
	plt.plot(x_axis, average, 'g', label='average')
	plt.plot(x_axis, kalman, 'r', label='kalman')
	plt.legend()
	out_name = filename+".png"
	plt.savefig("plots/"+out_name)
	# plt.show()

def plot(raw, average, kalman, filename, title):
	x_axis = np.arange(0, len(raw), 1)
	
	plt.title(title)
	plt.ylabel("RSSI in dB")
	plt.plot(x_axis, raw, 'bo', label='rssi')
	plt.plot(x_axis, average, 'g', label='average')
	plt.plot(x_axis, kalman, 'r', label='kalman')
	plt.legend()
	plt.savefig(filename)
