Image Test-Read Me
By Evan Tang

This project has two primary purposes:
  1. Detects the best fitting line via slope intercept format or polar
  coordinates.
  2. Detect how many circles or a fixed radius are in the image.

It takes a BMP image and outputs the results in the console on the
command prompt. For a quick demonstration, run main.py (For me thats python
main.py in terminal).

For further information on the files see below
  -main.py: executes the actual commands. No functions stored here
  -detection.py: where the detection function (slope, normal, and circle are
  stored). This is the primary part of the code
  -check_functions.py: executes the functions from detection.py and displays the
  output
  -edge_detection.py: utilizes a quick method to produce an image with only the
  edges present.
  -convert_values.py: transforms values from image space to parameter space
  -common.py: shared definitions.
  -read_file.py: converts a BMP file into a multidimensional array.
  -vote_functions.py: utilizes Hough space voting to find the solution.
All Rights Reserved Evan Tang 2019.
