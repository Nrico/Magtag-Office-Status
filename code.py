import time
import board
import terminalio
from adafruit_magtag.magtag import MagTag

# Initialize MagTag and clear the screen
magtag = MagTag()
magtag.set_background(0xFFFFFF)  # white background

# Status messages
STATUSES = [
    "In Office",
    "Out of Office",
    "Back in 15 min",
    "Out to Lunch",
    "Gone rest of day"
]

# Set the default status
current_status = 0  # "In Office"

# Add the "Enrico is" text field near the top
magtag.add_text(
    text_font=terminalio.FONT,
    text_position=(
        magtag.graphics.display.width // 2,  # Centered horizontally
        10  # Near the top
    ),
    text_scale=2,
    text_anchor_point=(0.5, 0.5)  # Center alignment
)

# Add main status text field
magtag.add_text(
    text_font=terminalio.FONT,
    text_position=(
        magtag.graphics.display.width // 2,  # Centered horizontally
        magtag.graphics.display.height // 2   # Centered vertically
    ),
    text_scale=3,
    text_anchor_point=(0.5, 0.5)  # Center alignment
)

# Add button labels just above the buttons at the bottom
magtag.add_text(
    text_font=terminalio.FONT,
    text_position=(3, 120),
    text_scale=1,
)

# Set text for each field
magtag.set_text("Enrico is", 0)  # "Enrico is" at the top
magtag.set_text(STATUSES[current_status], 1)  # Initial status
magtag.set_text("in/out      15 min       lunch     out for day", 2)  # Button labels

# Function to display the main status message
def display_status(status_index):
    magtag.set_text(STATUSES[status_index], 1)  # Update the main status
    magtag.refresh()
    time.sleep(3)  # Give some time for the screen to update

# Initial display (optional since we've already set it above)
# display_status(current_status)

# Main loop
while True:
    if magtag.peripherals.button_a_pressed:  # Button A is pressed
        if current_status == 0:  # If "In Office"
            current_status = 1  # Change to "Out of Office"
        else:
            current_status = 0  # Change back to "In Office"
        display_status(current_status)

    elif magtag.peripherals.button_b_pressed:  # Button B is pressed
        current_status = 2
        display_status(current_status)

    elif magtag.peripherals.button_c_pressed:  # Button C is pressed
        current_status = 3
        display_status(current_status)

    elif magtag.peripherals.button_d_pressed:  # Button D is pressed
        current_status = 4
        display_status(current_status)

    time.sleep(0.1)  # Just a small delay to prevent busy-waiting
