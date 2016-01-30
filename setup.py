import setuptools

from src.version import __VERSION_STR__


setuptools.setup(
    name='powser',
    version=__VERSION_STR__,
    description=(
        'Front-end package manager inspired by bower utilizing cdnjs. '
        'See https://github.com/JDeuce/powser for more.'
    ),
    author='Josh Jaques',
    author_email='jjaques@gmail.com',
    url='https://github.com/JDeuce/powser',
    py_modules=['src'],
    install_requires=open('requirements.txt').read().splitlines(),
    license='MIT License',
    zip_safe=False,
    keywords='front-end package management cdnjs bower',
    classifiers=[],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'powser = src.main:main'
        ]
    }
)
