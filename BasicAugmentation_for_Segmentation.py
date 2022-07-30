import imgaug.augmenters as iaa
import cv2
import glob  #path of all images on folder
import os

# 1. Load Dataset
images = []
images_path = glob.glob("images/images/*.jpg")
masks = []
masks_path = glob.glob("images/renklimask/*.png")

for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img) #put img inside images(loop to array)

for mask_path in masks_path:
    mask = cv2.imread(mask_path, cv2.COLOR_BGR2RGB)
    masks.append(mask)

# 2.Image Augmentation
augmentation = iaa.Sequential([
    #Rotate
    #iaa.Rotate((-30,30))

    # 1.Flip
    iaa.Fliplr(0.5), # Horizontal Flip
    iaa.Flipud(0.5),  #Vertical Flip

    # 2. Affine
    iaa.Affine(translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, #translate percent= black bar ekliyor
               rotate=(-30, 30),#rotate ediyor(döndürme)
               scale=(0.5, 1.5) #Zoom out and in
               ),

    # 3. Multiply (Channels) #
    # brighter or darker
    iaa.Multiply((0.8, 1.2)),

    # 4. Linearcontrast (Contrast)
    iaa.LinearContrast((0.6, 1.4)),




])
i = 0
# 3. Show Augmented images
#while True: #İnfinite Loop
def read_files(root_path, file_extension='.png'):
    image_names = list()
    images = list()
    for root, subdirectories, files in os.walk(root_path):
        for f in sorted(files):
            fp = os.path.join(root, f)
            if f.endswith(file_extension):
                image_names.append(f)
                images.append(cv2.imread(fp))

    return image_names, images

images_names, imagess = read_files(root_path='images/images/', file_extension='.jpg')
masks_names, maskk = read_files(root_path='images/renklimask/', file_extension='.png')

# Apply augmentation

augmentation_images,augmentation_masks = augmentation(images=images, segmentation_maps=masks)
#augmentation_images = augmentation(images=images)
#augmentation_masks = augmentation(images=masks)
for img in augmentation_images:
    cv2.imwrite('images/images-aug/augmente7' + images_names[i], img)
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    i = i + 1

i = 0
for mask in augmentation_masks:
    cv2.imwrite('images/mask-aug/augmente7' + masks_names[i], mask)
    print(mask.shape)
    #cv2.imshow("Image", mask)
    #cv2.waitKey(0)
    i = i + 1




