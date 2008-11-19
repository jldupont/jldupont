from setuptools import setup, find_packages

setup(
    name = "jld",
    version = "0.0.1",
    package_data = {'':['*.*']},
    packages = ['jld',],
    scripts=[ 'backup/scripts/mm','backup/scripts/mm.bat' ],
)