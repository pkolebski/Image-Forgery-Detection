import forgery_detect

"""
Main Code
"""

# example
# image_file = input("Enter image file name:")
image_file = "horse_fake.png"

forgery_detect.detect('../test_images/', image_file, '../output_images/', blockSize=32)
