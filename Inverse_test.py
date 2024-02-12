import math
import numpy as np

e= (1/math.tan(np.deg2rad(30))) * 20
f= (1/math.tan(np.deg2rad(30))) * 26
re = 59.5
rf =  30.9

sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3

def _angle_yz(x0, y0, z0, theta=None):
    y1 = -0.5*0.57735*f # f/2 * tg 30
    y0 -= 0.5*0.57735*e # shift center to edge
    # z = a + b*y
    a = (x0*x0 + y0*y0 + z0*z0 + rf*rf - re*re - y1*y1) / (2.0*z0)
    b = (y1-y0) / z0

    d = -(a + b*y1)*(a + b*y1) + rf*(b*b*rf + rf)
    if d<0:
        return [1,0] 

    yj = (y1 - a*b - math.sqrt(d)) / (b*b + 1) 
    zj = a + b*yj
    theta = math.atan(-zj / (y1-yj)) * 180.0 / pi + (180.0 if yj>y1 else 0.0)
    
    return [0,theta] # return error, theta

def Inverse(x0, y0, z0):
    theta1 = 0
    theta2 = 0
    theta3 = 0
    status = _angle_yz(x0,y0,z0)

    if status[0] == 0:
        theta1 = status[1]
        status = _angle_yz(x0*cos120 + y0*sin120,
                                   y0*cos120-x0*sin120,
                                   z0,
                                   theta2)
    if status[0] == 0:
        theta2 = status[1]
        status = _angle_yz(x0*cos120 - y0*sin120,
                                   y0*cos120 + x0*sin120,
                                   z0,
                                   theta3)
    theta3 = status[1]

    return [status[0],theta1,theta2,theta3]



def My_Inverse(x, y, z):

    parameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    x = x * 10
    y = y * 10
    z = z * 10

    #landa_1 = 1*(math.pi/6) + parameters[0]
    #landa_2 = 5*(math.pi/6) + parameters[1]
    #landa_3 = 9*(math.pi/6) + parameters[2]

    #beta_1 = 1*(math.pi/6) + parameters[3]
    #beta_2 = 5*(math.pi/6) + parameters[4]
    #beta_3 = 9*(math.pi/6) + parameters[5]

    landa_1 = 9*(math.pi/6) + parameters[0]
    landa_2 = 1*(math.pi/6) + parameters[1]
    landa_3 = 5*(math.pi/6) + parameters[2]

    beta_1 = 9*(math.pi/6) + parameters[3]
    beta_2 = 1*(math.pi/6) + parameters[4]
    beta_3 = 5*(math.pi/6) + parameters[5]

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


    theta_1 = math.degrees((2*math.atan((-B_1-math.sqrt(B_1**2+A_1**2-D_1**2))/(D_1-A_1))) - parameters[18])
    theta_2 = math.degrees((2*math.atan((-B_2-math.sqrt(B_2**2+A_2**2-D_2**2))/(D_2-A_2))) - parameters[19])
    theta_3 = math.degrees((2*math.atan((-B_3-math.sqrt(B_3**2+A_3**2-D_3**2))/(D_3-A_3))) - parameters[20])

    return [0,theta_1,theta_2,theta_3]



x0 = 10
y0 = -10
z0 = -50

test1 = Inverse(x0, y0, z0)
test2 = My_Inverse(x0, y0, z0)

print(test1)
print(test2)