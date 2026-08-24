from ml_utils import validate_binary_label

def test_binary_label_works() -> None:
    actual = validate_binary_label(0)
    assert actual is None
