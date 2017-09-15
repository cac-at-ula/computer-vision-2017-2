# PBL #0

- Due: Sunday 1, October, 2017

## Description

The PBL #0 (Stage-1) consists in segment traffic signs using color clues

## Instructions

Fill the method *segment_image* from train.py

```
def segment_image(self, im, color_space):
  """Segments an image using a given color space 
  :param im: Input image (x,x,3) 
  :param color_space: Color space required for segmentation
  :returns: uint8 mask. 255 true, 0 False
  """
  ## Add Segmentation code HERE
  if color_space == 'RGB':
    pass
  # This line must be removed after implementing the method
  return np.ones(im.shape[:2]).astype(np.bool)
  ## Code ends
```


## Tips

1. Try hard

## Run code

An example

```bash
python3 train.py eval --path=dataset_folder --color-space=RGB 
```

## Evaluation

Grade = 0.5Code * 0.5 Presentation

#### Code

1. 1 If nothing works
2. 4 If RGB segmentation is working (mandatory)
3. 5 If RGB plus 1 other color space is working (HSV, LAB, ...) (optional)
4. 6 If RGB plus 2 other color space are working (HSV, LAB, ...) (optional)
5. Optionals + mandatory + good quality code

#### Presentation (1 slide per item)

1. Used approach. How you solve the RGB segmentation
2. Analysis of metrics. What means each metric and why you choose one to optimize
3. Results of RGB segmentation
4. Optionals
5. Comment and conclusions

## Submission

1. Submissions are through Platea.
2. Submission must include just the file train.py compressed as a zip file
3. The zip file must be named pbl_0_rut.zip







