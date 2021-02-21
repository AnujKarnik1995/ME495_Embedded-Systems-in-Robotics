"""
The test case code. (Not executable)

Case 1 is defined at the start when t = 0.
Case 2 is defined at (T/4) where the robot should be at the end of the loop of the'8' figure.

Both the cases are for the first function traj_gen()

"""

import unittest
import homework2.homework2 as h2
import math
import numpy as np

class Test(unittest.TestCase):
    def test_case1(self):
        #checks results for [xd, yd, xdot, ydot] at t = 0
        # inputs to traj_gen() are: (T,w,h,time)
        answer1 = h2.FigureEight.traj_gen(16, 0.8, 2, 0)
        delta = (np.pi)/20
        beta = (np.pi)/4
        answer2 = [0,0,delta, beta]
        self.assertEquals(answer1[0], answer2[0])
        self.assertEquals(answer1[1], answer2[1])
        self.assertEquals(answer1[2], answer2[2])
        self.assertEquals(answer1[3], answer2[3])
    
    def test_case2(self):
        #checks results for [xd, yd, xdot, ydot] at t = 4
        a1 = h2.FigureEight.traj_gen(16, 0.8, 2, 4)
        
        f0 = round(a1[0],5)
        f1 = round(a1[1],5)
        f2 = round(a1[2],5)
        f3 = round(a1[3],5)

        answer3 = [f0, f1, f2, f3]

        answer4 = [0.4, 0.0, 0.0, -0.7854]

        self.assertEquals(answer3[0], answer4[0])
        self.assertEquals(answer3[1], answer4[1])
        self.assertEquals(answer3[2], answer4[2])
        self.assertEquals(answer3[3], answer4[3])

    def test_case3(self):
        #checks results for [v, omega, xddot, yddot] at t = 0
        control1 = h2.kinematics.control_inputs(16,0.8,2, (np.pi)/20, (np.pi)/4,0)
        control1[0] = round(control1[0],5)
        control1[1] = round(control1[1],5)
        control1[2] = round(control1[2],5)
        control1[3] = round(control1[3],5)

        control2 = [0.80095,-0.0,-0.0,-0.0]

        self.assertEquals(control1[0], control2[0])
        self.assertEquals(control1[1], control2[1])
        self.assertEquals(control1[2], control2[2])
        self.assertEquals(control1[3], control2[3])

    def test_case4(self):
        #checks results for [v, omega, xddot, yddot] at t = 4
        control3 = h2.kinematics.control_inputs(16,0.8,2, (np.pi)/20, (np.pi)/4,4)
        control3[0] = round(control3[0],5)
        control3[1] = round(control3[1],5)
        control3[2] = round(control3[2],5)
        control3[3] = round(control3[3],5)

        control4 = [0.80095,0.07552,-0.06169,-0.0]

        self.assertEquals(control3[0], control4[0])
        self.assertEquals(control3[1], control4[1])
        self.assertEquals(control3[2], control4[2])
        self.assertEquals(control3[3], control4[3])


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(homework2, 'Test_Case', Test)
