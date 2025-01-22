from setuptools import setup
import os
from glob import glob

package_name = 'damvi'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        #(os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jaeseo Shin',
    maintainer_email='sinjase@gmail.com',
    description='intergration paackage for damvi',
    license='None',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
