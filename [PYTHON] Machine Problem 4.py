import math
import numpy as np
import matplotlib.pyplot as plt

y0 = float(input('Enter initial height:  '))                    
v0 = float(input('Enter velocity:  '))  
angle = float(input('Enter angle (with respect to x-axis): '))
ax = float(input('Enter acceleration in x:  '))
ay = float(input('Enter acceleration in y:  '))

if ay == 0:
    print('Error. There is no vertical acceleration.')
    
else:
    x0 = 0;
    vx_initial = v0*(math.cos(angle * (math.pi/180)))
    vy_initial = v0*(math.sin(angle * (math.pi/180)))
    tf = np.roots([(1/2)*ay, vy_initial, y0])
    tf = max(tf)
    t = np.arange(0,tf,0.1)
    x = (x0 + vx_initial*t + (1/2)*ax*t**2).transpose()
    y = (y0 + vy_initial*t + (1/2)*ay*t**2).transpose()
    
    ax_ideal = 0
    ay_ideal = -9.8
    x_ideal = (x0 + vx_initial*t).transpose()
    y_ideal = (y0 + vy_initial*t + (1/2)*ay_ideal*t**2).transpose()
    
    plt.plot(x,y, label = 'Non-ideal')
    plt.plot(x_ideal, y_ideal,'g', label = 'Ideal')
    plt.legend()
    plt.title ('Projectile Trajectory')
    plt.xlabel('Horizontal distance (in meters)')
    plt.ylabel('Height (in meters)')
    plt.axis('tight')
    plt.grid()
    plt.tight_layout()
    plt.show()
    
