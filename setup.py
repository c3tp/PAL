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
    install_requires=[
        'Flask==0.12.2',
        'awscli==1.11.94',
        'PyYAML==3.12',
        'botocore==1.5.57',
        'boto3==1.4.4'
    ],
    entry_points={
        'console_scripts': ['pal=pal.main:run']
    }
)
