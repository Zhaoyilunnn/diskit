from setuptools import setup, find_packages

setup(
    name="diskit",
    version="0.1.0",
    description="A project that can be installed locally.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        # Add your project's dependencies here, e.g.,
        # 'numpy',
        # 'pandas',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
