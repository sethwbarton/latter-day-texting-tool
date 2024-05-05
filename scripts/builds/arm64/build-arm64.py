from setuptools import setup

setup(
    name='Latter-day Texting Tool - arm64',
    app=['../../../src/main.py'],
    options={
        "py2app": {
            "arch": "arm64",
        }
    },
)
