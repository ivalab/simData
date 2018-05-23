# simData
sketchup 3D model from 3D warehouse, compatible with UMD affordance dataset

------------------------------------
## view in Gazebo (gui)

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

## add/delete in Gazebo (script)

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

## connect ROS to Gazebo kinect
please follow [this post](http://gazebosim.org/tutorials?tut=ros_depth_camera&cat=connect_ros#UseaGazeboDepthCamerawithROS)

## change color of model for affordance ground truth
1. go to [sketchup](https://www.sketchup.com/products/sketchup-free)
2. insert the model 
3. right click on the model part if needed and select the color to change
4. resize if needed
5. upload the model in order to conver a .dae format for free


## sketchup tips
### online version
1. left side: paint, move (click on it to select scale)
2. right side: instructor for tips
3. right click for detailed component

### pro version
1. download the pro version (30 days, we should get it done much faster than that)
2. [tools on surface](http://www.thesketchupessentials.com/toolsonsurface) to draw lines on surface to separate surfaces for painting
3. you will need to install LibFredo (hint will pop out when installing tools on surface)
4. to install extension, click on the windows->extension manager, restart sketchup 
5. with pro version, you don't have to upload and download (such a waste of time); to name it, model.dae / model_gt.dae



