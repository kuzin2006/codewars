# https://www.codewars.com/kata/simple-finite-state-machine-compiler/train/python


class FSM(object):
    instr_sequence = {}

    def __init__(self, instructions):
        # Compile instructions string
        for instruction in instructions.split("\n"):
            self.instr_sequence[instruction.split(";")[0].strip()] = (
                    tuple(i.strip() for i in tuple(instruction.split(";")[1].split(','))),
                    instruction.split(";")[2].strip()
                )

    def run_fsm(self, start, sequence):
        # return tuple: (final_state, final_state_output, path)
        final_state = [start, None, [start, ]]
        for operation in sequence:
            final_state = [self.instr_sequence[final_state[0]][0][operation],
                           self.instr_sequence[final_state[0]][1],
                           final_state[2]+[self.instr_sequence[final_state[0]][0][operation]]]
        final_state[1] = self.instr_sequence[final_state[0]][1]

        return tuple(final_state)



instructions = \
'''S1; S1, S2; 9
S2; S1, S3; 10
S3; S4, S3; 8
S4; S4, S1; 0'''

fsm = FSM(instructions)
fsm.run_fsm('S1', [0, 1, 1, 0, 1])
