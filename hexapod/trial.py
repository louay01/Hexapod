from adafruit_servokit import ServoKit
from angles import ik, Z_Translation, Z_rotation, X_rotation, Y_rotation
from gyroscopeTrial import read_word_2c, get_x_rotation, get_y_rotation
import time


kit1 = ServoKit(channels=16)
kit2 = ServoKit(channels=16, address=65)

X_POS = {
	1: 18,
	2: 0,
	3: 18,
	4: 18,
	5: 0,
	6: 18
}

Y_POS = {
	1: 15,
	2: 24,
	3: 15,
	4: 15,
	5: 24,
	6: 15
}

LEG_SERVOS_NUM = {
	1: [0, 1, 2],
	2: [3, 4, 5],
	3: [6, 7, 8],
	4: [0, 1, 2],
	5: [3, 4, 5],
	6: [6, 7, 8]
}

Z = 11

step_size = 5

rotation_angle = -20

delay = 0.4

def standard_stance(z):
	count = 0

	for leg in range(1, 7):
		theta, beta, alpha = ik(X_POS[leg], Y_POS[leg], z, leg)
		#print(theta, beta, alpha)
		if count >= 8:
			count = 0

		if leg <= 3:
			kit1.servo[count].angle = theta
			kit1.servo[count+1].angle = beta
			kit1.servo[count+2].angle = alpha
		else:
			kit2.servo[count].angle = theta
			kit2.servo[count+1].angle = beta
			kit2.servo[count+2].angle = alpha

		count += 3



def steps(kit, x, y, z, leg_num, swing=False, stance=False, left_rotate=False):
	theta, beta, alpha = ik(x, y, z, leg_num)
	print(leg_num, theta, beta, alpha)
	if leg_num == 2 and (swing or stance) and (left_rotate):
		theta -= 70
	elif leg_num == 5 and (swing or stance) and (left_rotate):
		theta -= 70
	kit.servo[LEG_SERVOS_NUM[leg_num][0]].angle = theta
	kit.servo[LEG_SERVOS_NUM[leg_num][1]].angle = beta
	kit.servo[LEG_SERVOS_NUM[leg_num][2]].angle = alpha

def swing1():
	steps(kit1, X_POS[1]+step_size, Y_POS[1], 0, 1)
	steps(kit1, X_POS[3]-step_size, Y_POS[3], 0, 3)
	steps(kit2, X_POS[5]+step_size, Y_POS[5], 0, 5)

def swing2():
	steps(kit2, X_POS[4]+step_size, Y_POS[4], 0, 4)
	steps(kit2, X_POS[6]-step_size, Y_POS[6], 0, 6)
	steps(kit1, X_POS[2]-step_size, Y_POS[2], 0, 2)
	steps(kit1, X_POS[1]+step_size, Y_POS[1], Z, 1)
	steps(kit1, X_POS[3]-step_size, Y_POS[3], Z, 3)
	steps(kit2, X_POS[5]+step_size, Y_POS[5], Z-1, 5)

def stance1():
	steps(kit1, X_POS[1]+step_size, Y_POS[1], Z, 1)
	steps(kit1, X_POS[3]-step_size, Y_POS[3], Z, 3)
	steps(kit2, X_POS[5]+step_size, Y_POS[5], Z-1, 5)	
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
 
def stance2():
	steps(kit2, X_POS[4]+step_size, Y_POS[4], Z, 4)
	steps(kit2, X_POS[6]-step_size, Y_POS[6], Z, 6)
	steps(kit1, X_POS[2]-step_size, Y_POS[2], Z, 2)	
	steps(kit1, X_POS[1], Y_POS[1], Z, 1)
	steps(kit1, X_POS[3], Y_POS[3], Z, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)


def return_back1():
	steps(kit1, X_POS[1], Y_POS[1], Z, 1)
	steps(kit1, X_POS[3], Y_POS[3], Z, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)	
	steps(kit2, X_POS[4]+step_size, Y_POS[4], 0, 4)
	steps(kit2, X_POS[6]-step_size, Y_POS[6], 0, 6)
	steps(kit1, X_POS[2]-step_size, Y_POS[2], 0, 2)	

