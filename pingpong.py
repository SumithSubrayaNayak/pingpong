import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
BALL_SIZE = 20
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)   # Pure Red
BLUE = (0, 0, 255)  # Pure Blue

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Create the paddles and ball
paddle_a = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

# Set initial ball speed
ball_speed = [5, 5]

# Create clock object to control the frame rate
clock = pygame.time.Clock()

# Initialize scores
score_a = 0
score_b = 0

# Create font for displaying scores
font = pygame.font.Font(None, 36)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.top > 0:
        paddle_a.y -= 5
    if keys[pygame.K_s] and paddle_a.bottom < HEIGHT:
        paddle_a.y += 5
    if keys[pygame.K_UP] and paddle_b.top > 0:
        paddle_b.y -= 5
    if keys[pygame.K_DOWN] and paddle_b.bottom < HEIGHT:
        paddle_b.y += 5

    # Move the ball
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collisions with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collisions with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed[0] = -ball_speed[0]

    # Scoring
    if ball.left <= 0:
        score_b += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed[0] = -ball_speed[0]
    elif ball.right >= WIDTH:
        score_a += 1
        ball.x = WIDTH // 2 - BALL_SIZE // 2
        ball.y = HEIGHT // 2 - BALL_SIZE // 2
        ball_speed[0] = -ball_speed[0]

    # Draw everything
    space_color = (0, 0, 25)  # Dark blue color for the space background
    screen.fill(space_color)
    pygame.draw.rect(screen, RED, paddle_a)
    pygame.draw.rect(screen, BLUE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    score_display = font.render(f"Player A: {score_a}  Player B: {score_b}", True, WHITE)
    screen.blit(score_display, (WIDTH // 2 - 100, 20))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
