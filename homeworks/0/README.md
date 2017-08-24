# Homework #1


- Due: Wednesday 29, August, 2017

## Description

The first homework consist in programming a method to read image filenames in folders. The search can be recursive. 

## Instructions

Fill the method read\_images\_filename from CVHelper

```
def read_images_filename(self,  folder_path, recursive=False):
        """Reads images filename in a folder

        :folder_path: Folder path that contains the images 
        :recursive: Look inside subfolders
        :returns: List of image paths, e.g.,
        ['/path/to/im1.jpg', '/path/to/im2.png', '/path/to/img3.tiff']
        """
        #
        # Add code Here
        #
        pass
        #
        # End code
        #
          
```


## Tips

1. Check os.walk, os.listdir. Both are python packages
2. Test the code. For example, open a terminal in the folder of CVHelper.py and check the output

```
from CVHelper import CVHelper

path = 'path/images'
 
cvhelper = CVHelper()
image_list = cvhelper.read_images_filename(path, False)
print(image_list)
```
3. You can extract test_images.zip to test the method

## Evaluation

1. 3 if non-recursive search is working
2. 6 if non-recursive and recursive search are working
3. 7 if 1 and 2, plus clear code, good comments

## Submission

1. Submissions are through Platea.
2. Submission must include just the file CVHelper.py compressed as a zip file
3. The zip file must be named homework_0_rut.zip







