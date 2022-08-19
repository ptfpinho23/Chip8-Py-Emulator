from typing import List

from cpu import OPCODE_EXECUTION
from renderer import Renderer
from utils import DEFAULT_EXECUTION_SPEED, DEFAULT_START_ADDR, ExecutionState


class Chip8:
    rendeder: Renderer
    memory: List[int]
    state: ExecutionState
    registry: List[int]
    current_memory_address = int
    program_counter: int
    delay_timer: int
    sound_timer: int
    execution_speed: int

    def __init__(self, input, sound_interface, renderer):
        self.renderer = renderer
        self.input = input
        self.sound_interface = sound_interface
        self.memory = bytearray(4096)
        self.registry = bytearray(16)
        self.state = ExecutionState.READY.value
        self.execution_speed = DEFAULT_EXECUTION_SPEED
        self.program_counter = DEFAULT_START_ADDR

    def _cpu_cycle(self) -> None:
        if self.state == ExecutionState.PAUSED.value:
            return

        opcode = (
            self.memory[self.program_counter] << 8
            | self.memory[self.program_counter + 1]
        )
        self._execute_instruction(opcode)
        self.program_counter += 0x200

    def _execute_instruction(opcode: int):

        x = (opcode & 0xF00) >> 8

        y = (opcode & 0xF0) >> 8

        OPCODE_EXECUTION[opcode & 0xF00](x, y)


if __name__ == "__main__":
    Chip8("input", "sound_interface", "renderer")
