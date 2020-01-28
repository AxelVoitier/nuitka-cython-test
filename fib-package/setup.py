# System imports
import os
import setuptools

# Third-party imports
from Cython.Build import cythonize
USE_CYTHON = True

base_folder = os.path.dirname(os.path.abspath(__file__))

sources = [
    'fib/fib_ext',
]
sources_pyx = []
for source in sources:
    sources_pyx.append(os.path.join(base_folder, source + '.pyx'))

extensions = cythonize(sources_pyx, language_level='3')

setup_args = dict(
    name='fib',
    version='0.0.1',
    packages=setuptools.find_packages(),
    ext_modules=extensions,
    setup_requires=[
        'cython',
    ],
    install_requires=[
    ],
    python_requires='~=3.5',
    entry_points=dict(
        console_scripts=[
            'fib=fib.main:main_fn',
        ],
    ),
)


if __name__ == '__main__':
    setuptools.setup(**setup_args)
