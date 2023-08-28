from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirments(file_path: str) -> List[str]:
    requirments = []
    with open(file_path, 'r') as file:
        requirments = file.readlines()
        requirments = [req.replace("\n", "") for req in requirments]

        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)

    return requirments


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Vithurshan',
    author_email='vvithurshan@gmail.com',
    # packages need to be installed
    install_requires=get_requirments('requirement.txt'),
    packages=find_packages()
)
