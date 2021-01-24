import os
import pathlib

from setuptools import find_packages, setup

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, "src")

here = pathlib.Path(base_dir).resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

packages = find_packages(where='src', include=['aio_rsiapi'])

about = {}
with open(os.path.join(src_dir, "aio_rsiapi", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__summary__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=about["__license__"],
    url=about["__uri__"],
    author=about["__author__"],
    author_email=about["__email__"],

    # Classifiers help users find your project by categorizing it.
    #
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        # How mature is this project? Common values are
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Session',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],

    packages=find_packages(where='src', include=['aio_rsiapi']),
    package_dir={'': 'src'},
    python_requires='>=3.9, <4',
    install_requires=['aiohttp==3.7.3'],
    setup_requires=[],
    tests_require=[],
    test_suite='tests',
)
