from setuptools import setup, find_packages

setup(
    name='Topsis-Gazal-102217174',
    version='0.4',
    author='Gazal',
    author_email='2580gazal@gmail.com',
    description='A Python implementation of the TOPSIS method.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pandas', 'numpy'],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main',
        ],
    },
)