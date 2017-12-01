import fire
import numpy as np
from tqdm import tqdm
from glob import glob
from os.path import join
from skimage import io
from skimage.measure import label, regionprops
from joblib import Parallel, delayed
from collections import namedtuple 

Rect  = namedtuple('Rectangle','xmin ymin xmax ymax')

class Eval(object):
    """Eval traffic sign dataset """

    def __init__(self):
        pass

    def read_dataset(self, path):
        """ Read dataset images filename
        :param path: Path were the dataset is stored
        :returns: A dictionary with the dataset filenames
        """ 
        # train
        train_l = glob(join(path,'train','*.jpg'))
        dataset = [{'train':t, 'gt':t.replace('train','train_masks')} for t in train_l]
        return dataset
    
    @staticmethod
    def rect_inter_area(a,b):
        """Computes the intersecting area between two rectangles, a and b
        :param a: First rectangle
        :param b: Second rectangle
        :returns: Intersecting area
        """
        dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
        dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
        if (dx>=0) and (dy>=0):
            return dx*dy

    @staticmethod
    def rect_area(a):
        """Computes the area of a rectangle
        :param a: Rectangle
        :returns: Area of the rectangle 
        """
        dx = a.xmax -a.xmin
        dy = a.ymax -a.ymin
        if (dx>=0) and (dy>=0):
            return dx*dy
        return 0

    @staticmethod
    def segment_image(im, color_space):
        """Segments an image using a given color space 
        :param im: Input image (x,x,3) 
        :param color_space: Color space required for segmentation
        :returns: uint8 mask. 255 true, 0 False
        """
        ## Add Segmentation code HERE
        if color_space == 'RGB':
            pass
        return np.ones(im.shape[:2]).astype(np.bool)
        ## Code ends
    
    @staticmethod
    def eval_mask(gt, mask):
        """ Eval mask
        :param gt: Groundtruth mask (binary values)
        :param mask: Obtained mask (binary values)
        :returns: tp, tn, fp, fn in pixels
        """
        tp_m = (gt==1) & (mask==1)
        tn_m = (gt==0) & (mask==0)
        fp_m = (gt==0) & (mask==1)
        fn_m = (gt==1) & (mask==0)
        return (tp_m.sum(), tn_m.sum(), fp_m.sum(), fn_m.sum()) 

    @staticmethod
    def eval_recognition(bb_sol, bb_mask):
        """ Eval mask
        :param bb_sol: List of Rect bounding boxes obtained after classification 
        :param bb_mask: List of Rect bounding boxes from the GT mask
        :returns: tp, tn, fp, fn in windows  
        """
        used_mask = []
        tp = 0 
        for bb_s in bb_sol:
            for i, bb_m in enumerate(bb_mask):
                if i not in used_mask:
                    if Eval.rect_inter_area(bb_s,bb_m) > 0.5 * Eval.rect_area(bb_m) and \
                       Eval.rect_area(bb_s) < 1.5 * Eval.rect_area(bb_m):
                        tp += 1
                        used_mask.append(i)
        fn = len(bb_mask) - tp
        fp = len(bb_sol) - tp
        return (tp, fp, fn)

    @staticmethod
    def classify(im, mask):
        """ Classification of blobs
        :im: Image with traffic signs
        :mask: Mask after segmentation
        :returns: List of bounding boxes

        """
        return []

    @staticmethod
    def process_image(ip, color_space):
        """ Process one image
        :param ip: name of train and gt image files
        :returns: (tp,tn,fp,fn) 
        """
        # Segment image

        im = io.imread(ip['train'])
        gt = io.imread(ip['gt'])
        mask = Eval.segment_image(im, color_space)
        
        # Eval Segmentation
        (tp, tn, fp, fn) = Eval.eval_mask((gt>200), mask)

        # Classify blobs
        bb_sol = Eval.classify(im, mask)

        # Get bounding boxes from GT
        bb_mask = []
        label_im = label(gt>200)
        props = regionprops(label_im)
        for p in props:
            props = Rect(xmin=p.bbox[0], ymin=p.bbox[1], xmax=p.bbox[2], ymax=p.bbox[3])
            bb_mask.append(props)

        # Eval Traffic sign recognition
        (tp_r, fp_r, fn_r) = Eval.eval_recognition(bb_sol, bb_mask)
        return (tp, tn, fp, fn, tp_r, fp_r, fn_r)

    def process_dataset(self, dataset, color_space, njobs):
        """ Process the full dataset 
        :param dataset: Dicctionary that contains all dataset filenames
        :param color_space: Color space required for segmentation
        :param njobs: Number of cores
        :returns: None
        """
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        TP_r = 0
        FP_r = 0
        FN_r = 0

        res = Parallel(n_jobs=njobs, verbose=5)(delayed(Eval.process_image)(ip, color_space) for ip in dataset)
        for r in res: 
            TP += r[0]
            TN += r[1]
            FP += r[2]
            FN += r[3]
            TP_r += r[4]
            FP_r += r[5]
            FN_r += r[6]
        
        # Segmentation
        precision = TP/(TP+FP)
        accuracy = (TP + TN)/ (TP + TN + FP +FN)
        recall = TP/(TP+FN)
        print('\nSegmentation\n')
        print('Precision = ', precision)
        print('Accuracy = ',accuracy) 
        print('Recall = ', recall)
        print('F-measure = ', 2 * (precision * recall)/(precision+recall))
        
        # Recognition  
        if TP_r+FP_r == 0:
            print('\nRecognition\n')
            print('Precision = 0')
            print('Accuracy = 0') 
            print('Recall = 0')
            
        else:
            precision = TP_r/ (TP_r + FP_r)
            accuracy = TP_r /(TP_r + FN_r)
            recall = TP_r / (TP_r + FN_r + FP_r)
            print('\nRecognition\n')
            print('Precision = ', precision)
            print('Accuracy = ',accuracy) 
            print('Recall = ', recall)

    def eval(self, path, njobs=8, color_space='RGB'):
        """ Segmentation evaluation on training dataset
        :param path: Dataset path
        :param color_space: Select segmentation color space
        :returns: None
        """
        dataset = self.read_dataset(path)
        self.process_dataset(dataset, color_space, njobs)

if __name__ == "__main__":
    fire.Fire(Eval)
       
