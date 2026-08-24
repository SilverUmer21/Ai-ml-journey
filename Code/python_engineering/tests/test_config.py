from ml_utils import TrainingConfig
import pytest
def test_instance_stores_value() -> None:
    config = TrainingConfig(0.1, 1, 0.0)

    assert config.learning_rate == 0.1 

def test_instance_stores_invalid_value() -> None:
    with pytest.raises(ValueError):
        TrainingConfig(0.111, 0)
