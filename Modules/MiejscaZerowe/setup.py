from setuptools import setup

setup(
    name="MiejscaZerowe",
    description="Zawiera funkcje do wyznaczania miejsc zerowych",
    version="v1.0",
    author="Oliwier Pszeniczko",
    author_email="",
    licence="MIT",
    install_requires=["click"],
    packages=['MiejscaZerowe'],
    entry_points={
        'console_scripts': [
            'metoda_bisekcji = Dekoder.main:metoda_bisekcji',
            'metoda_siecznych = Dekoder.main:metoda_siecznych',

        ]
    }
)
