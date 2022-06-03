import numpy as np
from math import *
#import matplotlib.pyplot as plt

COXA, FEMUR, TIBIA = 3.8, 9.3, 10.9

COXA_ANGLES_OFFSET = {
	1: -180,
	2: 40,	
	3: 0,
	4: 0,
	5: 140,
	6: -180,
}

FEMUR_ANGLES_OFFSET = {
	1: 0,
	2: 0,
	3: 0,
	4: -180,
	5: -180,
	6: -180,
}

TIBIA_ANGLES_OFFSET = {
	1: -40,
	2: -40,
	3: -40,
	4: -220,
	5: -220,
	6: -220,
}

def ik(x, y, z, leg_num):

	if leg_num == 2 or leg_num == 5:
		x -= 0
		y -= 8.5

	else:
		x -= 7.5
		y -= 5.5

	#coxa's joint angle
	theta = abs(degrees(atan2(x, y)) + COXA_ANGLES_OFFSET[leg_num]) 

	#leg length from top view
	r = sqrt(x**2 + y**2)
	beta1 = degrees(atan2((r-COXA), z))

	#projectile between femur servo and end of the leg 
	t = sqrt(z**2 + (r-COXA)**2)

	#by applying law of cosines
	beta2 = degrees(acos((t**2 + FEMUR**2 - TIBIA**2) / (2*t*FEMUR)))

	beta = abs(180 - (beta1 + beta2) + FEMUR_ANGLES_OFFSET[leg_num])

	alpha = abs(degrees(acos((TIBIA**2 + FEMUR**2 - t**2) / (2*TIBIA*FEMUR))) + TIBIA_ANGLES_OFFSET[leg_num])

	return (round(theta), round(beta), round(alpha))


def Z_Translation(x, y, z, leg_num):
	
	if leg_num == 2 or leg_num == 5:
		x -= 0
		y -= 8.5

	else:
		x -= 7.5
		y -= 5.5

	leg_length = sqrt(x**2 + y**2)

	t = sqrt(z**2 + (leg_length-COXA)**2)

	beta1 = degrees(atan2((leg_length-COXA), z))

	#by applying law of cosines
	beta2 = degrees(acos((t**2 + FEMUR**2 - TIBIA**2) / (2*t*FEMUR)))

	beta = abs(180 - (beta1 + beta2) + FEMUR_ANGLES_OFFSET[leg_num])

	alpha = abs(degrees(acos((TIBIA**2 + FEMUR**2 - t**2) / (2*TIBIA*FEMUR))) + TIBIA_ANGLES_OFFSET[leg_num])

	return (round(beta), round(alpha))


def Z_rotation(x, y, z, angle):
	angle = radians(angle)
	A = np.array([[cos(angle), -sin(angle), 0],
				 [sin(angle), cos(angle), 0],
				 [0, 0, 1]])

	B = np.array([x, y, z])

	C = A.dot(B)

	return ceil(C[0]), ceil(C[1]), ceil(C[2])


def X_rotation(x, y, z, angle):
	angle = radians(angle)
	A = np.array([[1, 0, 0],
				 [0, cos(angle), -sin(angle)],
				 [0, sin(angle), cos(angle)]])

	B = np.array([x, y, z])

	C = A.dot(B)

	return ceil(C[0]), ceil(C[1]), ceil(C[2])


def Y_rotation(x, y, z, angle):
	angle = radians(angle)
	A = np.array([[cos(angle), 0, sin(angle)],
				 [0, 1, 0],
				 [-sin(angle), 0, cos(angle)]])

	B = np.array([x, y, z])

	C = A.dot(B)

	return ceil(C[0]), ceil(C[1]), ceil(C[2])


#xpoints = np.array([20, 0, 20, 20, 0, 20])
#ypoints = np.array([15, 24, 15, 15, 24, 15])
#
#for x, y, z in zip(xpoints, ypoints, range(len(xpoints))):
#	angle1, angle2, angle3 = ik(x, y, 10, 3)
#	matrix1 = np.array([[cos(angle1), 0, sin(angle1), 0],
#					[sin(angle1), 0, -cos(angle1), COXA],
#					[0, 1, 0, 0],
#					[0, 0, 0, 1]])
#
#	matrix2 = np.array([[cos(angle2), -sin(angle2), 0, FEMUR*cos(angle2)],
#						[sin(angle2), cos(angle2), 0, -FEMUR*sin(angle2)],
#						[0, 0, 1, 0],
#						[0, 0, 0, 1]])
#
#
#	matrix3 = np.array([[cos(angle3), -sin(angle3), 0, TIBIA*cos(angle3)],
#						[sin(angle3), cos(angle3), 0, -TIBIA*sin(angle3)],
#						[0, 0, 1, 0],
#						[0, 0, 0, 1]])
#	matrix4 = np.dot(matrix1, matrix2)
#	result = np.dot(matrix4, matrix3)
#	plt.xlim(-30 , 30)
#	plt.ylim(-30 , 30)
#	plt.scatter(xpoints[z], ypoints[z], marker = 'o')
#	plt.scatter(result[0][-1]+15, result[1][-1]+10, marker = 'o')
#	plt.xlabel("x-axis")
#	plt.ylabel("y-axis")
#	plt.show()

if __name__ == "__main__":
	print(__name__)