#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[4]:


import cv2
import matplotlib.pyplot as plt
gray_image =cv2.imread('car.png',0)
cv2.imshow('gray_image',gray_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[5]:


import cv2
import matplotlib.pyplot as plt
color_image =cv2.imread('car.png',-1)
cv2.imshow('color_image',color_image) 
cv2.waitKey(0) 
cv2.destroyAllWindows()


# In[6]:


hist = cv2.calcHist([gray_image],[0],None,[256],[0,255])


# In[7]:


h1 = cv2.calcHist([color_image],[0],None,[256],[0,255]) 


# In[8]:


h2 = cv2.calcHist([color_image],[1],None,[256],[0,255]) 


# In[9]:


h3 = cv2.calcHist([color_image],[2],None,[256],[0,255]) 


# In[10]:


equ_img = cv2.equalizeHist(gray_image)


# In[11]:


plt.figure()
plt.title("Histogram")
plt.xlabel('Blue value')
plt.ylabel('Pixel count')
plt.stem(h1)
plt.show()


# In[12]:


plt.figure()
plt.title("Histogram")
plt.xlabel('Green value')
plt.ylabel('Pixel count')
plt.stem(h2)
plt.show()


# In[13]:


plt.figure()
plt.title("Histogram")
plt.xlabel('Red value')
plt.ylabel('Pixel count')
plt.stem(h3)
plt.show()


# In[19]:


plt.figure()
plt.title("Histogram")
plt.xlabel('Grayscale value')
plt.ylabel('Pixel count')
plt.stem(hist)
plt.show()


# In[21]:


plt.figure()
plt.title("Histogram")
plt.xlabel('Grayscale value')
plt.ylabel('Pixel count')
plt.stem(hist)
plt.show()


# In[ ]:




