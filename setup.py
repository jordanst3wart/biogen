from setuptools import setup, find_packages

setup(
    name='biogen',
    description='Generate Versent Bios from YAML',
    author='Andrew Ivins',
    author_email='andrew.ivins@versent.com.au',
    url='https://gitlab.com/aivins/biogen',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['biogen=biogen.main:main']
    },
    install_requires=[
        'pyaml',
        'docxtpl'
    ],
    include_package_data=True,
    package_data={
        'biogen': [
            'templates/consultant.docx'
        ]
    }
)

