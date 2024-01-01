import pygame
import math
import random
#use some miku sprites
#that will like, make her angry sometimes
#sometimes shell be happy

# Initialize Pygame
pygame.init()

# Set up display dimensions
width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Miku')

# Load background image
background_image = pygame.image.load('assets/1.jpg')  # Replace with your image path
background_image = pygame.transform.scale(background_image, (width, height))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Eyes
eye_radius = 20  # Smaller eye radius
eye_distance = 100  # Distance between the eyes
center_x, center_y = width // 2, height // 2
right_eye_pos = (1000,1000)
left_eye_pos = (1000,1000)
eyebrow_length = 30  # Increased length
eyebrow_thickness = 10
countEye = 0
countRightEye = 0
# Mouse Capture
mouse_y,mouse_x = (0,0)
# Wobbling parameters
wobble_speed = 0.1  # Adjust the speed of the wobble
wobble_range = 10    # Adjust the range of the wobble
def leftPupil():
    global pupil_left_x,pupil_left_y,right_eye_pos,left_eye_pos
    angle_left = math.atan2(mouse_y - center_y, mouse_x - left_eye_pos[0])
    pupil_left_x = left_eye_pos[0] + math.cos(angle_left) * pupil_distance
    pupil_left_y = left_eye_pos[1] + math.sin(angle_left) * pupil_distance

def rightPupil():
    global pupil_right_y,pupil_right_x,angle_right,right_eye_pos,left_eye_pos
    angle_right = math.atan2(mouse_y - center_y, mouse_x - right_eye_pos[0])
    pupil_right_x = right_eye_pos[0] + math.cos(angle_right) * pupil_distance
    pupil_right_y = right_eye_pos[1] + math.sin(angle_right) * pupil_distance

pupil_distance = min(eye_radius // 2, math.hypot(mouse_x - right_eye_pos[0], mouse_y - right_eye_pos[1]))

# Sounds
click_sound = pygame.mixer.Sound("assets/mikudayo.wav")
count = 0
# Draw the image
screen.blit(background_image, (0, 0))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        keys = pygame.key.get_mods()
        mouse_buttons = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pupil_distance = min(eye_radius // 2, math.hypot(mouse_x - right_eye_pos[0], mouse_y - right_eye_pos[1]))
        if event.type == pygame.QUIT:
            running = False
        elif keys & pygame.KMOD_SHIFT and mouse_buttons[0]:  # Check Shift key and left mouse button
            countEye +=1
            if countEye == 1:
                pupil_right_x = right_eye_pos[0] + math.cos(angle_right) * pupil_distance
                pupil_right_y = right_eye_pos[1] + math.sin(angle_right) * pupil_distance
                right_eye_pos = (mouse_x,mouse_y)
                angle_right = math.atan2(mouse_y - center_y, mouse_x - right_eye_pos[0])
                pygame.draw.circle(screen, WHITE, right_eye_pos, eye_radius)
            elif countEye == 2:
                left_eye_pos = (mouse_x,mouse_y)
                angle_left = math.atan2(mouse_y - center_y, mouse_x - left_eye_pos[0])
                pupil_left_x = left_eye_pos[0] + math.cos(angle_left) * pupil_distance
                pupil_left_y = left_eye_pos[1] + math.sin(angle_left) * pupil_distance
                pygame.draw.circle(screen, WHITE, left_eye_pos, eye_radius)
            elif countEye > 2:
                print("Eyes already exist")       
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                right_eye_pos=(1000,1000)
                left_eye_pos=(1000,1000)
                screen.blit(background_image,(0,0))
                countLeftEye=0
                countRightEye=0
        
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
            if event.button == 1:  # Check for left mouse button click (1)
                ranPlay = int(random.randint(1,25))
                if ranPlay == 12:
                    click_sound.play()  # Play a sound upon mouse click
        
        else:
            pygame.display.flip()
            # Get mouse position
            # Draw circles representing the eyes
            # Calculate the angle between the eye center and mouse position
            leftPupil()
            rightPupil()
            # Draw smaller black circles (pupils) that follow the mouse with limited movement
            pygame.draw.circle(screen, WHITE, right_eye_pos, eye_radius)
            pygame.draw.circle(screen, WHITE, left_eye_pos, eye_radius)
            pygame.draw.circle(screen, BLACK, (int(pupil_right_x), int(pupil_right_y)), eye_radius // 4)
            pygame.draw.circle(screen, BLACK, (int(pupil_left_x), int(pupil_left_y)), eye_radius // 4)
            pygame.display.flip()

# Quit Pygame properly
pygame.quit()

