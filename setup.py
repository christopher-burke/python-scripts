from setuptools import setup, find_packages
from pathlib import Path


scripts_dir = [f.as_posix() for f in Path('./bin').iterdir()]

with open('README.md', "r", encoding='utf-8') as file_handler:
    long_description = file_handler.read()

setup(
    name='cb_scripts',
    version='0.1dev',
    author="Christopher Burke",
    description='Python Scripts that I am working on.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/christopher-burke/python-scripts',
    project_urls={
        "Bug Tracker": "https://github.com/christopher-burke/python-scripts/issues"
    },
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    scripts=scripts_dir,
    # include_package_data=True,
    package_data={
        'data': ['*'],
    },
    zip_safe=False,
)
