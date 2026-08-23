from ml_utils import TrainingConfig, calculate_accuracy


def main() -> None:
    config = TrainingConfig(learning_rate=0.5, epochs=5)
    y_true = [0, 1, 0]
    y_pred = [1, 1, 1]
    accuracy = calculate_accuracy(y_true, y_pred)

    print(f"Accuracy: {accuracy}")
    print(config)


if __name__ == "__main__":
    main()
