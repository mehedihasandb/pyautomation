import pygame
import random
import math

pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class ParticleSystem:
    def __init__(self):
        self.particles = []
    
    def add_particle(self, x, y, color):
        for _ in range(3):
            self.particles.append({
                'x': x * GRID_SIZE + GRID_SIZE // 2 + random.randint(-5, 5),
                'y': y * GRID_SIZE + GRID_SIZE // 2 + random.randint(-5, 5),
                'size': random.randint(3, 8),
                'alpha': 255,
                'color': color,
                'vx': random.uniform(-1, 1),
                'vy': random.uniform(-1, 1)
            })
    
    def update(self):
        for particle in self.particles[:]:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['alpha'] -= 8
            particle['size'] *= 0.96
            if particle['alpha'] <= 0:
                self.particles.remove(particle)
    
    def draw(self, screen):
        for particle in self.particles:
            surface = pygame.Surface((int(particle['size']*2), int(particle['size']*2)))
            surface.set_alpha(int(particle['alpha']))
            surface.fill(particle['color'])
            surface.set_colorkey(BLACK)
            pygame.draw.circle(surface, particle['color'], 
                             (int(particle['size']), int(particle['size'])), 
                             int(particle['size']))
            screen.blit(surface, (particle['x'] - particle['size'], 
                                 particle['y'] - particle['size']))

class Snake:
    def __init__(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.grow = False
        self.invincible = False
        self.invincible_timer = 0
    
    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
        
        if new_head in self.body and not self.invincible:
            return False
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        
        if self.invincible:
            self.invincible_timer -= 1
            if self.invincible_timer <= 0:
                self.invincible = False
        
        return True
    
    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def eat(self):
        self.grow = True
    
    def apply_effect(self, effect):
        if effect == 'invincible':
            self.invincible = True
            self.invincible_timer = 50
    
    def draw(self, screen):
        for i, segment in enumerate(self.body):
            intensity = 255 - int((i / max(len(self.body), 1)) * 150)
            
            if self.invincible and self.invincible_timer % 4 < 2:
                color = (160, 32, 240)  # Purple when invincible
            else:
                color = (0, intensity, 0)
            
            # Glow effect
            glow_surface = pygame.Surface((GRID_SIZE + 8, GRID_SIZE + 8))
            glow_surface.set_alpha(40)
            glow_surface.fill(color)
            screen.blit(glow_surface, 
                       (segment[0] * GRID_SIZE - 4, segment[1] * GRID_SIZE - 4))
            
            # Main body
            pygame.draw.rect(screen, color,
                           (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE,
                            GRID_SIZE - 2, GRID_SIZE - 2), border_radius=4)

class Food:
    TYPES = {
        'normal': {'color': (255, 0, 0), 'points': 1, 'effect': None},
        'golden': {'color': (255, 215, 0), 'points': 5, 'effect': None},
        'purple': {'color': (160, 32, 240), 'points': 3, 'effect': 'invincible'}
    }
    
    def __init__(self, snake_body):
        self.position = self.generate_position(snake_body)
        rand = random.random()
        if rand < 0.75:
            self.type = 'normal'
        elif rand < 0.90:
            self.type = 'golden'
        else:
            self.type = 'purple'
        self.lifetime = 0
    
    def generate_position(self, snake_body):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                return pos
    
    def draw(self, screen):
        food_data = self.TYPES[self.type]
        pulse = abs(math.sin(self.lifetime * 0.1)) * 4
        size = GRID_SIZE - 2 + pulse
        offset = (GRID_SIZE - size) // 2
        
        if self.type != 'normal':
            glow_surface = pygame.Surface((GRID_SIZE + 10, GRID_SIZE + 10))
            glow_surface.set_alpha(60)
            glow_surface.fill(food_data['color'])
            screen.blit(glow_surface, 
                       (self.position[0] * GRID_SIZE - 5, 
                        self.position[1] * GRID_SIZE - 5))
        
        pygame.draw.rect(screen, food_data['color'],
                        (self.position[0] * GRID_SIZE + offset,
                         self.position[1] * GRID_SIZE + offset,
                         size, size), border_radius=int(size//2))
        
        self.lifetime += 1

class ComboSystem:
    def __init__(self):
        self.combo = 0
        self.combo_timer = 0
        self.COMBO_TIMEOUT = 90
    
    def add_combo(self):
        self.combo += 1
        self.combo_timer = self.COMBO_TIMEOUT
    
    def update(self):
        if self.combo_timer > 0:
            self.combo_timer -= 1
            if self.combo_timer == 0:
                self.combo = 0
    
    def get_multiplier(self):
        if self.combo >= 5:
            return 3
        elif self.combo >= 3:
            return 2
        return 1
    
    def draw(self, screen):
        if self.combo > 1:
            font = pygame.font.Font(None, 42)
            text = f"x{self.get_multiplier()} COMBO!"
            combo_text = font.render(text, True, (255, 215, 0))
            # Pulsing effect
            scale = 1 + math.sin(self.combo_timer * 0.2) * 0.1
            scaled = pygame.transform.scale(combo_text, 
                                           (int(combo_text.get_width() * scale),
                                            int(combo_text.get_height() * scale)))
            screen.blit(scaled, (WIDTH // 2 - scaled.get_width() // 2, 60))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game - Enhanced Edition")
    clock = pygame.time.Clock()
    
    snake = Snake()
    food = Food(snake.body)
    particles = ParticleSystem()
    combo = ComboSystem()
    score = 0
    
    try:
        beep_sound = pygame.mixer.Sound("button-3.wav")
        beep_sound.set_volume(0.3)
    except:
        beep_sound = None
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)
        
        if not snake.move():
            print(f"Game Over! Final Score: {score}")
            running = False
            continue
        
        # Trail particles
        if len(snake.body) > 2:
            particles.add_particle(snake.body[-1][0], snake.body[-1][1], (0, 150, 0))
        
        if snake.body[0] == food.position:
            snake.eat()
            food_data = Food.TYPES[food.type]
            
            if food_data['effect']:
                snake.apply_effect(food_data['effect'])
            
            combo.add_combo()
            points = food_data['points'] * combo.get_multiplier()
            score += points
            
            # Food particles
            particles.add_particle(food.position[0], food.position[1], food_data['color'])
            
            food = Food(snake.body)
            if beep_sound:
                beep_sound.play()
        
        combo.update()
        particles.update()
        
        # Draw
        screen.fill(BLACK)
        
        # Draw grid (subtle)
        for x in range(0, WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (20, 20, 20), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (20, 20, 20), (0, y), (WIDTH, y))
        
        particles.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        combo.draw(screen)
        
        # Score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Effect indicator
        if snake.invincible:
            shield_text = font.render("INVINCIBLE!", True, (160, 32, 240))
            screen.blit(shield_text, (WIDTH - 200, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()

if __name__ == "__main__":
    main()