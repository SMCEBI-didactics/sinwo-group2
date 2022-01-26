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
            'Gauss = Liczby_pseudolosowe.main:RandomNumberGeneratorGauss',
            'Uniform = Liczby_pseudolosowe.main:RandomNumberGeneratorUniform',
            'Neumann = Liczby_pseudolosowe.main:RandomNumberGeneratorNeumann',
        ]
    }
)

