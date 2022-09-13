from setuptools import find_packages
from setuptools import setup

setup(
    name='gps_tools',
    version='1.0.5',
    packages=find_packages(
        include=('gps_tools', 'gps_tools.*')),
)
