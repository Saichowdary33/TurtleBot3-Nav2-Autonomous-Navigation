import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    project_dir = os.path.expanduser(
        '~/TurtleBot3-Nav2-Autonomous-Navigation'
    )

    nav2_dir = get_package_share_directory('nav2_bringup')

    map_file = LaunchConfiguration(
        'map',
        default=os.path.join(project_dir, 'office_map.yaml')
    )

    params_file = LaunchConfiguration(
        'params_file',
        default=os.path.join(project_dir, 'config', 'nav2_params.yaml')
    )

    use_sim_time = LaunchConfiguration(
        'use_sim_time',
        default='True'
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(nav2_dir, 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_file,
            'params_file': params_file,
            'use_sim_time': use_sim_time,
        }.items()
    )

    return LaunchDescription([
        nav2_launch
    ])
