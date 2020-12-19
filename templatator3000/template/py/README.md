{{ project_name }}
==================

# Getting started

## Dependencies

* `python3.9`;
* `requirements.txt` for runtime dependencies;
* `requirements.dev.txt` for development dependencies.

Simply run
```sh
virtualenv venv -p python3.9
. ./venv/bin/activate
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

## Running

```sh
make run
RUN_ARGS='--help' make run  # Custom command line arguments
```

## Documentation

Simply run
```sh
make docs
```
This will generate the HTML doc of the project, and the index file should be at
`docs/_build/index.html`.


## Code quality

Don't forget to run
```sh
make
```
to format the code following [black](https://pypi.org/project/black/),
typecheck it using [mypy](http://mypy-lang.org/), and check it using
[pylint](https://pylint.org/), and check for common vulnerabilities using
[bandit](https://pypi.org/project/bandit/).