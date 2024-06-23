from setuptools import setup, find_packages

setup(
    name='lib-nfl',
    version='1.0.0',
    packages=find_packages(),

    author='DDavid701',
    author_email='ddavid701@gmail.com',
    description='NFL is a number formatting library.',
    url='https://github.com/DDavid701/nfl',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    long_description=open('readme.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.10',
)