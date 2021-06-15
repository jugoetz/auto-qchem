from setuptools import setup

setup(
    name='auto-qchem',
    version='0.1',
    packages=['autoqchem'],
    data_files=['config.yml'],
    url='https://github.com/jugoetz/auto-qchem',
    license='GPL',
    author='Julian Götz',
    author_email='jgoetz@ethz.ch',
    description='auto-qchem-lsf-fork',
    install_requires=['numpy',
                      'pandas',
                      'pyyaml',
                      'scipy',
                      'fabric',
                      'paramiko',
                      'pymongo',
                      'appdirs']
)
