from setuptools import setup

setup(
    name='cb_scripts',
    description='Python Scripts that I am working on.',
    url='https://github.com/christopher-burke/python-scripts',
    author='Christopher Burke',
    license='MIT',

    packages=['cb_scripts'],
    scripts=['bin/greet'],
    zip_safe=False,
)
