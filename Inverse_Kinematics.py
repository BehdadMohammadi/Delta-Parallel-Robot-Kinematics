import math

parameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

x = 0
y = 0
z = -500

landa_1 = 1*(math.pi/6) + parameters[0]
landa_2 = 5*(math.pi/6) + parameters[1]
landa_3 = 9*(math.pi/6) + parameters[2]

beta_1 = 1*(math.pi/6) + parameters[3]
beta_2 = 5*(math.pi/6) + parameters[4]
beta_3 = 9*(math.pi/6) + parameters[5]

L1_1 = 308.95 + parameters[6]
L1_2 = 308.95 + parameters[7]
L1_3 = 308.95 + parameters[8]

L2_1 = 595 + parameters[9]
L2_2 = 595 + parameters[10]
L2_3 = 595 + parameters[11]

R_1 = 140 + parameters[12]
R_2 = 140 + parameters[13]
R_3 = 140 + parameters[14]

r_1 = 100 + parameters[15]
r_2 = 100 + parameters[16]
r_3 = 100 + parameters[17]

A_1 = -2*L1_1*r_1*math.sin(beta_1)*math.sin(landa_1) -2*L1_1*r_1*math.cos(beta_1)*math.cos(landa_1) -2*L1_1*x*math.cos(landa_1) -2*L1_1*y*math.sin(landa_1) +2*L1_1*R_1
B_1 = +2*L1_1*z
D_1 = x**2 + y**2 + z**2 + L1_1**2 - L2_1**2 + R_1**2 + r_1**2 -2*R_1*r_1*math.sin(beta_1)*math.sin(landa_1) -2*R_1*r_1*math.cos(beta_1)*math.cos(landa_1) +2*r_1*x*math.cos(beta_1) +2*r_1*y*math.sin(beta_1) -2*R_1*x*math.cos(landa_1) -2*R_1*y*math.sin(landa_1)

A_2 = -2*L1_2*r_2*math.sin(beta_2)*math.sin(landa_2) -2*L1_2*r_2*math.cos(beta_2)*math.cos(landa_2) -2*L1_2*x*math.cos(landa_2) -2*L1_2*y*math.sin(landa_2) +2*L1_2*R_2
B_2 = +2*L1_2*z
D_2 = x**2 + y**2 + z**2 + L1_2**2 - L2_2**2 + R_2**2 + r_2**2 -2*R_2*r_2*math.sin(beta_2)*math.sin(landa_2) -2*R_2*r_2*math.cos(beta_2)*math.cos(landa_2) +2*r_2*x*math.cos(beta_2) +2*r_2*y*math.sin(beta_2) -2*R_2*x*math.cos(landa_2) -2*R_2*y*math.sin(landa_2)

A_3 = -2*L1_3*r_3*math.sin(beta_3)*math.sin(landa_3) -2*L1_3*r_3*math.cos(beta_3)*math.cos(landa_3) -2*L1_3*x*math.cos(landa_3) -2*L1_3*y*math.sin(landa_3) +2*L1_3*R_3
B_3 = +2*L1_3*z
D_3 = x**2 + y**2 + z**2 + L1_3**2 - L2_3**2 + R_3**2 + r_3**2 -2*R_3*r_3*math.sin(beta_3)*math.sin(landa_3) -2*R_3*r_3*math.cos(beta_3)*math.cos(landa_3) +2*r_3*x*math.cos(beta_3) +2*r_3*y*math.sin(beta_3) -2*R_3*x*math.cos(landa_3) -2*R_3*y*math.sin(landa_3)


theta_1 = (2*math.atan((-B_1-math.sqrt(B_1**2+A_1**2-D_1**2))/(D_1-A_1))) + parameters[18]
theta_2 = (2*math.atan((-B_2-math.sqrt(B_2**2+A_2**2-D_2**2))/(D_2-A_2))) + parameters[19]
theta_3 = (2*math.atan((-B_3-math.sqrt(B_3**2+A_3**2-D_3**2))/(D_3-A_3))) + parameters[20]

print(theta_1)
print(theta_2)
print(theta_3)