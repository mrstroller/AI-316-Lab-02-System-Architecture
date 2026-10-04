from typing import Dict, List

import numpy as np


class ModelInferenceEngine:
    def __init__(self, model_path: str = 'yolov8n.pt', conf_threshold: float = 0.5) -> None:
        pass

    def load_model(self) -> None:
        pass

    def predict(self, frame: np.ndarray) -> List[Dict]:
        pass

    def get_class_names(self) -> Dict[int, str]:
        pass
