name: Python CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 4
      matrix:
        python-version: ["3.7", "3.8", "3.9", "3.10", "3.11" ]

    steps:
    - uses: actions/checkout@v1
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install tox tox-gh-actions codecov
    - name: Test with tox
      run: tox
    - name: coverage
      if: success()
      run: tox -e coverage-report
    - name: codecov
      if: success()
      run: codecov
