from setuptools import setup, find_packages

setup(
    name='lol-recent-match',
    version='0.1.0',
    author='Xiaoteng',
    author_email='lyuxiaot@gmail.com',
    packages=find_packages(),
    description='A CLI tool to fetch recent matches in League of Legends.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'click',
        'configparser',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lol-recent-match = lol_recent_match.cli:cli'
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
