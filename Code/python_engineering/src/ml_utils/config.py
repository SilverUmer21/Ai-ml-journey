from dataclasses import dataclass

@dataclass(frozen = True)
class TrainingConfig:
    learning_rate: float
    epochs: int
    threshold: float = 0.5

    def __post_init__(self):
        if self.learning_rate <
        if self.threshold > 1 or self.threshold < 0 :
            raise ValueError("Threshold must be in range of 0 and 1")

