# ft_package

A test package to learn how to create a publishable python package.

## build
### project structure
```shell
.
├── LICENSE
├── README.md
├── pyproject.toml
├── src
│   └── ft_package
│       ├── __init__.py
│       └── count_in_list.py
└── tester.py
```

**LICENSE:** A text file which indicates the user's permissions and the developer's liabilities and warranties. In this case, an MIT license was used.  
**pyproject.toml:** specifies certain metadata like dependencies, package name, python version, etc...  
**src:** contains the actual source code of the package.


### build backend
A build backend is the software responsible for building the artifacts which can then be installed as python packages.

In this case, uv build backend was used.

```shell
$ uv init --package
```

### build front end
A build frontend is a user friendly interface to the `build backend`.  In this case, uv itself serves as the build frontend.

```shell
$ uv build
```

This operation results in a `dist` folder which has the distribution files:

```shell
$ ./dist/ft_package-0.0.1.tar.gz
$ ./dist/ft_package-0.0.1-py3-none-any.whl
```

The first one is a [Source Distribution](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package), when we attempt to install it with pip, it builds it first, then installs it.  
The second one is a [Built Distribution](https://packaging.python.org/en/latest/glossary/#term-Built-Distribution) which is readdy to install.

## Installation

run either of the following:
```shell
$ pip install ./dist/ft_package-0.0.1.tar.gz
$ pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

To uninstall the package, simply run
```shell
$ pip uninstall ft_package
```

To show package details, run
```shell
$ pip show -v ft_package
```
