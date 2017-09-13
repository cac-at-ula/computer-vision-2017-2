import fire
import numpy as np
from tqdm import tqdm
from glob import glob
from os.path import join
from skimage import io

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
    
    def segment_image(self, im, color_space):
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
    
    def eval_mask(self, gt, mask):
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
        


    def process_dataset(self, dataset, color_space):
        """ Process the full dataset 
        :param dataset: Dicctionary that contains all dataset filenames
        :param color_space: Color space required for segmentation
        :returns: None
        """
        TP = 0
        TN = 0
        FP = 0
        FN = 0
        for ip in tqdm(dataset):
            im = io.imread(ip['train'])
            gt = io.imread(ip['gt'])
            mask = self.segment_image(im, color_space)
            (tp, tn, fp, fn) = self.eval_mask((gt==255), mask)
            TP += tp
            TN += tn
            FP += fp
            FN += fn
        precision = TP/(TP+FP)
        accuracy = (TP + TN)/ (TP + TN + FP +FN)
        recall = TP/(TP+FN)
        print('Precision = ', precision)
        print('Accuracy = ',accuracy) 
        print('Recall = ', recall)
        print('F-measure = ', 2 * (precision * recall)/(precision+recall))


    def eval(self, path, color_space='RGB'):
        """ Segmentation evaluation on training dataset
        :param path: Dataset path
        :param color_space: Select segmentation color space
        :returns: None
        """
        dataset = self.read_dataset(path)
        self.process_dataset(dataset, color_space)

if __name__ == "__main__":
    fire.Fire(Eval)
       
