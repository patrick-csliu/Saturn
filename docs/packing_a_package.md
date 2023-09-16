# Packaging Projects

In the past, `distutils` was usually used to packing python package. After the release of [PEP517](https://peps.python.org/pep-0517/) in 2015-2017, the way to build a package gradually changed. The new tools updated frequently in the past few years. 

## Introduction to Package and Packing

* What is "package" in python?

    [tutorial-package](https://docs.python.org/3/tutorial/modules.html#packages)

* Some concept about distribution: [An Overview of Packaging for Python](https://packaging.python.org/en/latest/overview/)

* Most (near all) of the tools in Python installation and packaging: [Project Summaries](https://packaging.python.org/en/latest/key_projects/#twine).

## Packaging Python Projects

* ### References

    * [Tutorial - Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

    * [Setuptools](https://setuptools.pypa.io/en/latest/setuptools.html)

    * [python packaging](https://drivendata.co/blog/python-packaging-2023)

* ### Demo

    1. Upgrade to latest version
        ```
        $ python -m pip install --upgrade pip
        $ python -m pip install --upgrade build
        ```
    
    1. A project

        * Demo repository zip: [package-release-demo](package-release-demo.zip)

        cd to the working directory
        ```
        package-release-demo/
        ├── LICENSE
        ├── pyproject.toml
        ├── README.md
        ├── requirements.txt
        ├── setup.py
        ├── .github/
        │   └── workflows/
        │       ├── pylint.yml
        │       └── python-app.yml
        └── src/
            └── testpackage/
                ├── run.py
                ├── __init__.py
                ├── c/
                │   └── mydemo.c
                └── test/
                    ├── test.py
                    └── __init__.py
        ```
        > **Note**
        > 
        > There are three types of name in different place, the name of the repository, the name of the directory that contain `__init__.py`, and the name for release.
        > 
        > In this demo, the repository name is `package-release-demo`.
        > The package directory name is `testpackage`, and this name also as import name.
        > The release name is define in `pyproject.toml`
        > ```toml
        > # pyproject.toml
        > [project]
        > name = "pypackage_test"
        > ```
        >

    1. Creating the package files

        1. **[LICENSE](https://choosealicense.com/)**

            This tells users who install your package the terms under which they can use your package.

        1. **[pyproject.toml](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)**

            [Configuring metadata](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/).

            [Configuring setuptools using pyproject.toml files](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html)

        1. **README.md**

            The Readme serves as a guide that explains the purpose of your project, provides instructions for installation, offers guidance on how to use it, and includes information on how to contribute to the project.

        1. **[MANIFEST.in](https://packaging.python.org/en/latest/guides/using-manifest-in/)**

            (optional)
            Including files in source distributions

    1. Generating distribution archives

        ```
        $ python -m build
        ```
        This command should output a lot of text and once completed should generate two files in the dist directory

        The `tar.gz` file is a source distribution whereas the `.whl` file is a built distribution.

## C/C++ extension modules

* [Building Extension Modules](https://setuptools.pypa.io/en/latest/userguide/ext_modules.html)

## Install package

* Install package from the working directory:
    
    `$ pip install .`

    build is not necessary

* Install package from the source distribution:

    `$ pip install pypackage_test-1.2.3.tar.gz`

* Install package from the built distribution:

    `$ pip install pypackage_test-1.2.3-cp311-cp311-win_amd64.whl`

# Release to Public

* PyPI

    ref: [Uploading the distribution archives](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives), [twine](https://twine.readthedocs.io/en/latest/)

* conda

    ref: [Building conda packages](https://conda.io/projects/conda-build/en/latest/user-guide/tutorials/building-conda-packages.html)
