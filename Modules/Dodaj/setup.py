from setuptools import setup

setup(
    name="Dodaj",
    description="dodaje 2 liczny",
    version="v1.0",
    author="Albert Szadziński",
    author_email="",
    licence="MIT",
    install_requires=["Click"],
    packages=['Dodaj'],
    entry_points={
        'console_scripts' : ['dodaj = Dodaj.main:main']
    }
)

