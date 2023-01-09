import cv2
import pygame
import numpy as np

# Initialize Pygame and the display screen
pygame.init()
screen = pygame.display.set_mode((640, 480))

# Initialize the camera
camera = cv2.VideoCapture(0)

while True:
    # Capture an image from the camera
    ret, frame = camera.read()

    # Convert the image to a Pygame surface
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)

    # Display the image on the screen
    screen.blit(frame, (0, 0))
    pygame.display.flip()

# Clean up
camera.release()
pygame.quit()
