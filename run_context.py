
import uuid
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def generate_run_id():
    """Generate a unique run ID for each execution."""
    return f"run_{uuid.uuid4()}"

class RunContext:
    def __init__(self, run_id=None):
        self.run_id = run_id or generate_run_id()

    def log(self, message):
        logger.info(f"[{self.run_id}] {message}")

    def error(self, message):
        logger.error(f"[{self.run_id}] {message}")

    def as_dict(self):
        return {"run_id": self.run_id}
