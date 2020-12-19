SRC_PATH	= templatator3000

.ONESHELL:

all: format typecheck

.PHONY: format
format:
	black --line-length 79 --target-version py38 $(SRC_PATH)

.PHONY: typecheck
typecheck:
	mypy -p $(SRC_PATH)
