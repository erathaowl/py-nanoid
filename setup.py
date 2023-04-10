from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='nanoid',
    version='3.0.0',
    author='Erathaowl',
    author_email='erathaowl@gmail.com',
    description='A tiny, secure, URL-friendly, unique string ID generator for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/erathaowl/py-nanoid',
    license='MIT',
    packages=['nanoid'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Topic :: Utilities'
    ],
    zip_safe=False
)
