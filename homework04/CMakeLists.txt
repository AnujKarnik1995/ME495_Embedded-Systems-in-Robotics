cmake_minimum_required(VERSION 2.8.3)
project(homework4)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

################################################################################
# Find catkin packages and libraries for catkin and system dependencies
################################################################################
find_package(catkin REQUIRED COMPONENTS
  move_base_msgs
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
  roscpp
)

################################################################################
# Setup for python modules and scripts
################################################################################

################################################################################
# Declare ROS messages, services and actions
################################################################################

################################################################################
# Declare ROS dynamic reconfigure parameters
################################################################################

################################################################################
# Declare catkin specific configuration to be passed to dependent projects
################################################################################
catkin_package(
  CATKIN_DEPENDS 
  roscpp 
  catkin
  std_msgs
)

################################################################################
# Build
################################################################################
include_directories(
  ${catkin_INCLUDE_DIRS}
)

#add_executable(turtlebot3_diagnostics src/turtlebot3_diagnostics.cpp)
#add_dependencies(turtlebot3_diagnostics ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
#target_link_libraries(turtlebot3_diagnostics ${catkin_LIBRARIES})

################################################################################
# Install
################################################################################
#install(TARGETS turtlebot3_diagnostics
  #RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

#install(PROGRAMS 
 # scripts/create_udev_rules
 # DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
#)

install(PROGRAMS
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
  start_slam.launch

)

#install(FILES 99-turtlebot3-cdc.rules
#  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
#)

catkin_install_python(PROGRAMS
 nodes/nav_node

 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/nodes
 DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/launch
)

################################################################################
# Test
################################################################################
