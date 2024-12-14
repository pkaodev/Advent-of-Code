import os
import sys
# from PIL import Image, ImageDraw, ImageFont


current_dir = os.path.dirname(os.path.realpath(__file__))
utils_path = os.path.join(current_dir, "../../../templates/python")
sys.path.append(utils_path)
import utils

# input_file = "input_example"
input_file = "input"

input_path = os.path.join(current_dir, input_file)

with open(input_path, "r", encoding="utf8") as file:
    data = file.read().split("\n")
    
    _data = []
    for _ in data:
        xo = int(_.split(' ')[0].split(',')[0].split('=')[1])
        yo = int(_.split(' ')[0].split(',')[1])
        vx = int(_.split(' ')[1].split(',')[0].split('=')[1])
        vy = int(_.split(' ')[1].split(',')[1])
        _data.append((xo, yo, vx, vy))
    data = _data
    
    



def move_robot(xo, yo, vx, vy, width, height, steps):
    x_final = (xo + vx * steps) % width
    y_final = (yo + vy * steps) % height
    return (x_final, y_final)

if input_file == "input_example":
    WIDTH = 11
    HEIGHT = 7
if input_file == "input":
    WIDTH = 101
    HEIGHT = 103

def solution_1(data):
    STEPS = 100
    
    final_positions = [
        move_robot(xo, yo, vx, vy, WIDTH, HEIGHT, STEPS)
        for xo, yo, vx, vy in data
    ]
    
    top_left = 0
    top_right = 0
    bot_left = 0
    bot_right = 0
    
    for x, y in final_positions:
        is_left = x < ((WIDTH - 1) / 2)
        is_right = x > ((WIDTH - 1) / 2)
        is_top = y < ((HEIGHT - 1) / 2)
        is_bot = y > ((HEIGHT - 1) / 2)
        if is_top and is_left:
            top_left += 1
        if is_top and is_right:
            top_right += 1
        if is_bot and is_left:
            bot_left += 1
        if is_bot and is_right:
            bot_right += 1
            
    solution = top_left * top_right * bot_left * bot_right
    print(solution)
        

def solution_2(data):
    
    # Option 1
    # def draw_grid(robots, step_num):
    #     grid = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    #     for (x, y, _, _) in robots:
    #         grid[y][x] = "#"
        
    #     IMAGE_DIR = '_p2_images'
    #     image_file_name = f"step_{step_num}.png"
    #     image_path = os.path.join(current_dir, IMAGE_DIR, image_file_name)
        
    #     cell_size = 10
    #     img_width = WIDTH * cell_size
    #     img_height = HEIGHT * cell_size
        
    #     img = Image.new("RGB", (img_width, img_height), "white")
    #     draw = ImageDraw.Draw(img)
        
    #     for y in range(HEIGHT):
    #         for x in range(WIDTH):
    #             color = "black" if grid[y][x] == "#" else "white"
    #             draw.rectangle([(x*cell_size, y*cell_size), ((x+1)*cell_size, (y+1)*cell_size)], fill=color, outline="grey")
        
    #     img.save(image_path)
    
    # Option 2
    def is_tree(robots, square_size):
        g = [0]*(WIDTH*HEIGHT)
        for rx, ry, _, _ in robots:
            if 0 <= rx < WIDTH and 0 <= ry < HEIGHT:
                g[ry*WIDTH+rx] = 1
        w, h = WIDTH, HEIGHT
        ps = [0]*((w+1)*(h+1))
        wp = w+1
        for y in range(h):
            s = 0
            yp = y*wp
            ypp = (y+1)*wp
            gy = y*w
            for x in range(w):
                s += g[gy+x]
                ps[ypp+x+1] = ps[yp+x+1]+s
        need = square_size*square_size
        ssz = square_size
        for y in range(h-ssz+1):
            yp = y*wp
            ypp = (y+ssz)*wp
            for x in range(w-ssz+1):
                if ps[ypp+x+ssz]-ps[ypp+x]-ps[yp+x+ssz]+ps[yp+x] == need:
                    return True
        return False
    
    STEPS = 10000 # just has to be enough to see the message
    for step in range(STEPS):
        
        for i, robot in enumerate(data):
            xo, yo, vx, vy = robot
            x = (xo + vx) % WIDTH
            y = (yo + vy) % HEIGHT
            robot = (x, y, vx, vy)
            data[i] = robot

        
        # draw_grid(data, step+1)
        
        SQUARE_SIZE = 3
        if is_tree(data, SQUARE_SIZE):
            print(step+1)
            break



if __name__ == "__main__":
    # solution_1(data)
    solution_2(data)
