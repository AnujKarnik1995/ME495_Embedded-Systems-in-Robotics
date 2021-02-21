#Python module  homework2 containing Trajectory and Controls Data.
import numpy as np
import math
"""
Python package containing the calculations for the trajectory and kinematics.
The eqn and math for the functions has been described in the pdf "Calculations" in the repo
"""

class FigureEight (object):
    """
    Class dealing with calculations for the figure of 8 trajectory.
    

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
        
        #Second manual implementation: worked equally well.
        """
        A = 2*(np.pi)/T
        B = 2*h/w
        C1 = math.cos(A*time)
        C2 = math.cos(2*A*time)
        S1 = math.sin(A*time)
        S2 = math.sin(2*A*time)
        omega = (1/(1+(B*(C2/C1))**2))*B*(((C1*(-S2)*2*A)-(C2*(-S1)*A))/(C1**2))
        """
        xddot = (2*w*((np.pi)/T)**2)*(-math.sin((2*(np.pi)*time)/T))  #accelaration in x

        yddot = (8*h*((np.pi)/T)**2)*(-math.sin((4*(np.pi)*time)/T))  #accelaration in y

        uv = (xdot*yddot - ydot*xddot)/(xdot**2)
        atan = 1/(1+((ydot/xdot)**2))

        omega = atan*uv

        CI = [v, omega, xddot,yddot] #calculating v,w

        return CI
        
