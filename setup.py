from setuptools import setup, find_packages
from distutils.command.install import install
import os

class PreInstallClean(install):
    # Calls the default run command, then deletes build directories
    def run(self):
        os.system('rm -rf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        install.run(self)
    
setup(
    name='cli-compiler',
    version='0.1.0',
    author='David Eriksson',
    author_email='david.eriksson@swedenmail.com',
    packages=find_packages(),
    url='http://seppaleinen.github.io/cli-compiler',
    zip_safe=True,
    license='GPLv3',
    description='A terminal based tool for managing vcs and compiling.',
    install_requires=[
        "setuptools==18.5",
        "enum34==1.0.4",
        "click==5.1",
    ],
    tests_require=[
        "pep8==1.6.2",
        "mock==1.3.0",
        "click==5.1",
    ],
    test_suite='tests',
    cmdclass={'install': PreInstallClean},
    entry_points='''
        [console_scripts]
        cli-compiler=your_package.manager:cli 
    ''',
)
