from setuptools import setup, find_packages
from pathlib import Path


scripts_dir = [f.as_posix() for f in Path('./bin').iterdir()]

setup(
    name='cb_scripts',
    description='Python Scripts that I am working on.',
    url='https://github.com/christopher-burke/python-scripts',
    author='Christopher Burke',
    license='MIT',
    version='0.1dev',
    packages=find_packages(),
    scripts=scripts_dir,
    include_package_data=True,
    zip_safe=False,
)
