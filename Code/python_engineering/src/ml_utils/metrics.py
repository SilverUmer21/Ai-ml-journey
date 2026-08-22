from ml_utils.validation import validate_binary_label

def calculate_accuracy(y_true: list[int], y_pred: list[int]) -> float:
    """Returns the accuracy of the two non-empty, equal-length binary label lists"""

    counts = 0
    range1,range2 = len(y_true), len(y_pred)

    if range1 == 0 or range2 == 0 or range1 != range2:
        raise ValueError("Unequal or Empty lists not allowed")

    for label in y_pred:
        validate_binary_label(label)
    
    for label in y_true:
        validate_binary_label(label)

    for i in range(range1):
        if y_true[i] == y_pred[i]:
            counts+=1

    return counts / range2