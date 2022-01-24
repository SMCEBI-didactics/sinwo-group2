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
        'console_scripts' : [
            'toBin = Dekoder.main:toBin',
            'toHex = Dekoder.main:toHex',
            'toBase64 = Dekoder.main:toBase64',
            'fromBase64 = Dekoder.main:fromBase64',
            'hashMD5 = Dekoder.main:hashMD5',
            'hashSHA256 = Dekoder.main:hashSHA256'
        ]
    }
)

