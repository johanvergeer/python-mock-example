from unittest.mock import Mock

from python_mock_example.car import Car
from python_mock_example.driver import Driver


def test_create_instance() -> None:
    car_mock = Mock(spec=Car)
    driver = Driver(car_mock)

    assert driver._car == car_mock


# TODO Test unlock

# TODO Test lock
