from year2019.intcode import Robot
from common import input_list_string

def explore(program, position=0+0j, start_cell=0, direction=1+0j, part=1):
    robot = Robot(program[:], [])
    grid = {}
    visited = []
    grid[position] = start_cell

    while True:
        if position in grid.keys():
            robot.i.append(grid[position])
        else:
            robot.i.append(0)
  
        colour = robot.run()
        grid[position] = colour
    
        if colour == 1:
            visited.append(position)
    
        if robot.s == 'H':
            break
    
        turn = robot.run()
        direction *= [1j, -1j][turn]
  
        position += direction
  
    if part == 1:
        painted_count = len(set(visited))
        return painted_count

    return grid

def part_one(prog):
    return explore(prog)

def part_two(prog):
    grid = explore(prog, start_cell=1, part=2)
    dot_list = []
    for key in grid:
        if grid[key] == 1:
            dot_list.append((key.real, key.imag))
    
    for y in range(0, -6, -1):
        line = ""
        for x in range(0, -40, -1):
            if(y, x) in dot_list:
                line += "#"
            else:
                line += " "
        print(line)

    
def get_result():
    inp = input_list_string("2019", "11")[0]
    inp_prog = [int(x) for x in inp.split(",")]
    print("Part one", part_one(inp_prog))
    print("Part two")
    part_two(inp_prog)
    
