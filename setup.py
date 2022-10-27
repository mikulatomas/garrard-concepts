from setuptools import setup, find_packages

from garrard_concepts import __version__, __author__, __email__

setup(
    name="garrard_concepts",
    version=__version__,
    description="",
    long_description="",
    url="https://github.com/mikulatomas/garrard-concepts",
    author=__author__,
    author_email=__email__,
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
    classifiers=["Development Status :: 1 - Planning"],
    include_package_data=True,
)
