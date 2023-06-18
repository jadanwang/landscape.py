# Import pygame
import pygame
from math import pi
 
pygame.init()
 
# Colours
BLACK = (  0,   0,   0)
BROWN = ( 86, 40, 13)
DARK_BROWN = (45, 22, 1)
LIGHT_BROWN = (96, 53, 15)
WHITE = (255, 255, 255)
BLUE =  (149, 244, 249)
GREEN = (  29, 119, 40)
RED =   (255,   0,   0)
LUSH_GREEN = (39, 165, 34)
LIGHT_BLUE = (42, 199, 214)
YELLOW = (255, 199, 0)
PINE_GREEN = (21, 79, 29)
BOAT = (165, 129, 97)

# Screen dimensions
size = [640, 480]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Mountain landscape with boat")
 
#Loop 
done = False
clock = pygame.time.Clock()
 
while not done:
    clock.tick(10)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done=True 
    screen.fill(BLUE)
 
    pygame.draw.line(screen, BLACK, [0, 250], [650, 250], 5)
    pygame.draw.rect(screen, GREEN, [0, 250, 650, 400])
    
    pygame.draw.circle(screen, YELLOW, [165, 160], 55)
    pygame.draw.polygon(screen, YELLOW, [[175, 100], [175, 30], [195, 40]])
    pygame.draw.polygon(screen, YELLOW, [[130, 110], [110, 40], [80, 50]])
    pygame.draw.polygon(screen, YELLOW, [[205, 110], [245, 60], [275, 70]])
    
    pygame.draw.ellipse(screen, LIGHT_BLUE, [100, 200, 500, 100]) 
    
    pygame.draw.polygon(screen, DARK_BROWN, [[265, 250], [345, 90], [490, 250]])
    pygame.draw.polygon(screen, DARK_BROWN, [[375, 250], [545, 50], [790, 250]])
    pygame.draw.polygon(screen, BROWN, [[100, 100], [-150, 250], [200, 250]])
    pygame.draw.polygon(screen, BROWN, [[315, 250], [425, 65], [590, 250]])
    pygame.draw.polygon(screen, LIGHT_BROWN, [[390, 250], [285, 70], [100, 250]])
    
    
    
    pygame.draw.polygon(screen, WHITE, [[100, 100], [49, 130], [120, 130]])
    pygame.draw.polygon(screen, WHITE, [[310, 110], [285, 70], [241, 110]])
    pygame.draw.polygon(screen, WHITE, [[330, 120], [345, 90], [373, 120]])
    pygame.draw.polygon(screen, WHITE, [[407, 95], [425, 65], [452, 95]])
    pygame.draw.polygon(screen, WHITE, [[500, 102], [545, 50], [610, 102]])    
    
    pygame.draw.ellipse(screen, LUSH_GREEN, [-600, 300, 1100, 250]) 
    
    pygame.draw.arc(screen, BLACK, [190, 255, 30, 20], pi,3*pi/2, 2)
    pygame.draw.arc(screen, BLACK,  [190, 255, 30, 20], 3*pi/2, 2*pi, 2)    
    pygame.draw.arc(screen, BLACK, [220, 255, 30, 20], pi,3*pi/2, 2)
    pygame.draw.arc(screen, BLACK,  [220, 255, 30, 20], 3*pi/2, 2*pi, 2)     
    
    pygame.draw.arc(screen, BLACK, [410, 265, 30, 20], pi,3*pi/2, 2)
    pygame.draw.arc(screen, BLACK,  [410, 265, 30, 20], 3*pi/2, 2*pi, 2)    
    pygame.draw.arc(screen, BLACK, [440, 265, 30, 20], pi,3*pi/2, 2)
    pygame.draw.arc(screen, BLACK,  [440, 265, 30, 20], 3*pi/2, 2*pi, 2)
    
    
    
    
    pygame.draw.rect(screen, BROWN, [90, 300, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[60, 280], [100, 250], [140, 280]])
    pygame.draw.polygon(screen, PINE_GREEN, [[60, 300], [100, 270], [140, 300]])
    pygame.draw.polygon(screen, PINE_GREEN, [[60, 320], [100, 290], [140, 320]])
   
    pygame.draw.rect(screen, BROWN, [20, 320, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[-10, 300], [30, 270], [80, 300]])
    pygame.draw.polygon(screen, PINE_GREEN, [[-10, 320], [30, 290], [80, 320]])
    pygame.draw.polygon(screen, PINE_GREEN, [[-10, 340], [30, 310], [80, 340]])   

    pygame.draw.rect(screen, BROWN, [160, 320, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[130, 300], [170, 270], [220, 300]])
    pygame.draw.polygon(screen, PINE_GREEN, [[130, 320], [170, 290], [220, 320]])
    pygame.draw.polygon(screen, PINE_GREEN, [[130, 340], [170, 310], [220, 340]]) 
    
    pygame.draw.rect(screen, BROWN, [260, 305, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[230, 285], [270, 255], [320, 285]])
    pygame.draw.polygon(screen, PINE_GREEN, [[230, 305], [270, 275], [320, 305]])
    pygame.draw.polygon(screen, PINE_GREEN, [[230, 325], [270, 295], [320, 325]])     
    
    pygame.draw.rect(screen, BROWN, [360, 355, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[330, 335], [370, 305], [420, 335]])
    pygame.draw.polygon(screen, PINE_GREEN, [[330, 355], [370, 325], [420, 355]])
    pygame.draw.polygon(screen, PINE_GREEN, [[330, 375], [370, 345], [420, 375]])   
    
    pygame.draw.rect(screen, BROWN, [220, 355, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[190, 335], [230, 305], [280, 335]])
    pygame.draw.polygon(screen, PINE_GREEN, [[190, 355], [230, 325], [280, 355]])
    pygame.draw.polygon(screen, PINE_GREEN, [[190, 375], [230, 345], [280, 375]]) 
    
    pygame.draw.rect(screen, BROWN, [70, 355, 20, 30])
    pygame.draw.polygon(screen, PINE_GREEN, [[40, 335], [80, 305], [130, 335]])
    pygame.draw.polygon(screen, PINE_GREEN, [[40, 355], [80, 325], [130, 355]])
    pygame.draw.polygon(screen, PINE_GREEN, [[40, 375], [80, 345], [130, 375]])     
    pygame.draw.line(screen, BLACK, [420, 250], [420, 190], 5)
    
    pygame.draw.polygon(screen, BOAT, [[380, 235], [460, 235], [420, 270]])
    
    pygame.draw.polygon(screen, BLUE, [[300, 251], [460, 251], [420, 270]])
    
    
    
    pygame.draw.polygon(screen, WHITE, [[420, 190], [420, 225], [450, 225]]) 
    
    pygame.draw.ellipse(screen, WHITE, [300, 25, 50, 20])
    pygame.draw.ellipse(screen, WHITE, [260, 30, 70, 30])
    pygame.draw.ellipse(screen, WHITE, [320, 40, 50, 20])
    
    pygame.draw.ellipse(screen, WHITE, [500, -25, 100, 40])
    pygame.draw.ellipse(screen, WHITE, [520, -5, 100, 40]) 
    pygame.draw.ellipse(screen, WHITE, [460, 2, 80, 30]) 
    pygame.draw.ellipse(screen, WHITE, [599, 2, 80, 30]) 

    pygame.draw.ellipse(screen, WHITE, [-100, -25, 100, 40])
    pygame.draw.ellipse(screen, WHITE, [-80, -5, 100, 40]) 
    pygame.draw.ellipse(screen, WHITE, [-140, 2, 80, 30]) 
    pygame.draw.ellipse(screen, WHITE, [-1, 2, 80, 30]) 
    
    
    pygame.display.flip()
 

pygame.quit()
