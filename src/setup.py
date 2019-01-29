from setuptools import find_packages
from setuptools import setup

setup(
    name='coding-kata',
    version='1.0.0',
    packages=find_packages(include=('kata*',)),
    include_package_data=True,
    zip_safe=False,
)
