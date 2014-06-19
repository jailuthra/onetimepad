from setuptools import setup

setup(
    name='onetimepad',
    
    version='1.1.0',
    description='A hacky implementation of One-time pad',
    
    py_modules=['onetimepad'],

    url='http://jailuthra.in/onetimepad',
    author='Jai Luthra',
    author_email='me@jailuthra.in',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],

    entry_points={
        'console_scripts': [
            'onetimepad = onetimepad:main',
        ],
    },
)
