from setuptools import setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='UTF-8')


setup(
    name='messari',
    version='0.0.1',
    packages=['messari',
              'messari.messari',
              'messari.defillama'],
    url='',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={'messari': ['mappings/messari_to_dl.json']},
    license='MIT`',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='Roberto Talamas, Michael Kremer',
    author_email='roberto.talamas@gmail.com, kremeremichael@gmail.com',
    description='Messari API'
)
