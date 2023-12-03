'''
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone!
The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one.
If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol,
even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right).
Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''
example_input = open('example_input.txt', 'r').read()
real_input = open('input.txt', 'r').read()

# part_sum takes a grid and returns the sum of the part numbers
def part_sum(grid):
    total = 0
    lines = grid.split('\n')
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if not line[j].isdigit() and line[j] != '.':
                if i-1 >= 0:
                    lines[i-1], line_sum1 = get_num(lines[i-1], j)
                    lines[i-1], line_sum2 = get_num(lines[i-1], j-1)
                    lines[i-1], line_sum3 = get_num(lines[i-1], j+1)
                    total += line_sum1 + line_sum2 + line_sum3
                if i+1 < len(lines):
                    lines[i+1], line_sum1 = get_num(lines[i+1], j)
                    lines[i+1], line_sum2 = get_num(lines[i+1], j-1)
                    lines[i+1], line_sum3 = get_num(lines[i+1], j+1)
                    total += line_sum1 + line_sum2 + line_sum3

                lines[i], line_sum1 = get_num(lines[i], j-1)
                lines[i], line_sum2 = get_num(lines[i], j+1)
                total += line_sum1 + line_sum2
    return total

# get_num takes a line and position in that line, and returns a tuple of the new line (with numbers replaced with .) and the expansion of the number at that position
def get_num(line : str, pos : int):
    if pos < 0 or pos >= len(line) or not line[pos].isdigit():
        return (line, 0)
    
    new_line = line[:pos] + '.' + line[pos+1:]
    left = pos-1
    right = pos+1
    num = line[pos]

    while left >= 0 and new_line[left].isdigit():
        num = new_line[left] + num
        new_line = new_line[:left] + '.' + new_line[left+1:]
        left -= 1

    while right < len(new_line) and new_line[right].isdigit():
        num = num + new_line[right]
        new_line = new_line[:right] + '.' + new_line[right+1:]
        right += 1
    
    return (new_line, int(num))
    



print("The sum of the part numbers for the example input is", part_sum(example_input))
print("The sum of the part numbers for the real input is", part_sum(real_input))

'''
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other.
You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345.
The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?
'''
def gear_ratio_sum(grid):
    total = 0
    lines = grid.split('\n')
    posix = [-1, 0, 1]
    for i in range(len(lines)):
        line = lines[i]
        for j in range(len(line)):
            if line[j] == '*':
                parts = []
                if i-1 >= 0:
                    new_line = lines[i-1]
                    for pos in posix:
                        new_line, part = get_num(new_line, j+pos)
                        if part != 0:
                            parts.append(part)
                if i+1 < len(lines):
                    new_line = lines[i+1]
                    for pos in posix:
                        new_line, part = get_num(new_line, j+pos)
                        if part != 0:
                            parts.append(part)
                for pos in [-1, 1]:
                    _, part = get_num(line, j+pos)
                    if part != 0:
                        parts.append(part)

                if len(parts) != 2:
                    continue
                
                total += parts[0] * parts[1]

    return total


example_input2 = open('example_input2.txt', 'r').read()
print("The sum of the gear ratios for the example input is", gear_ratio_sum(example_input))
print("The sum fo the gear ratios for the second example input is", gear_ratio_sum(example_input2))
print("The sum of the gear ratios for the real input is", gear_ratio_sum(real_input))