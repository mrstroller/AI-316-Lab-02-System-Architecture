from typing import Dict, List

import numpy as np


class AlertLogger:
    def __init__(self, log_path: str = 'logs/events.log', alert_dir: str = 'alerts') -> None:
        pass

    def should_alert(self, detections: List[Dict], priority_classes: List[str], threshold: float) -> bool:
        pass

    def save_snapshot(self, frame: np.ndarray) -> str:
        pass

    def log_event(self, detection: Dict) -> None:
        pass

    def send_alert(self, message: str) -> None:
        pass
