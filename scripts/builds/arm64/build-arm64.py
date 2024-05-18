from setuptools import setup

setup(
    name='Latter-day Texting Tool - arm64',
    app=['../../../main.py'],
    options={
        "py2app": {
            "arch": "arm64",
        }
    },
)
