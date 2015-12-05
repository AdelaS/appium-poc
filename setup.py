from setuptools import setup
from pip.req import parse_requirements

requirements = [
    str(ir.req) for ir in parse_requirements('requirements.txt', session=False)
]

setup(
    name='appium-poc',
    version='1.0.0',
    author='Adela Suhani',
    author_email='adela.suhani@gmail.com',
    description='Proof-of-concept for automated testing using Appium.',
    install_requires=requirements
)
