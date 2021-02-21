#Python module  homework2 containing Trajectory and Controls Data.
import numpy as np
import math


class FigureEight (object):
    """
    Class dealing with ccalculations for the figure of 8 trajectory.
    It uses functions from the Modern Robotics library.
    The eqn and math for the figure of 8 has been described in <NEED TO SPECIFY>

    """
    def traj_gen(T, w, h, time):     
        xt = (w/2)*(math.sin(2*np.pi*(time)/T))
        yt = (h/2)*(math.sin(4*np.pi*(time)/T))

        xdot = (w*(np.pi)/T)*math.cos(2*(np.pi)*time/T)
        ydot = (2*(np.pi)*h/T)*math.cos(4*(np.pi)*time/T)

        traj = np.array([xt, yt, xdot, ydot])
        return traj
                  
class kinematics(object):
    """
    Class containing functions dealing with the control input calculations
    """

    def control_inputs(T,w,h, xdot, ydot, time): #still not sure about time and what to do with it
        """
        The x, y values returned from traj_gen will form the inputs for this function.
        The Math is elaborated in the sympy code in the repo.
        """
        v= math.sqrt((xdot**2)+(ydot**2))  #caluculation of linear velocity

        A = 2*(np.pi)/T
        B = 2*h/w
        C1 = math.cos(A*time)
        C2 = math.cos(2*A*time)
        S1 = math.sin(A*time)
        S2 = math.sin(2*A*time)

        omega = (1/(1+B*(C2/C1)))*B*(((C1*-S2*2*A)-(C2*-S1*A))/(C1)**2)
        
        CI = [v, omega] #calculating v,w

        return CI
        
