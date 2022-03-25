'''
Test utility functions.
'''

from datetime import datetime, timezone

from nfsops import utils


def test_timezone_aware_should_return_same_timezone_aware_datetime_with_timezone_aware_datetime_parameter():  # pylint: disable=C0301
    '''
    Test converting naive to timezone-aware datetime (UTC timezone)
    with timezone-aware datetime parameter.

    Raises:
        AssertionError: Expected value does not match the returned value.
    '''

    expected_datetime = datetime.now(tz=timezone.utc)
    actual_datetime = utils.timezone_aware(expected_datetime)

    assert actual_datetime == expected_datetime


def test_timezone_aware_should_return_new_timezone_aware_datetime_with_naive_timezone_datetime_parameter():  # pylint: disable=C0301
    '''
    Test converting naive to timezone-aware datetime (UTC timezone)
    with naive datetime parameter.

    Raises:
        AssertionError: Expected value does not match the returned value.
    '''

    input_datetime = datetime.now()
    expected_datetime = input_datetime.replace(tzinfo=timezone.utc)
    actual_datetime = utils.timezone_aware(input_datetime)

    assert actual_datetime == expected_datetime
