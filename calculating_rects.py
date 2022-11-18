from collections import defaultdict
import pickle


data = pickle.load(open("binary.pickle", "rb"))
grid_size = (len(data[0][0]), len(data[0]))
target = 1  # if 0, then it will draw rectangles around white pixels, if 1, then it will draw rectangles around black pixels
print(grid_size)


def grid_to_dict(grid):
    d = defaultdict(int)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == target:
                d[(x, y)] = 1
    return d


def represent_grid_of_pixels_as_rectangles(grid):
    rectangles = []
    while not is_finished(grid):
        # find the smallest rectangle that can contain all the pixels
        # then delete those pixels from the grid
        # then repeat
        # print(grid)
        x, y = list(grid.keys())[0]
        width, height = 1, 1
        while (x + width, y) in grid:
            width += 1
        while (x, y + height) in grid:
            height += 1
        # print(x, y, width, height)
        grid = delete_rectangle(grid, x, y, width, height)
        rectangles.append((x, y, width, height))
    return rectangles


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
    return grid


all_frames = []

for frame in range(len(data)):
    grid = grid_to_dict(data[frame])
    rects = represent_grid_of_pixels_as_rectangles(grid)

    print("Frame", frame, "has", len(rects), "rectangles")
    print(f"Frame {frame} out of {len(data)}")
    all_frames.append(rects)

pickle.dump(all_frames, open(
    f"rects{'' if target == 1 else '_white'}.pickle", "wb"))
