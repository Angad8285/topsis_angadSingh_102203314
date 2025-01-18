# setup.py
from setuptools import setup, find_packages

setup(
    name="topsis_angadSingh_102203314",  # Replace with your desired package name
    version="1.0.0",  # Update the version as needed
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package to perform TOPSIS analysis on datasets.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",  # Replace with your GitHub URL
    packages=find_packages(),
    py_modules=["main"],  # Include the main script
    entry_points={
        "console_scripts": [
            "topsis=topsis:main",  # Command to run the script
        ],
    },
    install_requires=[
        "pandas>=1.0.0",  # Ensure pandas is installed
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
