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

def main():
	plot_csv('rssi_10:A2:EF:30:0C:03')
	plot_csv('rssi_30:1B:C8:DE:D1:75')
	plot_csv('rssi_5A:49:CD:F7:F0:CA')
	plot_csv('rssi_76:FD:71:07:9B:42')
	plot_csv('rssi_84:C0:EF:E0:55:B9')
	plot_csv('rssi_88:C6:26:AE:08:C7')
	plot_csv('rssi_88:C6:26:AE:08:C7')
	

if __name__ == '__main__':
	main()
