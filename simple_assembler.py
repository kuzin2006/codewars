# https://www.codewars.com/kata/simple-assembler-interpreter/train/python


def simple_assembler(program):
    print(program)
    registers = {}
    instruction_counter = 0
    while instruction_counter != len(program):
        cmd_args = program[instruction_counter].split(' ')

        if cmd_args[0] == 'mov':
            if cmd_args[2].lstrip('-').isnumeric():
                registers[cmd_args[1]] = int(cmd_args[2])
            else:
                registers[cmd_args[1]] = registers[cmd_args[2]]
        elif cmd_args[0] == 'inc':
            registers[cmd_args[1]] += 1
        elif cmd_args[0] == 'dec':
            registers[cmd_args[1]] -= 1
        elif cmd_args[0] == 'jnz':
            reg = int(cmd_args[1]) if cmd_args[1].isnumeric() else registers[cmd_args[1]]
            if reg != 0:
                if int(cmd_args[2]) >= len(program):
                    break
                else:
                    instruction_counter += int(cmd_args[2])
                continue
        instruction_counter += 1

    return registers


code = '''\
mov a 5
inc a
dec a
dec a
jnz a -1
inc a'''
print(simple_assembler(['mov d 3','dec d','mov b d','jnz b -2','inc d','mov a d','jnz 5 1','mov c a']))