import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkgPath = launch_ros.substitutions.FindPackageShare(package='urdf_test').find('urdf_test')
    urdfModelPath= os.path.join(pkgPath, 'urdf/urdf_test.urdf')
    
    with open(urdfModelPath,'r') as infp:
    	robot_desc = infp.read()
    
    params = {'robot_description': robot_desc}
    
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[params],
    )
    
    return launch.LaunchDescription([
        
        joint_state_publisher_node,
    ])
