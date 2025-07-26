from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='reliefweb',
    version='0.1.1',
    description='Python client library for the ReliefWeb API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Titus Joyson',
    author_email='tj.joyson@gmail.com',
    packages=find_packages(),
    install_requires=['requests'],
    python_requires='>=3.7',
    url='https://reliefweb.int/',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
