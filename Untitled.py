#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import re


# In[2]:


def extractSourceFileName(line):
    if re.findall('The full include-list for',line):
        flag = True
        index_right = line.rfind(':')
        index_left = line.rfind('/')+1
        return line[index_left:index_right]
    else:
        return None


# In[3]:


def extractIncludeFileName(line):
    result = re.findall('".+"',line)
    if len(result) != 0:
        return result
    else:
        return re.findall('<.+>',line)


# In[4]:


def addIncludeFileToList(index,log):
    includeList = []
    while index < len(log):
        line = log[index]
        print("line: ",line)
        res = extractIncludeFileName(line)
        print("res:",res)
        if len(res) != 0:
            includeList.append(res[0])
            index = index + 1
        else:
            break
    return includeList,index
        
    


# In[19]:


def seveDict(fileDict):
    file = open('includefile.txt','w')
    for k,v in fileDict.items():
        file.write('The include-list for ' + k + ':' + '\n')
        for temp in v:
            file.write(temp+'\n')
        file.write('\n')
    file.close()


# In[73]:


def saveDictAndSub(fileDict):
    file = open('includeSubFile.txt','w')
    flag = '        '
    for k,v in fileDict.items():
        file.write('The include-list for ' + k + ':' + '\n')
        for temp in v:
            searchIncludeRelation(temp,fileDict,file,flag)
            
    file.close()


# In[78]:


def searchIncludeRelation(line,fileDict,file,flag):
    file.write(flag+line+'\n')
    fileName = re.findall('/*([A-Za-z0-9_]+\.*[pb]*\.h)',line)

    if(len(fileName) == 0):
        fileName = re.findall('<([A-Za-z0-9]+)>',line)
    print("fileName :")
    print(fileName[0])
    includeList = fileDict.get(fileName[0])
    if(includeList ==None):
        return
    for temp in includeList:
        searchIncludeRelation(temp,fileDict,file,flag+flag)
        
        
    


# In[55]:


def main():
    log = []
    fileDict = {}
    for line in open("tmp.txt"):
        log.append(line[:-1]) #line[:-1]
    i=0
    while i < len(log):
        line = log[i]
        fileName = extractSourceFileName(line)
        if(fileName != None):
            print(fileName)
            includeList,i = addIncludeFileToList(i+1,log)
            fileDict[fileName] = includeList
        i = i+1
    saveDictAndSub(fileDict)
    


# In[79]:


main()


# In[48]:


filedict


# In[25]:


filedict.get('private_data_proto.pb.h')


# In[28]:


re.findall('/([A-Za-z0-9_]+\.h)','<google/protobuf/generated_message_util.h>')


# In[63]:


key = re.findall('<([A-Za-z0-9]+)>','<str_ing>')


# In[77]:


re.findall('/*([A-Za-z0-9_]+\.*[pb]*\.h)', '"google/protobuf/repeated_field.h"')


# In[ ]:




