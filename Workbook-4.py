#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image 


# In[3]:


mac = Image.open("example.jpg","r")


# In[4]:


type(mac)


# In[7]:


mac


# In[8]:


mac.size


# # Croping Images

# In[14]:


mac.crop((0,0,100,100))


# In[15]:


pencils = Image.open("pencils.jpg")


# In[16]:


pencils


# In[17]:


pencils.size


# In[25]:


x = 0 
y = 0 
width = 1950/3 
height = 1300


# In[19]:


pencils.crop((x,y,width,height))


# In[27]:


crop_size = (x,y,width,height)


# In[28]:


pencils.crop(crop_size)


# In[30]:


mac.size


# In[31]:


halfway = 1993/2


# In[33]:


x = halfway - 200 
w = halfway + 200 
y = 800
h = 1257

mac.crop((x,y,w,h))


# In[34]:


computer = mac.crop((x,y,w,h))


# In[35]:


computer


# In[38]:


mac.paste(computer,(0,0))


# In[39]:


mac


# In[40]:


mac.size


# In[42]:


mac.resize((3000,5000))


# In[44]:


mac.rotate(360)


# # Color Transparency

# In[74]:


red = Image.open("red_color.jpg")


# In[75]:


red


# In[76]:


red.putalpha(150)


# In[77]:


red


# In[78]:


blue = Image.open("blue_color.png")


# In[79]:


blue


# In[85]:


blue.paste(red,(0,0),red)


# In[87]:


blue


# In[ ]:




