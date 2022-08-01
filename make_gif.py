import argparse
import os
import glob
from PIL import Image
import imageio
import numpy as np

def to8b(x):
    return (255 * np.clip(x, 0, 1)).astype(np.uint8)


def make_gif(name, dir_path, iter):
    img_paths = glob.glob(os.path.join(dir_path, 'images/*coarse_raycolor.png'))
    # img_paths = glob.glob(os.path.join(dir_path, 'images/*gt_image.png'))
    img_paths.sort()
    img_list = []

    for img_path in img_paths:
        image = np.asarray(Image.open(img_path))
        image = (image / 255).astype(np.float32)
        img_list.append(image)
    
    print(img_paths)

    stacked_imgs = [to8b(np_img) for np_img in img_list]
    file_name = 'video_{:04d}_{}.gif'.format(iter, name)
    # file_name = 'video_gt_{}.gif'.format(iter, name)
    imageio.mimwrite(os.path.join(dir_path, 'vids', file_name), stacked_imgs, fps=1, format='GIF')
    
    print("FINISHED GENERATING GIF!!!")

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='name of the dataset')
    parser.add_argument('--dir_path', help='directory of the test results')
    parser.add_argument('--iter', type=int, help='which iteration')
    args = parser.parse_args()

    make_gif(args.name, args.dir_path, args.iter)