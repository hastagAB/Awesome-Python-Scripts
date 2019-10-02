
# coding: utf-8

# In[3]:


def wordFreq(string):
    word_count = {}
    word_bank = string.split()
    for word in word_bank:
        word = word.lower()
        if word.isalpha():
            if word in word_count:
                word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
    return word_count

