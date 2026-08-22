def validate_binary_label(label: int) -> None:
    """Raise ValueError when label is not 0 or 1"""
    if label not in (0,1):
        raise ValueError("Label is not 0 or 1")