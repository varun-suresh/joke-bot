
from setuptools import (
setup,
find_packages
)

runtime_packages = []

setup(
name = 'joke-bot',
version = '0.0.1',
description = 'A chat bot trained on a jokes dataset.',
author = 'Varun Suresh',
author_email = 'fab.varun@gmail.com',
license = 'MIT',
packages = find_packages(),
install_requires =runtime_packages,
extras_require = {}
)
