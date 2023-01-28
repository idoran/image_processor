import matplotlib.pyplot as plot 
import os,cv2
import numpy as np



#process any data and convert it to 256x256px

# data_dir = 'data/Winter/'
# save_dir = 'data/save_winter/'
# def prepare_data(dataset_dir):
#     input_names=[]
#     for file in os.listdir(dataset_dir ):
#         input_names.append(dataset_dir + file)
#     input_names
#     return input_names
# def process_data():
#     filenames = prepare_data(data_dir)
#     if not os.path.isdir(save_dir):
#         os.makedirs(save_dir)
#     for i,file in enumerate(filenames):
#         #  read image
#         img = cv2.imread(file)
#         # for each image, resize its size
#         img = cv2.resize(img,(256,256))
#         file_name = os.path.basename(filenames[i])
#         # done processing, write the processed image into save_folder
#         cv2.imwrite(save_dir+file_name,img)
# if __name__ == '__main__':
#     process_data() 



#put any of the data in the directory in an array
data_dir = 'data/save_winter/'

hues= np.array([0])
saturation = np.array([0])

def prepare_data(dataset_dir):
    input_names=[]

    for file in os.listdir(dataset_dir ):
        input_names.append(dataset_dir + file)
    input_names

    return input_names




        
        
#read each image and append its hue and saturation values to their respective arrays
def process_data():
    global hues
    global saturation
    filenames = prepare_data(data_dir)

    for i,file in enumerate(filenames):

        #  read image
        src = cv2.imread(file)
        file_name = os.path.basename(filenames[i])

        
        # newImg = np.array([[None]*256] * 256)
        img = cv2.cvtColor(src, cv2.COLOR_BGR2HSV_FULL)
        
        for x in range(256):
            hues = np.append(hues, img[x][0]) 
            saturation = np.append(saturation,img[x][1])

        
    x=0

    
        

        
        

        

if __name__ == '__main__':
    process_data() 
    #plot the hue and saturation arrays into a histogram
    fig = plot.figure()

    xHues = np.array(hues)
    ySat = np.array(saturation)



    ax = fig.add_subplot(projection = '3d')
    
    histo, xedges, yedges = np.histogram2d(xHues, ySat, bins=[12,4])
    xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
    xpos = xpos.ravel()
    ypos = ypos.ravel()
    zpos = 0

    dx = dy =  10 * np.ones_like(zpos)
    dz = histo.ravel()
    ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
    ax.set_xlabel("Hues")
    ax.set_ylabel("Saturation")


    plot.show()
