# This Kalman Filter is based on the implementation from Wouter Bulten. 
# https://github.com/wouterbulten/kalmanjs/blob/master/contrib/java/KalmanFilter.java

class KalmanFilter(object):

	def __init__(self, r, q, a=1, b=0, c=1): 
		self.R = r 
		self.Q = q
		
		self.A = a
		self.B = b
		self.C = c

		self.x = float('nan')
		self.cov = 0.0

	def __predict(self, u = 0):
		return (self.A * float(self.x)) + (self.B * u)

	def __uncertainty(self):
		return ((self.A * float(self.cov)) * self.A) + self.R

	def __isNaN(self, num):
		return num != num

	def filter(self, measurement, u=0):
		if (self.__isNaN(self.x)):
			self.x = (1 / self.C) * measurement
			self.cov = (1 / self.C) * self.Q * (1 / self.C)
		else:
			# prediction & uncertainty
			predX = self.__predict(u)
			predCov = self.__uncertainty()

			# Kalman gain
			k_gain = predCov * self.C * (1 / ((self.C * predCov * self.C) + self.Q))

			# correction
			self.x = predX + k_gain * (measurement - (self.C * predX))
			self.cov = predCov - (k_gain * self.C * predCov)

		return self.x
