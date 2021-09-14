from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.6.5'
DESCRIPTION = 'Encrypt your crucial data into Image file'
LONG_DESCRIPTION = 'A package that allows to hide and read crucial data from Image files.'

# Setting up
setup(
    name="piencrypt",
    version=VERSION,
    author="Throttlerz (Siddhartha Roy)",
    author_email="<sid86harth@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'image processing', 'encrypt',
              'decrypt', 'hide messages', 'data store'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
