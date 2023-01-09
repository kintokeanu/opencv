import RPi.GPIO as GPIO

# Set up the button input
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the camera and display screen
camera = cv2.VideoCapture(0)
pygame.init()
screen = pygame.display.set_mode((640, 480))

while True:
    # Check the state of the button
    button_state = GPIO.input(18)

    # If the button is pressed, display the camera's images
    if button_state == False:
        # Capture an image from the camera
        ret, frame = camera.read()

        # Convert the image to a Pygame surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)

        # Display the image on the screen
        screen.blit(frame, (0, 0))
        pygame.display.flip()
    else:
        # Clear the screen
        screen.fill((0, 0, 0))
        pygame.display.flip()

# Clean up
camera.release()
pygame.quit()
GPIO.cleanup()
