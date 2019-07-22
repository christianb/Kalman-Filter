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

def plot(raw, average, kalman, filename, title, out):
	x_axis = np.arange(0, len(raw), 1)
	
	plt.title(title)
	plt.ylabel("RSSI in dB")
	plt.plot(x_axis, raw, 'bo', label='rssi')
	plt.plot(x_axis, average, 'g', label='average')
	plt.plot(x_axis, kalman, 'r', label='kalman')
	plt.legend()
	plt.savefig(filename)

def plot_test():
	x_axis = np.arange(1, 11, 1)
	values = [1,np.nan,1,np.nan,1,1,1,1,1,1]

	plt.plot(x_axis, values, 'bo')
	plt.show()

def plot_test2(filename):
	data = np.loadtxt(filename, unpack = False, delimiter=',')
	rssi = data[0]
	average = data[1]
	kalman = data[2]

	x_axis = np.arange(0, len(rssi), 1)

	plt.plot(x_axis, rssi, 'bo')
	plt.plot(x_axis, average, 'g', label='average')
	plt.plot(x_axis, kalman, 'r', label='kalman')
	plt.show()

def plot_test3(filename, path, out_path):
	data = np.loadtxt(path+filename, unpack = False, delimiter=',')
	timestamp = data[0]
	rssi = data[1]
	average = data[2]
	kalman = data[3]
	# accumulated = data[4]

	# size = len(timestamp)
	# print("size: ", size)
	
	# start = timestamp[0]
	# last = timestamp[size-1]

	# durationInMs = (last - start)

	# Get current size
	fig_size = plt.rcParams["figure.figsize"]
 
	# Prints: [8.0, 6.0]
	# print("Current size:", fig_size)

	# Set figure width to 12 and height to 9
	fig_size[0] = 15
	fig_size[1] = 6
	plt.rcParams["figure.figsize"] = fig_size

	plt.figure()
	plt.plot(timestamp, rssi, 'bo', label='RSSI')
	plt.plot(timestamp, average, 'g', label='average')
	plt.plot(timestamp, kalman, 'r', label='kalman')
	# plt.plot(timestamp, accumulated, 'orange', label='accumulated')
	plt.legend()
	# plt.show()
	out_name = filename+".png"
	plt.savefig(out_path+out_name)
