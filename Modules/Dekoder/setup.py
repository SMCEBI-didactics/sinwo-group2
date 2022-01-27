from setuptools import setup

setup(
    name="Dekoder",
    description="Zawiera funkcje do dekodowania",
    version="v1.0",
    author="Aleksander Kopeć",
    author_email="",
    licence="MIT",
    install_requires=["click"],
    packages=['Dekoder'],
    entry_points={
        'console_scripts': [
            'decode = Dekoder.main:main'
        ]
    }
)

