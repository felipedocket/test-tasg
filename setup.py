import setuptools 
from setuptools.command.install import install
import os, sys

def main():
	print("Hello world")

long_description = "Tessste"
os.system("echo TESTE")
os.system("dvc get https://github.com/felipedocket/test-tasg.git tree2.jpg")

setuptools.setup(
	name='test_tasg',
	version='0.0.1',
	description=long_description,
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	packages=setuptools.find_packages(),
	entry_points={
        'console_scripts': [
            'main=main:hello',
        ],
    }
)

if __name__ == "__main__":
    main()