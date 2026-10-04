from typing import Tuple

import numpy as np


class ImagePreprocessor:
    def __init__(self, target_size: Tuple[int, int] = (640, 640)) -> None:
        pass

    def letterbox(self, frame: np.ndarray) -> np.ndarray:
        pass

    def normalize(self, frame: np.ndarray) -> np.ndarray:
        pass

    def process(self, frame: np.ndarray) -> np.ndarray:
        pass
