import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_PINK = (255, 182, 193)
BEIGE = (245, 245, 220)
PINK = (255, 192, 203)

# Ball properties
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Paddle properties
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 8

# Brick properties
BRICK_WIDTH = 50
BRICK_HEIGHT = 20

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game - Heart Edition")

# Clock for controlling frame rate
clock = pygame.time.Clock()

def create_heart_bricks():
    """Creates a heart-shaped configuration of bricks."""
    bricks = []
    heart_pattern = [
        "   0000   0000   ",
        "  000000 000000  ",
        "  0000000000000  ",
        "   00000000000   ",
        "    000000000    ",
        "     0000000     ",
        "      00000      ",
        "       000      "
    ]
    offset_x = (SCREEN_WIDTH - len(heart_pattern[0]) * BRICK_WIDTH) // 2
    offset_y = 50  # Starting y-position of the heart

    for row_idx, row in enumerate(heart_pattern):
        for col_idx, char in enumerate(row):
            if char == "0":
                brick_x = offset_x + col_idx * BRICK_WIDTH
                brick_y = offset_y + row_idx * BRICK_HEIGHT
                brick = pygame.Rect(brick_x, brick_y, BRICK_WIDTH - 2, BRICK_HEIGHT - 2)
                bricks.append(brick)
    return bricks

def show_welcome_screen():
    """Displays a welcome screen with a start button."""
    while True:
        screen.fill(BLACK)
        
        # Display title
        font = pygame.font.Font(None, 54)
        title_text = font.render("Welcome to Breakout", True, BEIGE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 4))

        # Display heart edition
        font = pygame.font.Font(None, 50)
        heart_text = font.render(" Heart Edition ^.^", True, PINK)
        screen.blit(heart_text, (SCREEN_WIDTH // 2 - heart_text.get_width() // 2, SCREEN_HEIGHT // 3))
        
        # Display start instruction
        font = pygame.font.Font(None, 26)
        start_text = font.render("Press SPACE to Start", True, BEIGE)
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game when SPACE is pressed
                    return
        
        pygame.display.flip()
        clock.tick(60)

def show_game_over_screen():
    """Displays the Game Over screen with Retry and Exit options."""
    while True:
        screen.fill(BLACK)
        
        # Display Game Over text
        font = pygame.font.Font(None, 54)
        game_over_text = font.render("Game Over", True, BEIGE)
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        
        # Display retry and exit instructions
        font = pygame.font.Font(None, 26)
        retry_text = font.render("Press R to Retry", True, BEIGE)
        exit_text = font.render("Press ESC to Exit", True, BEIGE)
        screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Retry the game
                    return True
                if event.key == pygame.K_ESCAPE:  # Exit the game
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()
        clock.tick(60)

def show_win_screen():
    """Displays the Win screen."""
    while True:
        screen.fill(BLACK)
        
        # Display win text
        font = pygame.font.Font(None, 54)
        win_text = font.render("Nice! You Win!", True, BEIGE)
        screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 3))
        
        # Display restart or exit instructions
        font = pygame.font.Font(None, 26)
        retry_text = font.render("Press R to Restart", True, BEIGE)
        exit_text = font.render("Press ESC to Exit", True, BEIGE)
        screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(exit_text, (SCREEN_WIDTH // 2 - exit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        
        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    return True
                if event.key == pygame.K_ESCAPE:  # Exit the game
                    pygame.quit()
                    sys.exit()
        
        pygame.display.flip()
        clock.tick(60)

def main():
    while True:
        # Show the welcome screen
        show_welcome_screen()
        
        # Paddle
        paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 40, PADDLE_WIDTH, PADDLE_HEIGHT)
        
        # Ball
        ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 15, 15)
        ball_speed_x = BALL_SPEED_X
        ball_speed_y = BALL_SPEED_Y
        
        # Bricks in heart shape
        bricks = create_heart_bricks()
        
        # Score
        score = 0
        
        # Main game loop
        running = True
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # Movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle.left > 0:
                paddle.move_ip(-PADDLE_SPEED, 0)
            if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
                paddle.move_ip(PADDLE_SPEED, 0)
            
            # Ball movement
            ball.x += ball_speed_x
            ball.y += ball_speed_y
            
            # Ball collision with walls
            if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
                ball_speed_x = -ball_speed_x
            if ball.top <= 0:
                ball_speed_y = -ball_speed_y
            if ball.bottom >= SCREEN_HEIGHT:
                running = False  # Game over
            
            # Ball collision with paddle
            if ball.colliderect(paddle):
                ball_speed_y = -ball_speed_y
            
            # Ball collision with bricks
            for brick in bricks[:]:
                if ball.colliderect(brick):
                    ball_speed_y = -ball_speed_y
                    bricks.remove(brick)
                    score += 1
            
            # Win condition
            if not bricks:
                if show_win_screen():  # Show win screen and restart if player chooses
                    return  # Restart the game loop
                else:
                    pygame.quit()
                    sys.exit()
            
            # Draw everything
            screen.fill(BLACK)
            pygame.draw.rect(screen, WHITE, paddle)
            pygame.draw.ellipse(screen, WHITE, ball)
            for brick in bricks:
                pygame.draw.rect(screen, LIGHT_PINK, brick)
            
            # Display score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            
            # Update display
            pygame.display.flip()
            
            # Cap the frame rate
            clock.tick(60)
        
        # Show Game Over screen and handle retry/exit
        if not show_game_over_screen():
            break  # Exit the game loop if the player chooses to quit

if __name__ == "__main__":
    main()
