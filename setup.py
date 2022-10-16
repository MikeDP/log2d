# Auto-generated by easyPyPI: https://github.com/PFython/easypypi
# Preserve current formatting to ensure easyPyPI compatibility.

from pathlib import Path
from setuptools import find_packages
from setuptools import setup

NAME = "log2d"
GITHUB_USERNAME = "PFython"
VERSION = "0.0.12"
DESCRIPTION = "Simple, sane, and sensible logging"
LICENSE = "MIT License"
AUTHOR = "Peter Fison"
EMAIL = "peter@awsom.solutions"
URL = "https://github.com/PFython/log2d"
KEYWORDS = "Logging, Logger, Output, Log,"
CLASSIFIERS = "Development Status :: 4 - Beta, Intended Audience :: Developers, Operating System :: OS Independent, Programming Language :: Python :: 3.10, Programming Language :: Python :: 3.6, Programming Language :: Python :: 3.7, Programming Language :: Python :: 3.8, Programming Language :: Python :: 3.9, Topic :: Internet, Topic :: Internet :: Log Analysis, Topic :: Internet :: WWW/HTTP, Topic :: Internet :: WWW/HTTP :: Session, Topic :: Security, Topic :: Software Development, Topic :: Software Development :: Bug Tracking, Topic :: Software Development :: Debuggers, Topic :: Software Development :: Libraries :: Python Modules, Topic :: Software Development :: Testing, Topic :: System, Topic :: System :: Logging, Topic :: System :: Monitoring, Topic :: System :: Networking, Topic :: Utilities, License :: OSI Approved :: MIT License"
REQUIREMENTS = ""


def comma_split(text: str):
    """
    Returns a list of strings after splitting original string by commas
    Applied to KEYWORDS, CLASSIFIERS, and REQUIREMENTS
    """
    if type(text) == list:
        return [x.strip() for x in text]
    return [x.strip() for x in text.split(",")]


if __name__ == "__main__":
    setup(
        name=NAME,
        packages=find_packages(),
        version=VERSION,
        license=LICENSE,
        description=DESCRIPTION,
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=EMAIL,
        url=URL,
        download_url=f"{URL}/archive/{VERSION}.tar.gz",
        keywords=comma_split(KEYWORDS),
        install_requires=comma_split(REQUIREMENTS),
        classifiers=comma_split(CLASSIFIERS),
        package_data={"": ["*.md", "*.json", "*.png", "*.ico"], NAME: ["*.*"]},
    )
