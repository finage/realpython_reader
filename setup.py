"""Setup script for realpython-reader"""

# Standard library imports
import pathlib
import os

# Third party imports
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).resolve().parent

# The text of the README file is used as a description
README = (HERE / "README.md").read_text()

# Variables
package_name = os.environ['PACKAGE_NAME']
build_number = os.environ['BUILD_NUMBER']

# This call to setup() does all the work
setup(
    name="%s"%package_name,
    version="1.0.%s"%build_number,
    description="This is a copy of realpython-reader",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/finage/realpython_reader",
    author="Mykola Copypaster",
    author_email="mykola@test.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["feedparser", "html2text"],
    entry_points={"console_scripts": ["realpython=reader.__main__:main"]},
)
