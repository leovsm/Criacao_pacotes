from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Teste-Pacotes",
    version="0.0.1",
    author="Leonardo",
    author_email="leo.vsm@hotmail.com",
    description="Teste de como utilizar pacotes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leovsm/Criacao_pacotes",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)