from setuptools import setup

setup(
    name='Latter-day Texting Tool - x86',
    app=['../../../main.py'],
    options={
        "py2app": {
            "arch": "x86_64",
        }
    },
)
