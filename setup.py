import setuptools 
import os

def _post_install():    
	os.system('dvc get https://github.com/felipedocket/test-tasg.git tree2.jpg')

setuptools.setup(
	name='test_tasg',
	version='0.0.1',
	description='Hello world',
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	packages=setuptools.find_packages(),
)

_post_install()