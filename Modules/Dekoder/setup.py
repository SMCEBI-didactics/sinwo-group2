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
            'to_bin = Dekoder.main:to_bin',
            'to_hex = Dekoder.main:to_hex',
            'to_base64 = Dekoder.main:to_base64',
            'from_base64 = Dekoder.main:from_base64',
            'hash_md5 = Dekoder.main:hash_md5',
            'hash_sha256 = Dekoder.main:hash_sha256'
        ]
    }
)

