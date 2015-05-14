from p6_game import Simulator

ANALYSIS = {}


def analyze(design):
    sim = Simulator(design)
    queue = []
    prev = []
    init = sim.get_initial_state()
    queue.append((init, [init]))
    prev.append(init)
    while queue:
        (state, path) = queue.pop(0)
        for next_move in sim.get_moves():
            next_state = sim.get_next_state(state, next_move)
            if next_state is not None and next_state not in ANALYSIS and next_state not in prev:
                ANALYSIS[next_state] = path
                queue.append((next_state, path + [next_state]))
                prev.append(next_state)


def inspect((i, j), draw_line):
    goal = False
    for next_item in ANALYSIS:
        if (i, j) == next_item[0]:
            path = ANALYSIS[next_item]
            for var in range(len(path) - 1):
                goal = True
                draw_line(path[var][0], path[var + 1][0], offset_obj=None, color_obj=path[var][1])
            draw_line(path[-1][0], (i, j), offset_obj=None, color_obj=path[-1][1])
            print "Path found!"
    if not goal:
        print "No path could be found, please try another tile."


__author__ = 'Alec'