def return_back2():
	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit1, X_POS[1]+step_size, Y_POS[1], 0, 1)
	steps(kit1, X_POS[3]-step_size, Y_POS[3], 0, 3)
	steps(kit2, X_POS[5]+step_size, Y_POS[5], 0, 5)

def swing3():
	steps(kit1, X_POS[1]-step_size, Y_POS[1], 0, 1)
	steps(kit1, X_POS[3]+step_size, Y_POS[3], 0, 3)
	steps(kit2, X_POS[5]-step_size, Y_POS[5], 0, 5)

def swing4():
	steps(kit2, X_POS[4]-step_size, Y_POS[4], 0, 4)
	steps(kit2, X_POS[6]+step_size, Y_POS[6], 0, 6)
	steps(kit1, X_POS[2]+step_size, Y_POS[2], 0, 2)
	steps(kit1, X_POS[1]-step_size, Y_POS[1], Z, 1)
	steps(kit1, X_POS[3]+step_size, Y_POS[3], Z, 3)
	steps(kit2, X_POS[5]-step_size, Y_POS[5], Z, 5)


def stance3():
	steps(kit1, X_POS[1]-step_size, Y_POS[1], Z, 1)
	steps(kit1, X_POS[3]+step_size, Y_POS[3], Z, 3)
	steps(kit2, X_POS[5]-step_size, Y_POS[5], Z-1, 5)	
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
 
def stance4():
	steps(kit2, X_POS[4]-step_size, Y_POS[4], Z, 4)
	steps(kit2, X_POS[6]+step_size, Y_POS[6], Z, 6)
	steps(kit1, X_POS[2]+step_size, Y_POS[2], Z, 2)	
	steps(kit1, X_POS[1], Y_POS[1], Z, 1)
	steps(kit1, X_POS[3], Y_POS[3], Z, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)

def return_back3():
	steps(kit1, X_POS[1], Y_POS[1], Z, 1)
	steps(kit1, X_POS[3], Y_POS[3], Z, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)	
	steps(kit2, X_POS[4]-step_size, Y_POS[4], 0, 4)
	steps(kit2, X_POS[6]+step_size, Y_POS[6], 0, 6)
	steps(kit1, X_POS[2]+step_size, Y_POS[2], 0, 2)	

def return_back4():
	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit1, X_POS[1]-step_size, Y_POS[1], 0, 1)
	steps(kit1, X_POS[3]+step_size, Y_POS[3], 0, 3)
	steps(kit2, X_POS[5]-step_size, Y_POS[5], 0, 5)

def forward_walk():
	swing1()
	time.sleep(delay)
	return_back2()
	time.sleep(delay)
	stance1()
	time.sleep(delay)
	swing2()
	time.sleep(delay)
	return_back1()
	time.sleep(delay)
	stance2()
	time.sleep(delay)

def backward_walk():
	swing3()
	time.sleep(delay)
	return_back4()
	time.sleep(delay)
	stance3()
	time.sleep(delay)
	swing4()
	time.sleep(delay)
	return_back3()
	time.sleep(delay)
	stance4()
	time.sleep(delay)


def rotation_matrice(leg_num, rotation_angle):
	x = X_POS[leg_num]
	y = Y_POS[leg_num]
	if leg_num == 3 or leg_num == 6:
		x *= -1
	if leg_num > 3:
		y *= -1
	x, y, z = Z_rotation(x, y, Z, rotation_angle)
	return x, y, z


def swing_rotation(x, y, leg_num, right=False, left=False):
	if leg_num <= 3:
		steps(kit1, abs(x), abs(y), 0, leg_num, True, False, left)
	else:
		steps(kit2, abs(x), abs(y), 0, leg_num, True, False, left)


def stance_rotation(x, y, leg_num, right=False, left=False):
	if leg_num <= 3:
		steps(kit1, abs(x), abs(y), Z, leg_num, False, True, left)
	else:
		steps(kit2, abs(x), abs(y), Z, leg_num, False, True, left)

	
