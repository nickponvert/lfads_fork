import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lfads", # Replace with your own username
    version="0.0.1",
    author="Nick Ponvert",
    author_email="nickponvert@gmail.com",
    description="Repackaging LFADS code for use with setup.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nickponvert/models",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache-2.0",
        "Operating System :: OS Independent",
    ],
    python_requires='==2.7.18',
)
