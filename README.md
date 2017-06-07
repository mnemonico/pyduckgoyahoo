# pyduckgoyahoo
a very small api to get urls results from the search engines yahoo and duckduckgo for those aiming to scrap the results

Yahoo_object class and Duckduckgo_object class attributes are: 
title,name,snippet,description,url

Search example 
    import * from pyduckgoyahoo.py
    if __name__ == '__main__':
    
    resultas = []
    yahoo = PySearchYahoo()  
    query = "Donald Trump"  
    resultas =yahoo.search(query) #you can increment the number of page yahoo.search(query,2) [1,2,3,5] by default 1 page as result
    
    """
    resultas = []
    duck = PySearchDuckDuckgo()
    resultas = duck.search("Donald Trump") #you can define the size of result duck.search(query,15) [1-30] by default 30  results 
    """
    
    In[1]:resultas
    Out[1]: 
    [<__main__.Yahoo_object instance at 0x7f4d6bf59170>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59290>,
     <__main__.Yahoo_object instance at 0x7f4d6bf592d8>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59248>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59368>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59200>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59320>,
     <__main__.Yahoo_object instance at 0x7f4d6bf591b8>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59fc8>,
     <__main__.Yahoo_object instance at 0x7f4d6bf59d88>]
     
    In[2]:for res in resultas:
    print res.url
    Out[2]:
    https://www.donaldjtrump.com/
    https://en.wikipedia.org/wiki/Donald_Trump
    https://twitter.com/realdonaldtrump
    http://www.huffingtonpost.com/topic/donald-trump
    http://www.politico.com/news/donald-trump
    http://www.msnbc.com/topics/donald-trump
    http://www.trump.com/
    http://www.trump.com/biography/
    http://www.cnbc.com/donald-trump/
    https://www.theguardian.com/us-news/donaldtrump
