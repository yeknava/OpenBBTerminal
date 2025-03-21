import pytest

from bots.economy.indices import indices_command


@pytest.mark.bots
@pytest.mark.vcr
def test_indices_command(mocker, recorder):
    mocker.patch("bots.helpers.uuid_get", return_value="1")
    value = indices_command()

    recorder.capture(value)
