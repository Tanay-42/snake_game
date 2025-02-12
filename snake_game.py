import pygame
import random

# Initialize pygame
pygame.init()

# Game window size
WIDTH, HEIGHT = 500, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Font
font = pygame.font.Font(None, 36)

def draw_snake(snake_pos):
    for pos in snake_pos:
        pygame.draw.rect(win, GREEN, (*pos, 10, 10))

def show_text(text, x, y, color=WHITE):
    label = font.render(text, True, color)
    win.blit(label, (x, y))

def run_game():
    snake_pos = [[100, 100]]
    snake_dir = "RIGHT"
    speed = 10
    score = 0

    food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
    
    clock = pygame.time.Clock()
    running = True

    while running:
        win.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit game

        # Movement controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_dir != "RIGHT":
            snake_dir = "LEFT"
        if keys[pygame.K_RIGHT] and snake_dir != "LEFT":
            snake_dir = "RIGHT"
        if keys[pygame.K_UP] and snake_dir != "DOWN":
            snake_dir = "UP"
        if keys[pygame.K_DOWN] and snake_dir != "UP":
            snake_dir = "DOWN"

        # Move snake
        head_x, head_y = snake_pos[0]
        if snake_dir == "LEFT":
            head_x -= speed
        elif snake_dir == "RIGHT":
            head_x += speed
        elif snake_dir == "UP":
            head_y -= speed
        elif snake_dir == "DOWN":
            head_y += speed

        new_head = [head_x, head_y]

        # Collision with walls
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return game_over(score)

        # Collision with itself
        if new_head in snake_pos:
            return game_over(score)

        # Add new head to snake
        snake_pos.insert(0, new_head)

        # Check if food is eaten
        if new_head == food_pos:
            food_pos = [random.randrange(0, WIDTH, 10), random.randrange(0, HEIGHT, 10)]
            score += 1
        else:
            snake_pos.pop()

        # Draw elements
        draw_snake(snake_pos)
        pygame.draw.rect(win, RED, (*food_pos, 10, 10))
        show_text(f"Score: {score}", 10, 10)

        pygame.display.update()
        clock.tick(10)

def game_over(score):
    win.fill(BLACK)
    show_text("Game Over!", WIDTH // 2 - 60, HEIGHT // 2 - 50, RED)
    show_text(f"Final Score: {score}", WIDTH // 2 - 70, HEIGHT // 2, WHITE)
    show_text("Press R to Restart or Q to Quit", WIDTH // 2 - 130, HEIGHT // 2 + 40, BLUE)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Quit game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return run_game()  # Restart game
                elif event.key == pygame.K_q:
                    return False  # Quit game

# Start the game
run_game()
pygame.quit()
