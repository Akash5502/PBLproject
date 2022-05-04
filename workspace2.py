#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


img = cv2.imread('E:\img_1.png')


# In[3]:


img.shape


# In[4]:


img[0]


# In[5]:


import matplotlib.pyplot as plt


# In[6]:


plt.imshow(img)


# In[7]:


while True:
    cv2.imshow('result' ,img)
    if cv2.waitKey(2) == 27:
    #27 is the ASCII of Escape
        break
cv2.destroyAllWindows()


# In[8]:


haar_data = cv2.CascadeClassifier('C:\Anaconda\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')


# In[9]:


haar_data.detectMultiScale(img)


# In[10]:


# cv2.rectangle(img, (x,y), (w, h), (b,g,r), border_thickness)


# In[11]:


while True:
    faces = haar_data.detectMultiScale(img)
    for x,y,w,h in faces:
        cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,255), 4)
    cv2.imshow('result' ,img)
    if cv2.waitKey(2) == 27:
    #27 is the ASCII of Escape
        break
cv2.destroyAllWindows()


# In[12]:


capture = cv2.VideoCapture(0)
while True:
    flag, img = capture.read()
    if flag:
        faces = haar_data.detectMultiScale(img)
        for x,y,w,h in faces:
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 4)
        cv2.imshow('result', img)
        #27 - ASCII of Escape
        if cv2.waitKey(2) == 27:
            break
capture.release()
cv2.destroyAllWindows ()
#yes this is

# In[ ]: