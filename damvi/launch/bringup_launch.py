from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch_xml.launch_description_sources import XMLLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    joy_teleop_config = os.path.join(
        get_package_share_directory('f1tenth_stack'),
        'config',
        'joy_teleop.yaml'
    )
    vesc_config = os.path.join(
        get_package_share_directory('f1tenth_stack'),
        'config',
        'vesc.yaml'
    )
    sensors_config = os.path.join(
        get_package_share_directory('f1tenth_stack'),
        'config',
        'sensors.yaml'
    )
    mux_config = os.path.join(
        get_package_share_directory('f1tenth_stack'),
        'config',
        'mux.yaml'
    )

    joy_la = DeclareLaunchArgument(
        'joy_config',
        default_value=joy_teleop_config,
        description='Descriptions for joy and joy_teleop configs')
    vesc_la = DeclareLaunchArgument(
        'vesc_config',
        default_value=vesc_config,
        description='Descriptions for vesc configs')
    sensors_la = DeclareLaunchArgument(
        'sensors_config',
        default_value=sensors_config,
        description='Descriptions for sensor configs')
    mux_la = DeclareLaunchArgument(
        'mux_config',
        default_value=mux_config,
        description='Descriptions for ackermann mux configs')

    ld = LaunchDescription([joy_la, vesc_la, sensors_la, mux_la])
    
    rf_input_node = Node(
        package='rf_joy',
        executable='rf_publisher_node',
        name='rf_publisher_node',
        output='screen'
    )

    rf_joy_node = Node(
        package='rf_joy',
        executable='rf_to_joy_node',
        name='rf_to_joy_node',
        output='screen'
    )

    joy_node = Node(
        package='joy',
        executable='joy_node',
        name='joy',
        parameters=[LaunchConfiguration('joy_config')]
    )
    joy_teleop_node = Node(
        package='joy_teleop',
        executable='joy_teleop',
        name='joy_teleop',
        parameters=[LaunchConfiguration('joy_config')]
    )
    ackermann_to_vesc_node = Node(
        package='vesc_ackermann',
        executable='ackermann_to_vesc_node',
        name='ackermann_to_vesc_node',
        parameters=[LaunchConfiguration('vesc_config')]
    )
    vesc_driver_node = Node(
        package='vesc_driver',
        executable='vesc_driver_node',
        name='vesc_driver_node',
        parameters=[LaunchConfiguration('vesc_config')]
    )
    urg_node = Node(
        package='urg_node',
        executable='urg_node_driver',
        name='urg_node',
        parameters=[LaunchConfiguration('sensors_config')]
    )
    ackermann_mux_node = Node(
        package='ackermann_mux',
        executable='ackermann_mux',
        name='ackermann_mux',
        parameters=[LaunchConfiguration('mux_config')],
        remappings=[('ackermann_cmd_out', 'ackermann_drive')]
    )
    static_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='static_baselink_to_laser',
        arguments=['0.27', '0.0', '0.11', '0.0', '0.0', '0.0', 'base_link', 'laser']
    )
    tf_publisher_node = Node(
    	package='f1tenth_stack',
        executable='tf_publisher',
        name='tf_publisher',
        parameters=[LaunchConfiguration('vesc_config')]
    )
    drive_publisher_node = Node(
    	package='f1tenth_stack',
        executable='drive_publisher',
        name='drive_publisher',
        parameters=[LaunchConfiguration('mux_config')]
    )    
    
    # finalize
    ld.add_action(joy_node)
    ld.add_action(joy_teleop_node)
    ld.add_action(ackermann_to_vesc_node)
    ld.add_action(rf_input_node)
    ld.add_action(rf_joy_node)
    ld.add_action(vesc_driver_node)

    ld.add_action(urg_node)
    ld.add_action(ackermann_mux_node)
    ld.add_action(static_tf_node)
    ld.add_action(tf_publisher_node)
    ld.add_action(drive_publisher_node)

    return ld
