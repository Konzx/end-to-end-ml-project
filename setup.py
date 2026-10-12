from setuptools import setup, find_packages

def get_requirements(file_path:str)->list[str]:

    '''This function will return the list of requirements'''
    requirements = []

    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="Ankit Kondilkar",
    author_email="kondilkarankit2@gmailcom",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),

)