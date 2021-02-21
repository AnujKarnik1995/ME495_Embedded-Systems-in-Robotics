# -- ME 495 -- HOMEWORK3 -- ANUJ KARNIK 

## Part 1 : Gazebo Differential Drive Challenge

### Execution Instructions:
1. Use the launch file *ddrive.launch* to run the program. It generates the urdf file from the xacro file.
2. The file will load a custom gazebo world with the diff_drive robot already loaded. There are also a few other objects in the world.
3. The node *follow_rect* is also automatically (by default) launched. With this, the robot follows an open loop rectangular path.
4. To see the robot perform some flips, run the launch file with the argument *rect:=0*. It runs the *flip* node.
5. The robot will drive and execute some flips.
6. To see the odometry data in rviz, use the argument *rvizconfig:=1*.
7. It will launch rviz along with gazebo and load a saved configuration which will display the odometry data.

### Results:
1. The rqt_plots of the system are saved as:
    1. Follow_rectangle: *follow_rect.png*
    2. Flip: *flip.png*
    3. rviz: *rviz+gazebo.png*
2. The diff_drive robot following the rectangular path can be seen in this video:
*https://drive.google.com/file/d/1bF2rFGnxhj6byTZuc4huDfcmCLXAKlb4/view?usp=sharing*

3. The robot executing flips driving can be seen in this video: 
*https://drive.google.com/file/d/1yAYAOu57hVjTX5CTqJZ5gwwcYr5Rn6SR/view?usp=sharing*
