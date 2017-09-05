# Homework #0.5


- Due: Thursday 7, September 2017.

## Description

This homework consists of constructing a software that changes the format of images from a given folder to another one. Additionally, it must support RGB to Grayscale conversion.

## Instructions

Using [Python Fire](https://github.com/google/python-fire) generate a command line interface with the following optional arguments.

1. **--folder (str)** Input folder that contains the images.
2. **--verbose (bool)** If true, print image filenames and running parameters. Else, don't show anything on the screen.
3. **--format (str)** Output format for each image.
4. **--output (str)** Output folder where the images are going to be stored.
5. **--grayscale (bool)** If true, convert each image to grayscale. *This must be done just using numpy methods*.
6. **--mosaic (true)** If true, generates a mosaic that contains all the images from the input folder (optional).

Everything must be implemented in CVHelper.py

## Tips

1. Ask

## Evaluation

1. 4 If format conversion works perfectly.
2. 6 if 1, and grayscale conversion works.
3. 7 if 1 and 2, plus clear code, good comments.
3. 7 if 1 and 2, plus mosaic.

## Submission

1. Submissions are through Platea.
2. Submission must include just the file CVHelper.py compressed as a zip file.
3. The zip file must be named homework_05_rut.zip. Rut in the format XXXXXXXX-X.
