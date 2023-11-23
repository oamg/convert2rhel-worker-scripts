from mock import patch, mock_open
from scripts.preconversion_assessment_script import get_rhel_version


@patch("__builtin__.open", mock_open(read_data='ID="centos"\nVERSION_ID="7"\n'))
def test_get_rhel_version_with_existing_file():
    distribution_id, version_id = get_rhel_version()

    assert distribution_id == "centos"
    assert version_id == "7"


@patch("__builtin__.open")
def test_get_rhel_version_with_missing_file(mock_open_file):
    mock_open_file.side_effect = IOError("Couldn't read /etc/os-release")

    distribution_id, version_id = get_rhel_version()

    assert distribution_id is None
    assert version_id is None
