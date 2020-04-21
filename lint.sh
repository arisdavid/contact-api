#!/usr/bin/env sh

pip install flake8 mccabe pep8-naming
flake8
pytest --cov=src/tests