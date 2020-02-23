import re
from pathlib import Path

from setuptools import setup, find_packages


def find_version():
    version_file = (
        Path(__file__)
        .parent.joinpath("pytest_virtualtime", "__init__.py")
        .read_text()
    )
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version string.")


setup(
    name="pytest-virtualtime",
    version=find_version(),
    packages=find_packages(),
    url="https://github.com/semiversus/python-virtualtime",
    license="MIT",
    author="Günther Jena",
    author_email="guenther@jena.at",
    description=" VirtualTimeEventLoop replaces asyncio eventloop and allows the testing time be different from wall-clock time ",
    long_description=Path(__file__).parent.joinpath("README.rst").read_text(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Testing",
        "Framework :: Pytest",
    ],
    python_requires=">= 3.5",
    install_requires=["pytest >= 3.6.0", "pytest-asyncio >= 0.10.0"],
    entry_points={"pytest11": ["virtualtime = pytest_virtualtime.plugin"]},
)
