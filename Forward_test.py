import math
import numpy as np

sqrt3  = math.sqrt(3.0)
pi     = 3.141592653
sin120 = sqrt3 / 2.0
cos120 = -0.5
tan60  = sqrt3
sin30  = 0.5
tan30  = 1.0 / sqrt3

e= (1/math.tan(np.deg2rad(30))) * 20
f= (1/math.tan(np.deg2rad(30))) * 26
re = 59.5
rf =  30.9

def Forward(theta1, theta2, theta3):
    x0 = 0.0
    y0 = 0.0
    z0 = 0.0
    
    t = (f-e) * tan30 / 2.0
    dtr = pi / 180.0
    
    theta1 *= dtr
    theta2 *= dtr
    theta3 *= dtr
    
    y1 = -(t + rf*math.cos(theta1) )
    z1 = -rf * math.sin(theta1)
    
    y2 = (t + rf*math.cos(theta2)) * sin30
    x2 = y2 * tan60
    z2 = -rf * math.sin(theta2)
    
    y3 = (t + rf*math.cos(theta3)) * sin30
    x3 = -y3 * tan60
    z3 = -rf * math.sin(theta3)
    
    dnm = (y2-y1)*x3 - (y3-y1)*x2
    
    w1 = y1*y1 + z1*z1
    w2 = x2*x2 + y2*y2 + z2*z2
    w3 = x3*x3 + y3*y3 + z3*z3
    
    # x = (a1*z + b1)/dnm
    a1 = (z2-z1)*(y3-y1) - (z3-z1)*(y2-y1)
    b1= -( (w2-w1)*(y3-y1) - (w3-w1)*(y2-y1) ) / 2.0
    
    # y = (a2*z + b2)/dnm
    a2 = -(z2-z1)*x3 + (z3-z1)*x2
    b2 = ( (w2-w1)*x3 - (w3-w1)*x2) / 2.0
    
    # a*z^2 + b*z + c = 0
    a = a1*a1 + a2*a2 + dnm*dnm
    b = 2.0 * (a1*b1 + a2*(b2 - y1*dnm) - z1*dnm*dnm)
    c = (b2 - y1*dnm)*(b2 - y1*dnm) + b1*b1 + dnm*dnm*(z1*z1 - re*re)

    d = b*b - 4.0*a*c
    if d < 0.0:
        return [1,0,0,0] 
    
    z0 = -0.5*(b + math.sqrt(d)) / a
    x0 = (a1*z0 + b1) / dnm
    y0 = (a2*z0 + b2) / dnm

    return [0,x0,y0,z0]






def My_Forward(theta1, theta2, theta3):
    
    parameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    theta_1 = math.radians(theta1)
    theta_2 = math.radians(theta2)
    theta_3 = math.radians(theta3)

    theta_1 = theta_1 + parameters[18]
    theta_2 = theta_2 + parameters[19]
    theta_3 = theta_3 + parameters[20]

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

    a_1 = 2*r_1*math.cos(beta_1)-2*(R_1+L1_1*math.cos(theta_1))*math.cos(landa_1)
    a_2 = 2*r_2*math.cos(beta_2)-2*(R_2+L1_2*math.cos(theta_2))*math.cos(landa_2)
    a_3 = 2*r_3*math.cos(beta_3)-2*(R_3+L1_3*math.cos(theta_3))*math.cos(landa_3)

    b_1 = 2*r_1*math.sin(beta_1)-2*(R_1+L1_1*math.cos(theta_1))*math.sin(landa_1)
    b_2 = 2*r_2*math.sin(beta_2)-2*(R_2+L1_2*math.cos(theta_2))*math.sin(landa_2)
    b_3 = 2*r_3*math.sin(beta_3)-2*(R_3+L1_3*math.cos(theta_3))*math.sin(landa_3)

    c_1 = 2*L1_1*math.sin(theta_1)
    c_2 = 2*L1_2*math.sin(theta_2)
    c_3 = 2*L1_3*math.sin(theta_3)

    d_1 = (R_1+L1_1*math.cos(theta_1))**2+r_1**2+(L1_1*math.sin(theta_1))**2-2*r_1*(R_1+L1_1*math.cos(theta_1))*math.cos(landa_1-beta_1)-L2_1**2
    d_2 = (R_2+L1_2*math.cos(theta_2))**2+r_2**2+(L1_2*math.sin(theta_2))**2-2*r_2*(R_2+L1_2*math.cos(theta_2))*math.cos(landa_2-beta_2)-L2_2**2
    d_3 = (R_3+L1_3*math.cos(theta_3))**2+r_3**2+(L1_3*math.sin(theta_3))**2-2*r_3*(R_3+L1_3*math.cos(theta_3))*math.cos(landa_3-beta_3)-L2_3**2

    A2 = a_1 - a_2
    A3 = a_1 - a_3

    B2 = b_1 - b_2
    B3 = b_1 - b_3

    C2 = c_1 - c_2
    C3 = c_1 - c_3

    D2 = d_1 - d_2
    D3 = d_1 - d_3

    m1 = (B2*C3-B3*C2)/(A2*B3-A3*B2)
    m2 = (A3*C2-A2*C3)/(A2*B3-A3*B2)

    n1 = (B2*D3-B3*D2)/(A2*B3-A3*B2)
    n2 = (A3*D2-A2*D3)/(A2*B3-A3*B2)

    Zp_1 = -(math.sqrt((a_3*m1+2*m1*n1+b_3*m2+2*m2*n2+c_3)**2-4*(m1**2+m2**2+1)*(n1**2+a_3*n1+n2**2+b_3*n2+d_3))+(a_3*m1+b_3*m2+2*m1*n1+2*m2*n2+c_3))/(2*m1**2+2*m2**2+2);
    Zp_2 = (math.sqrt((a_3*m1+2*m1*n1+b_3*m2+2*m2*n2+c_3)**2-4*(m1**2+m2**2+1)*(n1**2+a_3*n1+n2**2+b_3*n2+d_3))-(a_3*m1+b_3*m2+2*m1*n1+2*m2*n2+c_3))/(2*m1**2+2*m2**2+2);

    if Zp_1 <= 0:
        Zp = Zp_1;
    else:
        Zp = Zp_2;

    Xp = m1*Zp+n1;
    Yp = m2*Zp+n2;

    return [0, Xp/10, Yp/10, Zp/10]


theta1 = 10
theta2 = 20
theta3 = 0

test1 = Forward(theta1, theta2, theta3)
test2 = My_Forward(theta1, theta2, theta3)

print(test1)
print(test2)

