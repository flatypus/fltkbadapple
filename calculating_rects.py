from collections import defaultdict
import pickle


data = pickle.load(open("binary.pickle", "rb"))
grid_size = (len(data[0][0]), len(data[0]))
target = 0  # if 0, then it will draw rectangles around white pixels, if 1, then it will draw rectangles around black pixels
print(grid_size)


def grid_to_dict(grid):
    d = defaultdict(int)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == target:
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
    # find the largest rectangle that can be made with the top left corner being (x, y)
    # that ensures all points in the rectangle are 1
    # the rectangle can be made with the width and height being (width, height)
    width = 1
    height = 1
    while True:
        # check if the rectangle is valid
        valid = True
        for i in range(height):
            if (x, y + i) not in grid:
                valid = False
                break
        for j in range(width):
            if (x + j, y) not in grid:
                valid = False
                break
        if not valid:
            break
        # if the rectangle is valid, then increase the width and height of the rectangle
        width += 1
        height += 1
    # decrease the width and height of the rectangle by 1
    width -= 1
    height -= 1
    return x, y, width, height
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

for frame in range(len(data)):
    grid = grid_to_dict(data[frame])
    rects = []
    print(f"Frame {frame} out of {len(data)}")
    while (not is_finished(grid)):
        largest = find_largest_rectangle(grid)
        rects.append(largest)
        # print(largest)
        delete_rectangle(grid, *largest)
    # print("Rectangles:", rects)
    all_frames.append(rects)

pickle.dump(all_frames, open("rects.pickle", "wb"))
