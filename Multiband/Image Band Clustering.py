
# coding: utf-8

# # Import Libraries

# In[1]:


import tkinter as tk
import tkinter.filedialog
from PIL import ImageTk, Image
import os


# # Define Windows and Frames

# WINDOW SIZE

# In[20]:


root = tk.Tk()
root.title("Image Clustering")
root.geometry("700x700")


# FRAME TOP

# In[21]:


frame = tk.Frame(root)
frame.pack(side=tk.TOP)


# FRAME LEFT&RIGHT

# In[22]:


frameLeft = tk.Frame(root)
frameLeft.configure(width=350)
frameLeft.grid_propagate(0)
frameLeft.pack(side=tk.TOP)
frame2 = tk.Frame(root)
frame2.pack(side=tk.TOP)
frameRight = tk.Frame(root,width=350)
frameRight.pack(side=tk.TOP)


# # Title and Labels

# In[23]:





paths = []
title = tk.Label(frame,text="MULTIBAND IMAGE CLUSTERING")
title.config(font=("Courier",30))
title.pack(side=tk.TOP)
label1 = tk.Label(frameLeft,text="Insert Image")
label1.config(font=("Calibri",14))
label1.pack(side=tk.TOP)
label2 = tk.Label(frameRight,text="Processed Image")
label2.config(font=("Calibri",14))
label2.pack(side=tk.TOP)
labelInput = tk.Label(frame2,text="Number of Clusters : ")
labelInput.pack(side=tk.LEFT)
entry = tk.Entry(frame2,bd=5)
entry.pack(side=tk.LEFT)


# # Methods

# In[24]:


def getFileName(image):
    print(image)
def browseFile():    
    file = tk.filedialog.askdirectory()
    print(file)
    print("test")
    for images in os.listdir(file):
        print(os.listdir(file))
        if images.endswith("GIF"):
            print(images)
            imgpath = os.path.join(file,images)
            paths.append(imgpath)
            im = Image.open(imgpath)
            resized = im.resize((100,100),Image.ANTIALIAS)
            tkimage = ImageTk.PhotoImage(resized)
#             handler = lambda img = images: getFileName(img)  #here modify
            imageLabel = tk.Label(frameLeft, image=tkimage)#here
            imageLabel.config(width=100,height=100)
            imageLabel.image=tkimage
            imageLabel.pack(expand="true",side=tk.LEFT)
def sendPath():
      cluster = entry.get()
      clusterText = tk.Label(frameRight,text = "Number of Cluster = "+cluster)
      clusterText.pack(side=tk.LEFT)
      print(cluster)
      print(paths)
      


# # Buttons

# In[25]:


# inputLabel = tk.Label()
fileButton = tk.Button(frameLeft,text = "Browse",command=browseFile)
fileButton.pack(side=tk.BOTTOM)
processButton = tk.Button(frameRight,text = "Process",command = sendPath)
processButton.pack(side=tk.BOTTOM)
# print(paths)
root.mainloop()

