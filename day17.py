with open('day17-input.txt', 'r') as f:
    DEBUG = False
    lines = f.readlines()
    for line in lines:
        if line.startswith('Register A:'):
            reg_a = int(line.strip().split(':')[1])
        if line.startswith('Register B:'):  
            reg_b = int(line.strip().split(':')[1])
        if line.startswith('Register C:'):
            reg_c = int(line.strip().split(':')[1])
        if line.startswith('Program:'):
            prog = [int(s) for s in line.strip().split(':')[1].split(',')]

    def combo(registers, operand):
        reg_a, reg_b, reg_c = registers
# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return reg_a
        if operand == 5:
            return reg_b
        if operand == 6:
            return reg_c
        raise ValueError   


    def run_prog(state, prog):
        counter, reg_a, reg_b, reg_c, output = state

        while True:
            if counter >= len(prog):
                break
            stmt = prog[counter]
            operand = prog[counter+1]
            if DEBUG: print(counter, oct(reg_a), oct(reg_b), oct(reg_c), output)
            if DEBUG: print(stmt, operand)
#The adv instruction (opcode 0) performs division. 
# The numerator is the value in the A register. 
# The denominator is found by raising 2 to the power of the instruction's combo operand. 
# (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) 
# The result of the division operation is truncated to an integer and then written to the A register.
            if stmt == 0:
                reg_a = reg_a // pow(2, combo((reg_a,reg_b,reg_c), operand))
#The bxl instruction (opcode 1) calculates the bitwise XOR of register B 
# and the instruction's literal operand, 
# then stores the result in register B.
            elif stmt == 1:
                reg_b = reg_b ^ operand
#The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 
# (thereby keeping only its lowest 3 bits), then writes that value to the B register.
            elif stmt == 2:
                reg_b = combo((reg_a,reg_b,reg_c), operand) % 8
# The jnz instruction (opcode 3) does nothing if the A register is 0. 
# However, if the A register is not zero, it jumps by setting the instruction pointer 
# to the value of its literal operand; if this instruction jumps, 
# the instruction pointer is not increased by 2 after this instruction.
            elif stmt == 3:
                if reg_a != 0:
                    counter = operand-2
#The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, 
# then stores the result in register B. 
# (For legacy reasons, this instruction reads an operand but ignores it.)
            elif stmt == 4:
                reg_b = reg_b ^ reg_c
#The out instruction (opcode 5) calculates the value of its combo operand modulo 8, 
# then outputs that value. (If a program outputs multiple values, they are separated by commas.)
            elif stmt == 5:
                output.append(combo((reg_a,reg_b,reg_c), operand) % 8)
#The bdv instruction (opcode 6) works exactly like the adv instruction 
# except that the result is stored in the B register. 
# (The numerator is still read from the A register.)
            elif stmt == 6:
                reg_b = reg_a // pow(2, combo((reg_a,reg_b,reg_c), operand))
#The cdv instruction (opcode 7) works exactly like the adv instruction 
# except that the result is stored in the C register. 
# (The numerator is still read from the A register.)
            elif stmt == 7:
                reg_c = reg_a // pow(2, combo((reg_a,reg_b,reg_c), operand))

            counter+=2

        return (counter, reg_a, reg_b, reg_c, output)
    


    reg_a, reg_b, reg_c = 0, 0, 0
    i = 1
    while True:
        state = run_prog((0, reg_a, reg_b, reg_c, []), prog)
        _, _, _, _, output = state
        if output[-i] == prog[-i]:
            if DEBUG: print(reg_a, oct(reg_a), output)
            if i>2 and output[0:2] != prog[-i:-i+2]: 
                if DEBUG: print ('matched the head but the next got messed up')
                reg_a += 1
            else:
                if DEBUG: print ('match', i, prog[-i])
                if i == len(prog):
                    if DEBUG: print ('***full match***') 
                    if DEBUG: print ('REG_A', reg_a) 
                    if DEBUG: print ('PROG', prog) 
                    if DEBUG: print ('OUTPUT', output) 
                    print('day17 part2', reg_a)
                    break
                reg_a = reg_a * 8
                i += 1            
        else:
            reg_a += 1