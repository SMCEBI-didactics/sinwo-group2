from setuptools import setup

setup(
    name="Liczby_pseudolosowe",
    description="Generuje liczby pseudolosowe przy pomocy roznych metod",
    version="v1.0",
    author="Adam Martyniak",
    author_email="",
    licence="MIT",
    install_requires=["click"],
    packages=['Liczby_pseudolosowe'],
    entry_points={
        'console_scripts' : [
            'Losoj = Liczby_pseudolosowe.main:main'
        ]
    }
)

