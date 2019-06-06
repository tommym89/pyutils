import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mcneelat-pyutils",
    version="0.1.0",
    description="A collection of helpful Python utilities to simplify dealing with databases, Kafka, and more.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tommym89/pyutils",
    author="Tommy McNeela",
    author_email="mcneelat@gmail.com",
    license="GPLv3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["kafka-python", "psycopg2-binary", "requests"],
)