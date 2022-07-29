import imgaug.augmenters as iaa
import cv2
import glob  #path of all images on folder


# 1. Load Dataset
images = []
images_path = glob.glob("images/*.jpg")
for img_path in images_path:
    img = cv2.imread(img_path)
    images.append(img) #put img inside images(loop to array)

# 2.Image Augmentation
augmentation = iaa.Sequential([
    #Rotate
    #iaa.Rotate((-30,30))

    # 1.Flip
    iaa.Fliplr(0.5), # Horizontal Flip
    iaa.Flipud(0.5),  #Vertical Flip

    # 2. Affine
    iaa.Affine(translate_percent={"x": (-0.2,0.2), "y": (-0.2,0.2)}, #translate percent= black bar ekliyor
               rotate=(-30,30),#rotate ediyor(döndürme)
               scale=(0.5,1.5) #Zoom out and in
               ),

    # 3. Multiply (Channels) #
    # brighter or darker
    iaa.Multiply((0.8,1.2)),



])
#Apply augmentation
augmentation_images = augmentation(images=images)

# 3. Show Augmented images
for img in augmentation_images:
    cv2.imshow("Image", img)
    cv2.waitKey(0)







# 3. Show Images
# for img in images:
#    cv2.imshow("Image", img)
#    cv2.waitKey(0)



