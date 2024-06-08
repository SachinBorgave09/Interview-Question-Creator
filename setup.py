## To create a local package

from setuptools import find_packages, setup

setup(
    name = "Generative AI Project",
    version='0.0.0',
    author="Sachin Borgave",
    author_email="borgavejs@gmail.com",
    packages=find_packages(),
    install_requires = []
)

