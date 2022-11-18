from collections import defaultdict
import pickle

with open("badapple.txt") as f:
    data = f.read().split()

grid_size = (36, 28)


def grid_to_dict(grid):
    d = defaultdict(int)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                d[(x, y)] = 1
    return d


def find_top_left(grid):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if grid[(x, y)] == 1:
                return x, y


def find_largest_rectangle(grid):
    top_left = find_top_left(grid)
    x, y = top_left
    width = 0
    height = 0
    while grid[(x, y)] == 1 and x < grid_size[0]:
        width += 1
        x += 1
    x, y = top_left
    while grid[(x, y)] == 1 and y < grid_size[1]:
        height += 1
        y += 1
    return *top_left, width, height


def is_finished(grid):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if grid[(x, y)] == 1:
                return False
    return True


def delete_rectangle(grid, x, y, width, height):
    for i in range(height):
        for j in range(width):
            if grid[(x + j, y + i)] == 1:
                del grid[(x+j, y+i)]


all_frames = []

for frame in range(4381):
    grid = [list(map(int, i)) for i in data[frame*28:(frame+1)*28]]
    grid = grid_to_dict(grid)
    rects = []
    print("Frame", frame)
    while (not is_finished(grid)):
        largest = find_largest_rectangle(grid)
        rects.append(largest)
        # print(largest)
        delete_rectangle(grid, *largest)
    print("Rectangles:", rects)
    all_frames.append(rects)

pickle.dump(all_frames, open("rects.pickle", "wb"))
