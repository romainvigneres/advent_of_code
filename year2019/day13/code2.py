from common import input_integer_sep

def calc(log, ticker):
    from .program import Program
    from .grid import Grid

    program = Program(ticker, log)

    program.ticker[0] = 2
    score = 0
    grid = Grid()

    ball = (0, 0)
    paddle = (0, 0)

    dump = 0
    skip = 0

    while True:
        program.tick_till_end()
        if not program.flag_running:
            break

        while len(program.output) > 0:
            x = program.output.pop()
            y = program.output.pop()
            tile = program.output.pop()
            if tile == 4:
                ball = (x, y)
            if tile == 3:
                paddle = (x, y)

            if x == -1:
                score = tile
            else:
                grid.set(x, y, tile)

            if tile == 4:
                skip += 1
                if skip >= 2:
                    skip = 0
                    grid.save_frame()
        
        dump += 1
        if dump >= 100:
            grid.show_grid(log, disp_map={0: ' ', 1: '#', 2: 'X', 3: '-', 4: 'o'})
            print("Score: " + str(score))
            dump = 0

        if ball[0] > paddle[0]:
            program.add_to_input(1)
        elif ball[0] < paddle[0]:
            program.add_to_input(-1)
        else:
            program.add_to_input(0)

    grid.draw_frames(color_map={
        0: (0, 0, 0), 
        1: (255, 255, 255), 
        2: (128, 128, 128), 
        3: (128, 10, 10), 
        4: (128, 128, 255), 
    })
    Grid.make_animation()

    print("Last score: " + str(program.output))

    count = 0
    for cur in grid.grid:
        value = grid.grid[cur]
        if value in {2}:
            count += 1

    return count

def get_result():
    inp = input_integer_sep("2019", "13")
    print("Part two", calc(None, inp))