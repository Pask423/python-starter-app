from setuptools import setup

setup(
    name='greeter-service',
    version='1.0',
    packages=['api'],
    entry_points={
        'console_scripts': [
            'greeter-service = api.main:start',
        ]
    }
)
