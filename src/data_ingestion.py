from typing import Optional, Tuple

import numpy as np


class DataIngestion:
    def __init__(self, source: str, width: int = 1280, height: int = 720) -> None:
        pass

    def open(self) -> bool:
        pass

    def is_opened(self) -> bool:
        pass

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        pass

    def release(self) -> None:
        pass
