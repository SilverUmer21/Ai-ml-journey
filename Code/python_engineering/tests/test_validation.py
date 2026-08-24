from ml_utils import validate_binary_label
import pytest 

def test_binary_label_works() -> None:
    actual = validate_binary_label(0)
    assert actual is None

def test_binary_label_raises_error() -> None:
    with pytest.raises(ValueError, match = "Label is not"):
        validate_binary_label(2)
