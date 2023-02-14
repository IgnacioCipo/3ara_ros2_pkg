from setuptools import setup

package_name = '3ara_ros2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cipo',
    maintainer_email='ignaciojcipolatti@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = 3ara_ros2_pkg.publisher:main',
            'publishToSTM32 = 3ara_ros2_pkg.publishToSTM32:main',
        ],
    },
)
