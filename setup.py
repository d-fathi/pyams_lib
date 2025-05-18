from setuptools import setup, find_packages



setup(
    name="pyams_lib",
    version="0.2.1",
    author="Dhiabi.Fathi",
    author_email="dhiabi.fathi@gmail.com",
    description="Simulation modeling of analog, digital and mixed-signal electronic elements and circuits",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license_file="LICENSE",
    url="https://github.com/d-fathi/pyams_lib",
    packages=find_packages(),
    include_package_data=True, 
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    keywords=[
        "simulation", "circuit", "electronics", "mixed-signal", 
        "analog", "EDA", "electronic modeling", "electrical engineering"
    ],
    project_urls={
        "Website": "https://pyams-lib.readthedocs.io/", #"https://pyams.sf.net",
        "Source": "https://github.com/d-fathi/pyams_lib",
        "Documentation": "https://pyams-lib.readthedocs.io/",
        "Bug Tracker": "https://github.com/d-fathi/pyams_lib/issues",
        "Support": "https://github.com/d-fathi/pyams_lib/discussions",
        "Donate": "https://ko-fi.com/pyams"
    }
)