def rotate(angle, right=False, left=False):
	for leg in range(1, 7, 2):
		x, y, z = rotation_matrice(leg, angle)
		swing_rotation(x, y, leg, right, left)

	time.sleep(delay)

	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)

	time.sleep(delay)

	for leg in range(1, 7, 2):
		x, y, z = rotation_matrice(leg, angle)
		stance_rotation(x, y, leg, right, left)

	time.sleep(delay)

	for leg in range(2, 7, 2):
		x, y, z = rotation_matrice(leg, angle)
		swing_rotation(x, y, leg, right, left)

	time.sleep(delay)

	steps(kit1, X_POS[1], Y_POS[1], Z, 1)
	steps(kit1, X_POS[3], Y_POS[3], Z, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)

	time.sleep(delay)

	for leg in range(2, 7, 2):
		x, y, z = rotation_matrice(leg, angle)
		stance_rotation(x, y, leg, right, left)

	time.sleep(delay)

	for leg in range(1, 7, 2):
		x, y, z = rotation_matrice(leg, angle)
		swing_rotation(x, y, leg, right, left)

	time.sleep(delay)
	steps(kit2, X_POS[4], Y_POS[4], Z, 4)
	steps(kit2, X_POS[6], Y_POS[6], Z, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	time.sleep(delay)


standard_stance(Z)
time.sleep(1)

def pitch_down():
	steps(kit2, X_POS[4], Y_POS[4], 5, 4)
	steps(kit2, X_POS[6], Y_POS[6], 15, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit1, X_POS[1], Y_POS[1], 5, 1)
	steps(kit1, X_POS[3], Y_POS[3], 15, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)

def pitch_up():
	steps(kit2, X_POS[4], Y_POS[4], 15, 4)
	steps(kit2, X_POS[6], Y_POS[6], 5, 6)
	steps(kit1, X_POS[2], Y_POS[2], Z, 2)
	steps(kit1, X_POS[1], Y_POS[1], 15, 1)
	steps(kit1, X_POS[3], Y_POS[3], 5, 3)
	steps(kit2, X_POS[5], Y_POS[5], Z-1, 5)

def yaw_right():
	steps(kit2, X_POS[4], Y_POS[4], 15, 4)
	steps(kit2, X_POS[6], Y_POS[6], 15, 6)
	steps(kit1, X_POS[2], Y_POS[2], 5, 2)
	steps(kit1, X_POS[1], Y_POS[1], 5, 1)
	steps(kit1, X_POS[3], Y_POS[3], 5, 3)
	steps(kit2, X_POS[5], Y_POS[5], 14, 5)

def yaw_left():
	steps(kit2, X_POS[4], Y_POS[4], 5, 4)
	steps(kit2, X_POS[6], Y_POS[6], 5, 6)
	steps(kit1, X_POS[2], Y_POS[2], 15, 2)
	steps(kit1, X_POS[1], Y_POS[1], 15, 1)
	steps(kit1, X_POS[3], Y_POS[3], 15, 3)
	steps(kit2, X_POS[5], Y_POS[5], 4, 5)

def rotate_left():
	rotate(-20, right=False, left=True)
	time.sleep(0.2)
	for leg in range(1, 7, 2):
			theta, beta, alpha = ik(X_POS[leg], Y_POS[leg], 0, leg)
			if leg < 5:
				kit1.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
				kit1.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
				kit1.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
			else:
				kit2.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
				kit2.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
				kit2.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
			time.sleep(delay)

if __name__ == '__main__':

	print("forward walk")
	#forward_walk()
	#time.sleep(delay)
	#forward_walk()
	#time.sleep(delay)
	#forward_walk()
	#time.sleep(delay)
	#forward_walk()
	#time.sleep(delay)
	#steps(kit1, X_POS[2], Y_POS[2], 0, 2)
	#steps(kit2, X_POS[4], Y_POS[4], 0, 4)
	#steps(kit2, X_POS[6], Y_POS[6], 0, 6)
	#time.sleep(delay)
	#standard_stance(Z)
	#time.sleep(1)

	#print("backward walk")
	#backward_walk()
	#time.sleep(delay)
	#backward_walk()
	#time.sleep(delay)
	#standard_stance(Z)
	#time.sleep(1)
	#
	print("rotate right")
	#rotate(20, right=True, left=False)
	#time.sleep(delay)
	#standard_stance(Z)
	#time.sleep(1)
	#
	#print("rotate left")
	#rotate(-20, right=False, left=True)
	#time.sleep(0.2)
	#for leg in range(1, 7, 2):
	#		theta, beta, alpha = ik(X_POS[leg], Y_POS[leg], 0, leg)
	#		if leg < 5:
	#			kit1.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
	#			kit1.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
	#			kit1.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
	#		else:
	#			kit2.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
	#			kit2.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
	#			kit2.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
	#		time.sleep(delay)
	#
	#time.sleep(delay)
	#standard_stance(Z)
	##time.sleep(1)
	#standard_stance(Z)
	#
	#
	##swing2()
	##standard_stance(Z)
	#count = 0
	#
	##standard_stance(13)
	#
	##for _ in range(2):
	##	rotate(-20, right=False, left=True)
	##for leg in range(1, 7, 2):
	##		theta, beta, alpha = ik(X_POS[leg], Y_POS[leg], 0, leg)
	##		if leg < 5:
	##			kit1.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
	##			kit1.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
	#			kit1.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
	#		else:
	#			kit2.servo[LEG_SERVOS_NUM[leg][0]].angle = theta
	#			kit2.servo[LEG_SERVOS_NUM[leg][1]].angle = beta
	#			kit2.servo[LEG_SERVOS_NUM[leg][2]].angle = alpha
	#time.sleep(0.1)
	#standard_stance(Z)
	#swing2()
	#standard_stance(Z)

	#while True:
	#	accel_xout = read_word_2c(0x3b)
	#	accel_yout = read_word_2c(0x3d)
	#	accel_zout = read_word_2c(0x3f)
	#	
	#	accel_xout_scaled = accel_xout / 16384.0
	#	accel_yout_scaled = accel_yout / 16384.0
	#	accel_zout_scaled = accel_zout / 16384.0
	#	print("X rotation: ", get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	#	print("Y rotation: ", get_y_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	#	time.sleep(0.2)
	#
	#	x_angle = get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled)
	#	
	#	#while x_angle > 1:
	#	#	x, y, z = X_rotation(X_POS[leg], Y_POS[leg], Z, x_angle)
	#	#	x_angle -= 1
	#
	#	if x_angle > 10:
	#		x_angle += 5
	#	
	#	if -24 < x_angle < -2:
	#			for leg in range(1, 4):
	#				x, y, z = X_rotation(X_POS[leg], Y_POS[leg], Z, x_angle)
	#				print("coordnates:",x, y, z)
	#				steps(kit1, x, y, z, leg)
	#			for leg in range(4, 7):
	#				x, y, z = X_rotation(X_POS[leg], Y_POS[leg], Z, -x_angle)
	#				print("coordnates:", x, y, z)
	#				steps(kit2, x, y, z, leg)
	#	elif 24 > x_angle > 2:
	#		for leg in range(1, 4):
	#			x, y, z = X_rotation(X_POS[leg], Y_POS[leg], Z, x_angle)
	#			print("coordnates:",x, y, z)
	#			steps(kit1, x, y, z, leg)
	#		for leg in range(4, 7):
	#			x, y, z = X_rotation(X_POS[leg], Y_POS[leg], Z, -x_angle)
	#			print("coordnates:",x, y, z)
	#			steps(kit2, x, y, z, leg)
	#
	#	time.sleep(0.3)
	#	
	#	accel_xout = read_word_2c(0x3b)
	#	accel_yout = read_word_2c(0x3d)
	#	accel_zout = read_word_2c(0x3f)
	#	
	#	accel_xout_scaled = accel_xout / 16384.0
	#	accel_yout_scaled = accel_yout / 16384.0
	#	accel_zout_scaled = accel_zout / 16384.0
	#	print("X rotation222: ", get_x_rotation(accel_xout_scaled, accel_yout_scaled, accel_zout_scaled))
	#

	pitch_up()
	time.sleep(0.5)
	pitch_down()
	time.sleep(0.5)
	yaw_left()
	time.sleep(0.5)
	yaw_right()

