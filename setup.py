from setuptools import setup

setup(
    app=['src/main.py'],
    options={
        "py2app": {
            "includes": ["os", "platform"],
            "arch": "arm64",
        }
    },
)
