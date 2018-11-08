from setuptools import setup
from pathlib import Path


scripts_dir = [f.as_posix() for f in Path('./bin').iterdir()]

setup(
    name='cb_scripts',
    description='Python Scripts that I am working on.',
    url='https://github.com/christopher-burke/python-scripts',
    author='Christopher Burke',
    license='MIT',

    packages=['cb_scripts'],
    scripts=scripts_dir,
    zip_safe=False,
)
