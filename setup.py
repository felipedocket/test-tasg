from setuptools import setup

print("Instalando pacote test-tag")

setup(
	name='test_tasg',
	version='0.0.1',
	description='Hello world',
	py_modules=[''],
	url='https://github.com/felipedocket/test-tasg',
	entry_points={
        'console_scripts': [
            'test_tasg=test_tag.main:hello',
        ],
    }
)