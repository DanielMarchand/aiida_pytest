import pytest
from fsc.export import export

@export
@pytest.fixture
def assert_outputs_equal():
    def inner(output1, output2):
        def normalize_output(output):
            return {key: value.uuid for key, value in output.items()}
        assert normalize_output(output1) == normalize_output(output2)
    return inner
