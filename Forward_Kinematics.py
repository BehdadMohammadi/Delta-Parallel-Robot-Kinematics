import math

parameters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

theta_1 = 1
theta_2 = 1
theta_3 = 1

theta_1 = theta_1 + parameters[18]
theta_2 = theta_2 + parameters[19]
theta_3 = theta_3 + parameters[20]

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

print(Xp)
print(Yp)
print(Zp)
