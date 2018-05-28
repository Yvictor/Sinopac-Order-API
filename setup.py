from setuptools import setup, find_packages
from sinotrade._version import get_version 

setup(
    name='sinotrade',
    version=get_version(),
    author='ypochien,Yvictor',
    author_email='ypochien@gmail.com,yvictor3141@gmail.com',
    packages=find_packages(),
    install_requires=["ujson"],
    description='Python Sinopac Trade API'
)