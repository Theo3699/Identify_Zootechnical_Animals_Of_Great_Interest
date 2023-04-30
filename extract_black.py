from PIL import Image

# Open the original image
image = Image.open('cv\\testnonostrils_sobelx1.png')

# Define the darkness threshold for the pixels
threshold = 3

# Create a new black image with the same dimensions as the original image
black_image = Image.new('RGB', image.size, (0, 0, 0))

# Get the dimensions of the image
width, height = image.size

# Iterate through each pixel of the original image
for x in range(width):
    for y in range(height):
        # Get the pixel value at the current location
        pixel = image.getpixel((x, y))

        # Check if the pixel is darker than the threshold
        if pixel < threshold * 3:
            # If the pixel is dark, set the corresponding pixel in the black image to white
            black_image.putpixel((x, y), (255, 255, 255))

# Save the modified black image as a new file
black_image.save('cv\\modified_black_image.png')