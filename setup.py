'''
Setup tools config for installing PAL.
'''

from setuptools import setup, find_packages

setup(
    name='PAL',
    version='0.0.0',
    include_package_data=True,
    description='Prototype abstraction layer over DDN WOS',
    author='Compute Canada',
    url='https://github.com/c3tp/PAL',
    packages=find_packages(),
    install_requires=['Flask'],
    entry_points={fibonacci = pal.main:run}
)