# CircuitPython test program for M5Stick Plus 2
# Adapted from the LilyGO T-Display test program.
# 10-1-24 MicroDevSteve
# https://www.youtube.com/@MicroDevSteve
# https://github.com/MicroDev-Steve/Circuitpython_m5stickplus2

import time
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_st7789

# Release any existing display resources
displayio.release_displays()

# Define display pins
tft_clk = board.LCD_CLK  # Clock pin
tft_mosi = board.LCD_MOSI  # MOSI pin
tft_cs = board.LCD_CS  # Chip Select pin
tft_dc = board.LCD_DC  # Data/Command pin
tft_rst = board.LCD_RST  # Reset pin
tft_bl = board.LCD_BCKL  # Backlight pin

# Set up SPI bus for display communication
tft_spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)
display_bus = displayio.FourWire(tft_spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)

# Initialize the ST7789 display
display = adafruit_st7789.ST7789(
    display_bus,
    width=135,
    height=240,
    rowstart=40,
    colstart=53,
    backlight_pin=tft_bl
)

# Create the display context (splash)
splash = displayio.Group()
display.root_group = splash

# Create a background color bitmap
color_bitmap = displayio.Bitmap(display.width, display.height, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF7F7F  # Background color

# Create a background sprite and add it to the splash group
bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Box 1: Green
inner_bitmap1 = displayio.Bitmap(120, 67, 1)
inner_palette1 = displayio.Palette(1)
inner_palette1[0] = 0x2E8B57  # Green
inner_sprite1 = displayio.TileGrid(inner_bitmap1, pixel_shader=inner_palette1, x=0, y=0)
splash.append(inner_sprite1)

# Box 2: Blue
inner_bitmap2 = displayio.Bitmap(120, 67, 1)
inner_palette2 = displayio.Palette(1)
inner_palette2[0] = 0x0000FF  # Blue
inner_sprite2 = displayio.TileGrid(inner_bitmap2, pixel_shader=inner_palette2, x=120, y=0)
splash.append(inner_sprite2)

# Box 3: Cyan
inner_bitmap3 = displayio.Bitmap(120, 68, 1)
inner_palette3 = displayio.Palette(1)
inner_palette3[0] = 0x00FFFF  # Cyan
inner_sprite3 = displayio.TileGrid(inner_bitmap3, pixel_shader=inner_palette3, x=0, y=67)
splash.append(inner_sprite3)

# Box 4: Purple
inner_bitmap4 = displayio.Bitmap(120, 68, 1)
inner_palette4 = displayio.Palette(1)
inner_palette4[0] = 0x800080  # Purple
inner_sprite4 = displayio.TileGrid(inner_bitmap4, pixel_shader=inner_palette4, x=120, y=67)
splash.append(inner_sprite4)

# Function to create and display text
def create_text(label_text, position_x, position_y, color):
    text_area = label.Label(terminalio.FONT, text=label_text, color=color)
    text_group = displayio.Group(scale=2, x=position_x, y=position_y)
    text_group.append(text_area)  # Add text to the group
    splash.append(text_group)  # Add the text group to the splash

# Draw labels
create_text("Hello", 40, 100, 0xDC143C)  # Red color
create_text("World", 40, 150, 0xEEE00)   # Yellow color

# Main loop (keeps the program running)
while True:
    pass
