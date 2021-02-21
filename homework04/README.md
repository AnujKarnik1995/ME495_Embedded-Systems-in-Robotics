# -- ME495 -- Homework4 --Anuj Karnik

## Options
1. All launch files have the option to run the program on either the real turtlebot or in gazebo.
2. The *simulation* argument is set to TRUE by default for all the launch files.

## Launching the files on the actual turtlebot: 
1. The turtlebot has been configured to connect to the PC running the roscore. 
2. First launch the launch files on the computer using roslaunch.
3. Then `ssh` into the turtlebot and use `roslaunch turtlebot3_bringup turtlebot3_robot.launch` command.

## Instructions:
All the following files can be launched in the manner shown: `roslaunch homework4 *filename* simulation:=true/false` <br>
    a. `start_slam.launch`: <br>
    argument sync= true for online_sync and false for online_async. <br>
    This launch file runs the basic navigation setup for the turtlebot. It launches the teleop node, slam_toolbox, and rviz in proper configuration. <br><br>
    b. `nav_stack.launch`: <br>
    This launch file launches the map saved in the first step, the AMCL node, the move_base action client and rviz. <br>
    The robot moves to points published through rviz and usel amcl particles to paint as estimate of its locaation. <br><br>
    c. `slam_stack.launch`: <br>
    The *slam_stack* launch file ditches the amcl node and the pre-built map for the slam-toolbox. <br>
    The map is generated in real time as the robot explores the environment.<br>
    Destination points still have to be fed through rviz using the *2D Path Planning* option. <br><br>
    d. `part6.launch`: <br>
    The last launch file is used by the robot to autonomously explore an area.<br>
    It launches the same nodes as the *slam_stack* launch file with the addition of the *nav_node* node. <br>
    
## Results:
1. The map generated from `start_slam.launch` can be seen in the /maps folder under *map.pgm*.
2. The following link shows the actual turtlebot performing the tasks: <br>
[live_view](https://drive.google.com/file/d/1NIhUMulYgZG_buWTISAHfolE-Lr_DM07/view?usp=sharing)
3. The map generated from `nav_stack.launch` can be seen in the /maps folder under *navstack_real.pgm*.
4. The results from `nav_stack.launch` can be seen in the video link below:<br>
[live_view](https://drive.google.com/file/d/1yAL-FJK-JEq-qtEcyw-oJvEfG88qVFkN/view?usp=sharing)
5. The results from `slam_stack.launch` can be seen in the *part5_real.pgm* file in the /maps folder.
6. The link to the video of the results:
[live_view](https://drive.google.com/file/d/1jbbu2utUMzgtQgOQSSTOa2-csB3WETBL/view?usp=sharing) <br>
At the 3:00 mark, the video shows the robot replanning the path after an unforeseen obstacle is placed in its path.
7. The results of the autonomous exploration can be seen in the *expl.pgm* (for the gazebo version) and *expl_actual.pgm* (for the actual turtlebot version) in the /maps folder.
8. The video results for the same can be found in the links mentioned: <br>
[gazebo](https://drive.google.com/file/d/1tZxxd9CWbW-w-YAvvy4SvMhhjrk9CyJY/view?usp=sharing) <br>
[live_view](https://drive.google.com/file/d/1S4LVYx1sdQ8lqYauX4CgGC2Hs1p45xN1/view?usp=sharing) <br><br>

## Node explanation:
1. The *nav_node* is the main node used to generate waypoints for the /move_base client.
2. It does not use any well defined strategies exploration strategies.
3. The node uses data from the `/scan` topic and randomly selects a direction to explore.
4. A random, valid pair of distance and angle from the `/scan` topic is recorded.
5. Taking into account the current location of the turtlebot in the `/map` frame, the distances are used to generate target/goal x, y coordinates for the `/move_base` client (SimpleActionClient).
6. To keep things straightforward, the orientation is always kept fixed at w = -1.
7. The algorithm is not fast or efficient and many times causes the turtlebot to revisit the locations it already passed through.
8. However, given enough time, it does explore all parts of the maps, as can be seen in the videos linked in Results (point 8).
9. Overall in both the real world and the simulation, the turtlebot explored the rooms successfully.
10. At times the bot would get stuck/trapped in corners and would have a tough time exiting. More parameter tweaking is needed as I feel the stock parameters for the turtlebot are fairly conservative. 

