from renderer import Renderer
from utils import Execution_state


class Chip8:
    rendeder: Renderer
    memory: []
    state: Execution_state
    registry: []
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
        self.state = Execution_state.READY.value
        self.execution_speed = 10
        self.program_counter = 0x200

    def _cpu_cycle(self) -> None:
        if self.state == Execution_state.PAUSED.value:
            return

        opcode = self.memory[self.program_counter] << 8 | self.memory[self.program_counter + 1]
        self._execute_instruction(opcode)
        self.program_counter += 0x200

    def _execute_instruction(opcode: int):

        x = (opcode & 0xF00) >> 8

        y = (opcode & 0xF0) >> 8

        opcode_execution[opcode & 0xF00](x, y)


if __name__ == "__main__":
    Chip8('input', 'sound_interface', 'renderer')
