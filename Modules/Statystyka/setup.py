from setuptools import setup

setup(
    name="Statystyka",
    description="Moduł z wybranymi elementami statystyki",
    version="v1.0",
    author="Adam Wowra",
    author_email="",
    licence="MIT",
    install_requires=["click"],
    packages=['Statystyka'],
    entry_points={
        'console_scripts': [
            'srednia = Statystyka.main:srednia',
            'mediana = Statystyka.main:mediana',
            'odchylenie = Statystyka.main:odchylenie',
            'regresjaliniowa = Statystyka.main:regresjaliniowa',
            'korelacja = Statystyka.main:korelacja',
            'testshapiro = Statystyka.main:testshapiro'
        ]
    }
)
