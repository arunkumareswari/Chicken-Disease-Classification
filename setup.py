from setuptools import find_packages, setup

setup(
    name = "Chicken-Disease-Classification",
    version = "0.0.0",
    author = "Arun kumar",
    author_email ="",
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    install_requires = []
)