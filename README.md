# python_lib_sphinx

[![Build Status](https://travis-ci.org/saun4app/python_lib_sphinx.svg?branch=master)](https://travis-ci.org/saun4app/python_lib_sphinx)
[![codecov.io](https://codecov.io/github/hbetts/orbitalpy/coverage.svg?branch=master)](https://codecov.io/github/saun4app/python_lib_sphinx?branch=master)

This is a supplemental example for [`generator-python-lib`](https://github.com/hbetts/generator-python-lib) to crate a Python library with documentation using [`Sphinx`](https://pypi.python.org/pypi/Sphinx).

```bash
$ npm install -g yo
$ npm install -g generator-python-lib
$ mkdir python_lib_sphinx
$ cd python_lib_sphinx
$ virtualenv --python=python3 venv
$ source ./venv/bin/activate
$ yo python-lib
```

Follow the instructions of `yo python-lib`.

```bash
$ python setup.py test
$ python setup.py install
$ mkdir docs
$ cd docs
$ sphinx-quickstart
```

Follow the instructions of `sphinx-quickstart`.

Add `sys.path.insert(0, os.path.abspath('../..'))` to `conf.py` after `sphinx-quickstart` is finished,

```bash
$ sphinx-apidoc -f -o source/ ../python_lib_sphinx/
$ make html
```

The generated documentation is located at `_build/html/index.html`.

## References

- [generator-python-lib](https://github.com/hbetts/generator-python-lib)
- [Sphinx for Python documentation](http://gisellezeno.com/tutorials/sphinx-for-python-documentation.html)


Read [CONTRIBUTING](CONTRIBUTING.md).
