# FizzBuzz exercise

An example repo to introduce python and TDD through the FizzBuzz kata.

## Getting started

```sh
git clone https://github.com/FIL-Enterprise-Prod/TAPP102826-fizzbuzz-exercise.git
cd TAPP102826-fizzbuzz-exercise
# Install deps
poetry install
# Open in vscode
code .
```

**Note**: Feel free to commit your solutions on a branch `git checkout -b <branch_name>` but we want to keep `main` nice and clean for everyone going through the exercise.

## What is fizzbuzz

- When a number is a multiple of 3, then return "Fizz"
- When a number is a multiple of 5, then return "Buzz"
- When a number is both a multiple of 3 and a multiple of 5, then return "FizzBuzz"
- When a number is not a multiple of 3 or 5 then return the number as a string

## The exercise

This repo contains a very basic set of tests to get you started, these are "marked" so that you can easily target a single scenario.

```sh
just fizz-test     # Just run the tests for the "fizz" scenario
just buzz-test     # Just run the tests for the "buzz" scenario
just fizzbuzz-test # Just run the tests for the "fizzbuzz" scenario
just test          # Run all the tests
```

The most basic task is to make all the tests pass (based on the rules described above), we recommend that you run solve them 1 scenerio at a time before running the entire test suite.

In addition to running the tests in order to instill some good practice you can run formatting and linting:

```sh
just format lint
```

Does your code have any linting errors?

## Reflection

- How might you change the tests to make them more resilient
- Did the tests change how you approached the solution?
- Can you change your solution without breaking the tests? What does this mean?
