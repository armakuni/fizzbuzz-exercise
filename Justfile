# This help screen
show-help:
  @just --list --unsorted

# Just run the tests for the "fizz" scenario
fizz-test:
  poetry run python -m pytest -m fizz

# Just run the tests for the "buzz" scenario
buzz-test:
  poetry run python -m pytest -m buzz

# Just run the tests for the "fizzbuzz" scenario
fizzbuzz-test:
  poetry run python -m pytest -m fizzbuzz

# Run all the tests
test:
  poetry run python -m pytest

# Format the code
format:
  poetry run black .
  poetry run isort .

# Run basic linting against the code
lint:
  poetry run black --check .
  poetry run isort --check .
  poetry run flake8p .

alias fmt := format
