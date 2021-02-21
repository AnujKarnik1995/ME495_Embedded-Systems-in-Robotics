# -- ME495 -- Homework2 -- Anuj Karnik

## Part 1: Drive the Turtlebot in a figure of '8'

### Instructions:
1. Use the launch file *figure_eight.launch* to run the program. 
2. Implementation has been limited and not all tasks have been achieved.
3. The trajectory and controls have been implemented successfully.
4. The *pause/resume* service and *transformation_broadcaster* have NOT been implemented.
5. The math in homework2.py has been verified by *unittest*.
6. The math has been explained in the 'Calculations' pdf.

### Aside:
Launching *rviz* and *turtle_sim* causes the publishing frequency to drop. The turtle deviates from trajectory if rviz is turned on.

### Results:
1. The rqt_plot: *rqt_graph_for_Part2.png*
2. The turtle_sim [video](https://drive.google.com/file/d/1lknS3N5-MPZQw_S9MYcKrtn08k1t7BQD/view?usp=sharing)
3. Video showing discrepancy when rviz is running can be seen [here](https://drive.google.com/file/d/1eWV3fOx9ZpenT7-c4LSwilzgj3IX0diV/view?usp=sharing)

## Part 2: Robot Arm with URDF/Xacro

### Instructions:
1. Use the launch file *Part2.launch* to run the simulation.
2. By default, the file will generte the 2R robot and launch the *robot_state_publisher* and *rviz*.
3. By default, the markers have been turned off and the js_check has been disabled (because of the issues with Joint_state_publisher use_gui). This launches the *arm_traj* node.

Launch options:
- *mark_check*: set to 1 to launch the marker view. They appear and disappear at regular intervals.
- *rviz_check*: set to 0 to avoid launching rviz

### Results:
1. The rqt plot: *RQT_graph_for_Part2.png*
2. The motion with markers can be seen [here](https://drive.google.com/file/d/1J_h55WY_aEvyZOxJSZMP7cFJ4K6_bkkx/view?usp=sharing)
3. The motion without markers can be seen [here](https://drive.google.com/file/d/1vHU5B_QJc3phmaHYlXTdLX9ALWTkndWI/view?usp=sharing)

### Inverse Kinematics:
The inverse kinematics of the 2R robot were found from 'Modern Robotics' by Lynch, Park.
