from enum import Enum

DEFAULT_EXECUTION_SPEED = 10

DEFAULT_START_ADDR = 0x200


class ExecutionState(Enum):
    PAUSED = "PAUSED"
    ACTIVE = "ACTIVE"
    ERROR = "ERROR"
    READY = "READY"
