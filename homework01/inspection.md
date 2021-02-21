# CRAZY TURTLE
Demonstration package for ME495.
This README is intentionally vague.
Figuring out how this package works and filling in the details is part of the
exercise. Fill in the blanks between `<angle brackets>` with your answer.
Unless otherwise specified, list the command and all arguments that you passed to it.

## Setup Instructions
1. Compile the workspace by executing `catkin_make`
2. Initialize the ROS environment by exectuing `catkin_make`
3. Run the launchfile `go_crazy_turtle.launch` by executing `roslaunch go_crazy_turtle.launch`
4. When running you can see a visual depiction of the ROS graph using the `rqt_graph` command.
   The ROS graph, including all topics and node labels, looks like:
   ![<The ROS Graph>](https://github.com/ME495-EmbeddedSystems/homework01-AnujKarnik1995/blob/master/The_Ros_Graph_HW1.png)

## Runtime Information
5. Use the ROS command `rosnode list` to list all the nodes that are running.
   The output of the command looks like
   ```
/mover
/roaming_turtle
/rosout

   ```
6. Use the ROS command `rostopic list` to list the topics
   The output of the command looks like
   ```
   /rosout
   /rosout_agg
   /turtle1/cmd_vel
   /turtle1/color_sensor
   /turtle1/pose

   ```

7. Use the ROS command `rostopic hz /turtle1/cmd_vel` to verify that the frequency of the `/turtle1/cmd_vel` topic is `~60 (59.665) Hz`

8. Use the ROS command `rosservice list` to list the services.
   The output of the command looks like
   ```
/clear
/kill
/mover/get_loggers
/mover/set_logger_level
/reset
/roaming_turtle/get_loggers
/roaming_turtle/set_logger_level
/rosout/get_loggers
/rosout/set_logger_level
/spawn
/switch
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative

 
   ```
9. Use the ROS command `rosservice info /switch` to view information about the `/switch` service.
   The type of the `/switch` service is `crazy_turtle/Switch` and it is offered by
   the `/mover` node.

10. Use the ROS command `rosparam list` to list the parameters that are loaded
    into the parameter server.
    The output of the command looks like
    ```
/mover/velocity
/roaming_turtle/background_b
/roaming_turtle/background_g
/roaming_turtle/background_r
/rosdistro
/roslaunch/uris/host_ajubuntu__34507
/roslaunch/uris/host_ajubuntu__36165
/roslaunch/uris/host_ajubuntu__36525
/roslaunch/uris/host_ajubuntu__39359
/roslaunch/uris/host_ajubuntu__40565
/roslaunch/uris/host_ajubuntu__40921
/roslaunch/uris/host_ajubuntu__41167
/roslaunch/uris/host_ajubuntu__42653
/roslaunch/uris/host_ajubuntu__45927
/rosversion
/run_id


    ```

## Package and Dependencies
11. Use the ROS command `rospack depends1` to list the immediate (direct) dependencies of `crazy_turtle`
   The output of the command looks like
   ```
rospy
message_runtime
turtlesim

   ```
12. Use the ROS command `rosservice list` to list the types of services defined by `crazy_turtle`
    The output of the command looks like
    ```
/clear
/kill
/mover/get_loggers
/mover/set_logger_level
/reset
/roaming_turtle/get_loggers
/roaming_turtle/set_logger_level
/rosout/get_loggers
/rosout/set_logger_level
/spawn
/switch
/turtle1/set_pen
/turtle1/teleport_absolute
/turtle1/teleport_relative
    ```
## Live Interaction
13. Use the ROS command `rosservice call /switch [2,3,5,1,1]` to call the `/switch` service.
    The command returns `x: 2 y: 3` and the turtle 'moves to location (2,3) and starts moving again'.
    (Hint: use `rossrv info` on the type of the `/switch` service to see the parameters.
     To test the behavior, look at the code or try calling with `x = 1`, `y = 1`, once with `linear_velocity = 0` and `angular_velocity = 0` and once with these at different nonzero values.)
14. What is the value of the `/mover/velocity` parameter? '5'
15. What happens to the turtle if you change `/mover/velocity` to 10? 'Nothing'
16. Use the ROS command `rosnode kill /mover` to kill the `/mover` node.
17. Use the ROS command `<command and args>` to start the `/mover` node. Be sure to
    remap `cmd_vel` to `/turtle1/cmd_vel`.
18. What happened to the turtle's velocity after relaunching `mover`? Nothing.
