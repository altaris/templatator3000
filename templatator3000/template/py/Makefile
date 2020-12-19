SRC_PATH 		= {{ project_name }}
SPHINX_PATH 	= docs
VENV			= ./venv
RUN_ARGS	   ?=
RUN				= python3 -m $(SRC_PATH) $(RUN_ARGS)

.ONESHELL:

all: format typecheck lint bandit

.PHONY: bandit
bandit:
	bandit --format custom --quiet --recursive $(SRC_PATH)

.PHONY: command-line-args
command-line-args:
	$(RUN) --help > $(SPHINX_PATH)/command-line-args.txt

.PHONY: docs
docs: docs_uml command-line-args configuration-spec  # openapi-spec
	sphinx-build -b html $(SPHINX_PATH)/ $(SPHINX_PATH)/_build

.PHONY: format
format:
	black --line-length 79 --target-version py38 $(SRC_PATH)

.PHONY: lint
lint:
	pylint $(SRC_PATH)

.PHONY: run
run:
	@set -a
	@. $(VENV)/bin/activate
	$(RUN)

.PHONY: typecheck
typecheck:
	mypy -p $(SRC_PATH)
