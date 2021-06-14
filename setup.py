import setuptools 
from setuptools.command.install import install
import os

class PostInstall(install):
	def run(self):    
		print("Conseguindo modelo.")
		os.system('dvc get https://github.com/felipedocket/test-tasg.git tree2.jpg')

setuptools.setup(
	name='test_tasg',
	version='0.0.1',
	description='Hello world',
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	packages=setuptools.find_packages(),
	cmdclass={'install': PostInstall},
)

_post_install()