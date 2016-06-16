from distutils.core import setup
from setuptools import find_packages

try:
    import six
    # TODO check six.__version__
    additional_requirements = []
except ImportError:
    additional_requirements = ['six>=1.4.1']

with open('README.md') as description:
    long_description = description.read()

setup(
    name='fabricio',
    version='0.2.1',
    author='Rinat Khabibiev',
    author_email='srenskiy@gmail.com',
    packages=list(map('fabricio.'.__add__, find_packages('fabricio'))) + ['fabricio'],
    url='https://github.com/renskiy/fabricio',
    license='MIT',
    description='fabricio',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'Fabric>=1.1,<2.0',
        'cached-property>=1.3,<2.0',
    ] + additional_requirements,
)
