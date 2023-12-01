'''
You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky")
and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize
that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show
off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover.
On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?
'''
real_input = open('input.txt', 'r').read()
example_input = open('example_input.txt', 'r').read()

def calibration_value(line):
    first = ''
    second = ''

    for c in line:
        if c.isdigit():
            if first == '':
                first = c
            second = c
    
    num = first + second
    return int(num)

def total_calibration(lines):
    total = 0
    for line in lines.split('\n'):
        total += calibration_value(line)
    return total

print("Total calibration value for example is", total_calibration(example_input))
print("Total calibration value for real input is", total_calibration(real_input))

'''
Part 2:
Your calculation isn't quite right. It looks like some of the digits are 
actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?
'''
example_input2 = open('example_input2.txt', 'r').read()

def calibration_value_2(line):
    first = ''
    second = ''

    prefixes = {
        'o' : ['one'],
        't' : ['two', 'three'],
        'f' : ['four', 'five'],
        's' : ['six', 'seven'],
        'e' : ['eight'],
        'n' : ['nine'],
    }

    digits = {
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }

    for i in range(len(line)):
        if line[i].isdigit():
            if first == '':
                first = line[i]
            second = line[i]
        elif line[i] in prefixes:
            # Figure out which / if the number is here
            for p in prefixes[line[i]]:
                if line[i:].find(p) == 0:
                    if first == '':
                        first = digits[p]
                    second = digits[p]
                    break
    
    num = first + second
    return int(num)

def total_calibration_2(lines):
    total = 0
    for line in lines.split('\n'):
        total += calibration_value_2(line)
    return total

print("Total calibration value for example is", total_calibration_2(example_input2))
print("Total calibration value for real input is", total_calibration_2(real_input))