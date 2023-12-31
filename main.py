import pygame
import math
import random

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
countLeftEye = 0
countRightEye = 0
# Mouse Capture
mouse_y,mouse_x = (0,0)

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
def angryFaceExpression():
    pygame.draw.line(screen, BLACK, (left_eye_pos[0]-20, left_eye_pos[1]-30),  # x y right from your point of view
                                    (left_eye_pos[0] + eyebrow_length, left_eye_pos[1] -50 + eyebrow_thickness), eyebrow_thickness)
    pygame.draw.line(screen, BLACK, (right_eye_pos[0]+20, right_eye_pos[1]-30),  # x y left from your point of view
                                    (right_eye_pos[0] - eyebrow_length, right_eye_pos[1] -50 + eyebrow_thickness), eyebrow_thickness)
def faceSadExpression():
    pygame.draw.line(screen, BLACK, (left_eye_pos[0]-20, left_eye_pos[1]-40),  # x y right from your point of view
                    (left_eye_pos[0] + eyebrow_length, left_eye_pos[1] -30 + eyebrow_thickness), eyebrow_thickness)
    
    pygame.draw.line(screen, BLACK, (right_eye_pos[0]+20, right_eye_pos[1]-40),  # x y left from your point of view
                    (right_eye_pos[0] - eyebrow_length, right_eye_pos[1] -30 + eyebrow_thickness), eyebrow_thickness)
def cuteFace():
    pygame.draw.line()
    
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
            countLeftEye +=1
            if countLeftEye > 1:
                print("Eye already exists")
            else:
                left_eye_pos = (mouse_x,mouse_y)
                angle_left = math.atan2(mouse_y - center_y, mouse_x - left_eye_pos[0])
                pupil_left_x = left_eye_pos[0] + math.cos(angle_left) * pupil_distance
                pupil_left_y = left_eye_pos[1] + math.sin(angle_left) * pupil_distance
                pygame.draw.circle(screen, WHITE, left_eye_pos, eye_radius)
                
        elif keys & pygame.KMOD_SHIFT and mouse_buttons[2]: # check shift and right mouse button
            countRightEye +=1
            if countRightEye > 1:
                print("Right eye already exists")
            else:
                pupil_right_x = right_eye_pos[0] + math.cos(angle_right) * pupil_distance
                pupil_right_y = right_eye_pos[1] + math.sin(angle_right) * pupil_distance
                right_eye_pos = (mouse_x,mouse_y)
                angle_right = math.atan2(mouse_y - center_y, mouse_x - right_eye_pos[0])
                pygame.draw.circle(screen, WHITE, right_eye_pos, eye_radius)

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse click event
            if event.button == 1:  # Check for left mouse button click (1)
                ranPlay = int(random.randint(1,25))
                if ranPlay == 12:
                    click_sound.play()  # Play a sound upon mouse click
                count +=2
                if count % 2 == 0:
                    ranExp = int(random.randint(1, 50))  # Generate a random number between 1 and 10  
                    print(ranExp)  
                    if ranExp in [1,2,3,4,5,6,]:  # Check if the random number falls within [1, 2, 3]
                        screen.blit(background_image, (0, 0))
                        angryFaceExpression()
                    if ranExp in [30,31,32,33,34,45,49]:
                        screen.blit(background_image, (0, 0))
                        faceSadExpression()
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

