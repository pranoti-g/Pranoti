#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = "pooja"
n1 = "pranoti"


# In[2]:


n


# In[3]:


n1


# In[5]:


n + " " + n1


# In[37]:


type(n)


# In[39]:


n.capitalize()


# In[42]:


n.center(2)


# In[47]:


n1.count


# In[49]:


n1.casefold()


# In[54]:


n.find


# In[7]:


#list


# In[10]:


lst = [2,4,6,8.1,["GPS",11,99]]


# In[11]:


lst


# In[12]:


lst[0]


# In[15]:


lst[4]


# In[16]:


lst[4][0]


# In[17]:


lst.append("PG")


# In[18]:


lst


# In[20]:


lst.index(4)


# In[25]:


lst.pop(-1)


# In[26]:


lst


# In[30]:


lst.count(1)


# In[35]:


lst.reverse()


# In[36]:


lst


# In[56]:


#DICT


# In[57]:


dit = {"name":"Pranoti", "age":"21", "occupation":"Student", "email":"pranoti@gmail.com"}


# In[58]:


dit


# In[60]:


dit.get("name")


# In[61]:


dit.items()


# In[62]:


dit.keys()


# In[63]:


dit.pop("occupation")


# In[64]:


dit


# In[65]:


dit["school"] = "SPS"


# In[66]:


dit


# In[71]:


dit.setdefault("name")


# In[72]:


#SETS


# In[73]:


st = {"PG","Rahata",1,3,5,7,9,1,3}


# In[74]:


st


# In[75]:


st1 = {"PG",1,3}


# In[76]:


st.intersection(st1)


# In[77]:


st1.isdisjoint(st)


# In[80]:


st1.difference(st)


# In[83]:


st.difference_update(st1)


# In[84]:


st.union(st1)


# In[85]:


st1.issubset(st)


# In[86]:


st.issubset(st1)


# In[88]:


st.issuperset(st1)


# In[89]:


#TUPLE


# In[90]:


tup = ("python", "#", "letsupgrade")


# In[91]:


tup


# In[93]:


tup.count("#")


# In[94]:


tup.index("python")


# In[ ]:




