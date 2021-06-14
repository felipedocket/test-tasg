import setuptools 
import os

print("Instalando pacote test-tag")

setuptools.setup(
	name='test_tasg',
	version='0.0.1',
	description='Hello world',
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	packages=setuptools.find_packages(),
)

os.system('dvc get https://github.com/felipedocket/test-tasg.git tree2.jpg')