import setuptools 

print("Instalando pacote test-tag")

setuptools.setup(
	name='test_tasg',
	version='0.0.1',
	description='Hello world',
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	packages=setuptools.find_packages(),
	entry_points={
        'console_scripts': [
            'test_tasg=test_tag.main:hello',
        ],
    }
)