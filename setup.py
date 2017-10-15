# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='crud',
    version='0.0.1',
    description='Exemplo de Crud e Rotinas',
    long_description=readme,
    author='Rogério Ribeiro',
    author_email='rogerio.rs@gmail.com',
    url='https://github.com/rogrs/pythoncrud',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

