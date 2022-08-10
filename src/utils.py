from enum import Enum

class Execution_state(Enum):
    PAUSED = 'PAUSED'
    ACTIVE = 'ACTIVE'
    ERROR = 'ERROR'
    READY = 'READY'