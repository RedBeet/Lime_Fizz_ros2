# Copyright (C) 2021, Raffaello Bonghi <raffaello@rnext.it>

from setuptools import setup
# Launch command
from os import path
from glob import glob

package_name = 'nanosaur_hardware'

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['requirements.txt']),
        (path.join('share', package_name), glob('launch/*.py'))
    ],
    install_requires=requirements,
    zip_safe=True,
    maintainer='Raffaello Bonghi',
    maintainer_email='raffaello@rnext.it',
    description='Basic drivers for NanoSaur, motors and displays',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'nanosaur = nanosaur_hardware.nanosaur:main'
        ],
    },
)
