from setuptools import find_packages, setup

def _load_requirements(file_name):
    with open(file_name, "r") as file:
        return [line.strip() for line in file.readlines()]

setup(
    name='utaformatix-data',
    version='1.0.1',    
    description='Common data container for singing synthesis softwares.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sdercolin/utaformatix-data',
    author='sdercolin',
    author_email='sder.colin@gmail.com',
    license='Apache-2.0 license',
    packages=find_packages(),
    install_requires=_load_requirements("requirements.txt"),
)