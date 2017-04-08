import pytest

from fixtures.pulse_api_client import PulseRestAPI


@pytest.fixture()
def app():
    return PulseRestAPI("books")