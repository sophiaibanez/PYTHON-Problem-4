import math
import numpy as np
import matplotlib.pyplot as plt

y0 = float(input('Enter initial height:  '))                    
v0 = float(input('Enter velocity:  '))  
angle = float(input('Enter angle (with respect to x-axis): '))
ax = float(input('Enter initial acceleration in x:  '))
ay = float(input('Enter initial acceleration in y:  '))

if ay == 0:
    print('Error. There is no vertical acceleration.')
    
else:
    x0 = 0;
    vx_initial = v0 * math.degrees(math.cos(angle))
    vy_initial = v0 * math.degrees(math.sin(angle))
    tf = np.roots([(1/2)*ay, vy_initial, y0])
    tf = max(tf)
    t = np.array([np.linspace(0,tf)])
    x = x0 + vx_initial*t + (1/2)*ax*t**2
    y = y0 + vy_initial*t + (1/2)*ay*t**2
    
    ax_ideal = 0
    ay_ideal = -9.8
    x_ideal = x0 + vx_initial*t
    y_ideal = y0 + vy_initial*t + (1/2)*ay_ideal*t**2
    
    plt.plot(x,y)
    plt.plot(x_ideal, y_ideal,'g')
    plt.title ('Projectile Trajectory')
    plt.xlabel('Horizontal distance (in meters)')
    plt.ylabel('Height (in meters)')
    plt.legend('Non-ideal Trajectory','Ideal Trajectory')
    plt.axis('tight')
    plt.grid()
    plt.show()
    
    