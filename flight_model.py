import numpy as np
import matplotlib.pyplot as plt
from math import *

#以下，テキストの数値例を写経
#縦の有次元安定微係数
Xu=-0.0215
Zu=-0.227
Mu=0
Xa=14.7
Za=-236
Ma=-3.78
Madot=-0.28
Xq=0
Zq=-5.76
Mq=-0.992

X_deltat=0
Z_deltae=-12.9
Z_deltat=0
M_deltae=-2.48
M_deltat=0

#安定軸での水平つり合い飛行条件での飛行速度など
knot=240
U0=knot/0.592484 #293.8
W0=0    #0
g=9.80  #9.8
theta0=0.0  #0.0


#4次ルンゲクッタ
#x=[u,a,theta,q] 運動変数
#縦の運動パラメータの微分計算
#u1=[delta_e,delta_t] = 操縦項
def deriv_pitch(x,u1):
    du=Xu*x[0]+Xa*x[1]-g*np.cos(theta0)*x[2]-W0*x[3]+X_deltat*u1[1]
    da=Zu/U0*x[0]+Za/U0*x[1]-g*np.sin(theta0)/U0*x[2]+(U0+Zq)/U0*x[3]+(M_deltae+Madot*Z_deltae/U0)*u1[0]+(M_deltat+Madot*Z_deltat/U0)*u1[1]
    dtheta=x[3]
    dq=(Madot*Zu/U0+Mu)*x[0]+(Ma+Madot*Za/U0)*x[1]-Madot*g*np.sin(theta0)/U0*x[2]+(Madot*(U0+Za)+Mq*U0)/U0*x[3]+(M_deltae+Madot*Z_deltae/U0)*u1[0]+(M_deltat+Madot*Z_deltat/U0)*u1[1]
    dx=np.array([du,da,dtheta,dq])
    return dx
#時間の刻み幅
dt=0.01
#時間の経過範囲
T=np.arange(0.0,300.0,dt)
N=len(T)
X=np.zeros((N,4))
#微小擾乱の初期値
u0=0
a0=0
q0=0
theta_ini=0
#操縦項を定数
u1=[0,0]
#運動変数を格納する行列
X[0,:]=np.array([u0,a0,theta_ini,q0])

for i in range(1,N):
    k1=deriv_pitch(X[i-1,:],u1)
    k2=deriv_pitch(X[i-1,:]+0.5*dt*k1,u1)
    k3=deriv_pitch(X[i-1,:]+0.5*dt*k2,u1)
    k4=deriv_pitch(X[i-1,:]+dt*k3,u1)
    X[i,:]=X[i-1,:]+dt/6*(k1+2*k2+2*k3+k4)

#1ft/s = 0.592484knot
print('U0={:1.2f}ft/s {:1.2f}knot\n'.format(U0,knot))
print('stick=[{:1.3f},{:1.3f}]\n'.format(u1[0],u1[1]))



plt.plot(T,X[:,0])
plt.xlabel('time [s]')
plt.ylabel('u [ft/s]')
plt.grid()
plt.show()

plt.plot(T,X[:,0]*0.592484)
plt.xlabel('time [s]')
plt.ylabel('u [knot]')
plt.grid()
plt.show()


plt.plot(T,X[:,1])
plt.xlabel('time [s]')
plt.ylabel('AoA [rad]')
plt.grid()
plt.show()

plt.plot(T,X[:,2])
plt.xlabel('time [s]')
plt.ylabel('theta [rad]')
plt.grid()
plt.show()

plt.plot(T,X[:,2]*180/np.pi)
plt.xlabel('time [s]')
plt.ylabel('theta [degree]')
plt.grid()
plt.show()

plt.plot(T,X[:,3])
plt.xlabel('time [s:')
plt.ylabel('q [rad/s]')
plt.grid()
plt.show()


