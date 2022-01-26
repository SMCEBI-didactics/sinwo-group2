from setuptools import setup

setup(
    name="LiczbyPierwsze",
    description="Znajduje najwieksza liczbe pierwsza",
    version="v1.0",
    author="Jakub Krukowski",
    author_email="",
    licence="MIT",
    install_requires=["Click"],
    packages=['LiczbyPierwsze'],
    entry_points={
        'console_scripts' : [
            'LiczbyPierwsze = LiczbyPierwsze.main:main'

            ]
    }
)

