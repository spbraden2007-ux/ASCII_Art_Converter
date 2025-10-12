# Basic
# Choosing image from the folder which you want to convert into ascii art. 

# Set Up
import PIL.Image

# Initialize Ascii Character
ascii_chr = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize Image
def resize(image, new_width=100):
    width, height = image.size # Seeing image's size
    ratio = height / width # Finding ratio
    new_height = int(new_width*ratio)
    r_image = image.resize((new_width, new_height)) # Resized image
    return(r_image)

# Convert into gray scale
def grayify(image):
    g_s_image = image.convert("L") # Convert into grayify image
    return(g_s_image)

# Convert into pixel to ascii
def pixel_to_ascii(image):
    pixels = image.getdata() # Get value 
    characters = "".join([ascii_chr[pixel//25]for pixel in pixels]) # Defining ascii characters on pixel. 
    return(characters)

def main(new_width = 100): # Function to do every functions that I made. 
    path = "Sample.png" # Path of image and file name. 
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid. Try again.") # When path is incorrect. 

    # convert image to ascii
    new_image_data = pixel_to_ascii(grayify(resize(image)))

    # format
    pixel_count = len(new_image_data) # COunting Pixels. 
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width)) # Put ascii characters on new format image. 

    # Print Ascii 
    print(ascii_image) 

    # Saving into .txt file
    with open("SampleResult.txt", "w") as f:
        f.write(ascii_image)

main()
