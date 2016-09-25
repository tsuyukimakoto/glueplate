from setuptools import setup, find_packages
setup(
    name = "GluePlate",
    version = "0.9",
    packages = find_packages(),
    #scripts = ['say_hello.py'],

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    #install_requires = ['docutils>=0.3'],

    #package_data = {
    #    # If any package contains *.txt or *.rst files, include them:
    #    '': ['*.txt', '*.rst'],
    #    # And include any *.msg files found in the 'hello' package, too:
    #    'hello': ['*.msg'],
    #}

    # metadata for upload to PyPI
    author = "makoto tsuyuki",
    author_email = "mtsuyuki@gmail.com",
    description = "Settings framework for framework or library.",
    license = "MIT",
    keywords = "settings config framework",
    url = "https://github.com/tsuyukimakoto/glueplate",   # project home page, if any
    test_suite = 'nose.collector'
    # could also include long_description, download_url, classifiers, etc.
)
