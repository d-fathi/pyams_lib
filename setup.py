from setuptools import setup, find_packages

setup(
    name="pyams_lib", 
    version="0.1.1", 
    author="Dhiabi.Fathi",
    author_email="dhiabi.fathi@gmail.com",
    description=" Python library for analog and mixed-signal simulation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license_file="LICENSE",
    url="https://github.com/d-fathi/pyams_lib", 
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
    ],
)