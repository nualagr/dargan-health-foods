# Python3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():

    for count, image in enumerate(os.listdir("viridian_images")):
        new_name = "viridian-" + image
        source_address = "viridian_images/" + image
        destination = "viridian_images/" + new_name

        # rename() function will
        # rename all the files
        os.rename(source_address, destination)


# Driver Code
if __name__ == "__main__":

    # Calling main() function
    main()
