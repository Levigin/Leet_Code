def flood_fill(image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
    visited = set()
    pixels = set()
    px = image[sr][sc]
    pixels.add((sr, sc))
    while pixels:
        curr_pixel = pixels.pop()
        visited.add(curr_pixel)
        image[curr_pixel[0]][curr_pixel[1]] = color
        for pixel in get_neighs(image, curr_pixel[0], curr_pixel[1], px):
            if pixel not in visited:
                image[pixel[0]][pixel[1]] = color
                pixels.add(pixel)

    return image


def get_neighs(img: list[list[int]], y: int, x: int, px: int) -> list[tuple[int, int]]:
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighs = []
    for d in delta:
        y_, x_ = d[0] + y, x + d[1]
        if 0 <= y_ < len(img) and 0 <= x_ < len(img[0]) and img[y_][x_] == px:
            neighs.append((y_, x_))

    return neighs


if __name__ == '__main__':
    nums = [[0,0,0],[0,0,0]]
    i, j = 0,0
    c = 0
    print(f'Ans: {flood_fill(nums, i, j, c)}')
