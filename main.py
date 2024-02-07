import random

SIZE = 15
WIDTH = SIZE * 30
HEIGHT = SIZE * 30
direction = "east" # 贪吃蛇移动方向
counter = 0 # 延迟变量，用于控制贪吃蛇移动速度
dirs = {"east":(1,0), "west":(-1,0), "north":(0,-1), "south":(0,1)}
length = 1 # 贪吃蛇长度
finished = False

# 创建贪吃蛇
snake_head = Actor("snake_head", (30, 30))
body = []

# 创建食物
food = Actor("snake_food")
food.x = random.randint(2, WIDTH//SIZE - 1) * SIZE
food.y = random.randint(2, HEIGHT//SIZE - 1) * SIZE

def eat_food():
    global length
    if food.x == snake_head.x and food.y == snake_head.y:
        sounds.eat.play()
        food.x = random.randint(2, WIDTH//SIZE - 1) * SIZE
        food.y = random.randint(2, HEIGHT//SIZE - 1) * SIZE

        # 贪吃蛇长度变长
        length += 1

def draw():
    screen.fill((255, 255, 255))
    food.draw()
    for b in body:
        b.draw()
    snake_head.draw()

def update():
    if finished:
        return
    check_gameover()
    check_keys()
    eat_food()
    update_snake()

def check_gameover():
    global finished
    if snake_head.left < 0 or snake_head.right > WIDTH \
            or snake_head.top < 0 or snake_head.bottom > HEIGHT:
        sounds.fail.play()
        finished = True
    for n in range(len(body)-1):
        if body[n].x == snake_head.x and body[n].y == snake_head.y:
            sounds.fail.play()
            finished = True

def check_keys():
    global direction
    if keyboard.right and direction != "west":
        direction = "east"
        snake_head.angle = 0
    elif keyboard.left and direction != "east":
        direction = "west"
        snake_head.angle = 180
    elif keyboard.up and direction != "south":
        direction = "north"
        snake_head.angle = 90
    elif keyboard.down and direction != "north":
        direction = "south"
        snake_head.angle = -90

def update_snake():
    # 设置 UPS ，让游戏运行变慢
    global counter
    counter += 1
    if counter < 10:
        return
    else:
        counter = 0

    # 让蛇移动
    dx, dy = dirs[direction]
    snake_head.x += dx * SIZE
    snake_head.y += dy * SIZE

    # 根据 length 字段添加贪吃蛇的身体
    if len(body) == length:
        body.remove(body[0])
    body.append(Actor("snake_body", (snake_head.x, snake_head.y)))
