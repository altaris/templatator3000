# templatator3000

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

## Code quality

Don't forget to run
```sh
make
```
to format the code following [black](https://pypi.org/project/black/),
typecheck it using [mypy](http://mypy-lang.org/).
