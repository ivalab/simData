# simData
This is the dataset of our RA-L work 'Learning Affordance Segmentation for Real-world Robotic Manipulation via Synthetic Images'. The detector jointly learns detection and affordance map prediction in an unsupervised manner via synthetic data. The original paper can be found [here](https://ieeexplore.ieee.org/abstract/document/8620534). The final version will be updated after publication process.

If you find it helpful for your research, please consider citing:

    @inproceedings{chu2019learning,
      title = {Learning Affordance Segmentation for Real-world Robotic Manipulation via Synthetic Images},
      author = {F. Chu and R. Xu and P. A. Vela},
      journal = {IEEE Robotics and Automation Letters},
      year = {2019},
      volume = {4},
      number = {2},
      pages = {1140-1147},
      DOI = {10.1109/LRA.2019.2894439},
      ISSN = {2377-3766},
      month = {April}
    }
    
------------------------------------
## Usage
Please follow the instructions in [Image Saver](https://github.com/ivalab/simData_imgSaver)   

This repo contains sketchup 3D models from 3D warehouse, compatible with UMD affordance dataset. This dataset is collected for simulation in Gazebo to automatically generate affordance annotations. 

## Download processed dataset 
If you simply want to use the dataset directly:
- [dropbox link](https://www.dropbox.com/s/9a3qoggh96qolj2/SimData_Gazebo.tar.gz?dl=0)

Note: dataset with segmentation/classification/bounding box groundtruth in VOC2012 format 
## View in Gazebo (gui)

1. put the .dae model under `~/.gazebo/models/MODEL_NAME/meshes/`
2. create a `model.config` as below in `~/.gazebo/models/MODEL_NAME/`
```
<?xml version="1.0"?>
<model>
  <version>1.0</version>
  <name>scissors</name>
  <sdf version="1.4">model.sdf</sdf>

  <description>
    A model of for testing
  </description>
</model>
```
3. create a `model.sdf` as below in `~/.gazebo/models/MODEL_NAME/`
```
<?xml version='1.0'?>
<sdf version="1.4">
<model name="MODEL_NAME">
  <pose>0 0 0.0 0 0 0</pose>
  <static>true</static>
    <link name="link">
      <inertial>
        <mass>1.0</mass>
        <inertia> <!-- inertias are tricky to compute -->
          <!-- http://gazebosim.org/tutorials?tut=inertia&cat=build_robot -->
          <ixx>0.083</ixx>       <!-- for a box: ixx = 0.083 * mass * (y*y + z*z) -->
          <ixy>0.0</ixy>         <!-- for a box: ixy = 0 -->
          <ixz>0.0</ixz>         <!-- for a box: ixz = 0 -->
          <iyy>0.083</iyy>       <!-- for a box: iyy = 0.083 * mass * (x*x + z*z) -->
          <iyz>0.0</iyz>         <!-- for a box: iyz = 0 -->
          <izz>0.083</izz>       <!-- for a box: izz = 0.083 * mass * (x*x + y*y) -->
        </inertia>
      </inertial>
      <collision name="collision">
        <geometry>
          <box>
            <size>1 1 1</size>
          </box>
        </geometry>
      </collision>
      <visual name="visual">
        <geometry>
          <mesh>
            <uri>model://MODEL_NAME/meshes/model.dae</uri>
            <scale>0.001 0.001 0.001</scale>
          </mesh>
        </geometry>
      </visual>
    </link>
  </model>
</sdf>
```
4. open Gazebo `roscore` & `rosrun gazebo_ros gazebo` and you can insert the model

## Add/Delete in Gazebo (script)

1. follow step 1&2&3 as above to prepare the model
2. open an empty world `roscore` & `rosrun gazebo_ros gazebo`
3. add model
```
rosrun gazebo_ros spawn_model -sdf -z 1 -file /home/USERNAME/.gazebo/models/MODEL_NAME/model.sdf -model MODEL_NAME
```
4. delete model
```
rosservice call gazebo/delete_model '{model_name: MODEL_NAME}'
```

arg in spawn_model can be used to specify 6DOF of the position for placing

## Connect ROS to Gazebo kinect
please follow [this post](http://gazebosim.org/tutorials?tut=ros_depth_camera&cat=connect_ros#UseaGazeboDepthCamerawithROS)


## Contact
If you encounter any questions, please contact me at fujenchu[at]gatech[dot]edu

