from PIL import Image

# Function to convert an image to grayscale
def convert_to_grayscale(image_path):
    try:
        # Open the image
        image = Image.open(image_path)
        
        # Convert to grayscale
        grayscale_image = image.convert('L')
        
        # Save the grayscale image
        grayscale_image.save("grayscale_" + image_path)
        
        return grayscale_image
    except Exception as e:
        print(f"Error: {e}")
        return None

# Function to perform LSB and MSB steganography
def steganography_lsb_msb(cover_image, secret_image):
    try:
        # Create a new image for the stego image
        stego_image = Image.new('L', cover_image.size)
        
        # Get pixel data for both images
        cover_pixels = list(cover_image.getdata())
        secret_pixels = list(secret_image.getdata())
        
        # Initialize a list for stego pixels
        stego_pixels = []
        
        # Perform LSB and MSB steganography by swapping bits
        for cover_pixel, secret_pixel in zip(cover_pixels, secret_pixels):
            lsb_cover = cover_pixel & 0xFE  # Clear the LSB of the cover pixel
            msb_secret = (secret_pixel >> 7) & 1  # Get the MSB of the secret pixel
            stego_pixel = lsb_cover | (msb_secret << 7)  # Combine LSB of cover and MSB of secret
            stego_pixels.append(stego_pixel)
        
        # Put the stego pixels into the stego image
        stego_image.putdata(stego_pixels)
        
        # Save the stego image
        stego_image.save("stego_image.png")
        
        return stego_image
    except Exception as e:
        print(f"Error: {e}")
        return None

# Specify the paths to the cover and secret images
cover_image_path = "cover_image.jpg"
secret_image_path = "secret_image.jpg"

# Convert both images to grayscale
cover_grayscale = convert_to_grayscale(cover_image_path)
secret_grayscale = convert_to_grayscale(secret_image_path)

if cover_grayscale and secret_grayscale:
    # Perform LSB and MSB steganography
    stego_result = steganography_lsb_msb(cover_grayscale, secret_grayscale)
    
    if stego_result:
        print("Steganography complete. Stego image saved as stego_image.png.")
