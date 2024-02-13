from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as obj_file:
        requirements=obj_file.readline()
        requirements=[req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name='Diwali Sales Analysis',
    version='0.0.1',
    description='Sales analysis during a festival season in India',
    author='Mohd Faisal Ansari',
    author_email='fhrt811@gmail.com',
    intall_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)