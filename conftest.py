import pytest

from fixtures.pulse_api_client import PulseRestAPI


@pytest.fixture(scope="session")
def app():
    return PulseRestAPI("books")

