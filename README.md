# Python Mock Example

This repository can be used as a base for junior Python developers to practice mocking.

The `Car` class is a `Protocol` without an implementation. 
This is by design because the system under test is the `Driver` class. 

If the developer wants to apply Test Driven Development (TDD) he or she can apply the following steps:

## Testing `Driver.lock`

1. Create a test method in `test_driver.py` that uses a mock to test whether `Car.lock()` is called
1. Run the test and see that it fails.
1. Implement the `Driver.lock()` method so the test method passes.  

## Testing `Driver.unlock`

1. Create a test method in `test_driver.py` that uses a mock to test whether `Car.unlock()` is called
1. Run the test and see that it fails.
1. Implement the `Driver.unlock()` method so the test method passes.  

## Getting started instructions

1. Make sure you have [installed Poetry](https://python-poetry.org/docs/#installation)
1. Clone this repository to your local device.
1. `cd` into the repository and run `poetry install`, this will create a virtual environment for this project.
    1. __PRO TIP:__ Run `poetry config virtualenvs.in-project true` before running `poetry install` so the virtual environment is created inside your project.
1. Run `poetry shell` to activate the virtual environment
1. Run `pytest` to see the first test pass