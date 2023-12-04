def call_func_adj_tiles(func, x, y, max_x, max_y, min_x=0, min_y=0):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dy, dx in directions:
        nx = x + dx
        ny = y + dy
        
        if min_y <= ny <= max_y and min_x <= nx <= max_x:
            func(nx, ny)
