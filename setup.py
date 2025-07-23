from setuptools import setup, find_packages

setup(
    name='reliefweb',
    version='0.1.0',
    description='Python client library for the ReliefWeb API',
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
