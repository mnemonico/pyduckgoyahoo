#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 10:42:31 2017

@author: achrafbaiz
"""

import mechanize as mech
import requests
import urlparse 
from bs4 import BeautifulSoup



"""
br = mech.Browser()
br.set_handle_robots(False)
br.addheaders = [('User-agent','Mozilla/5.0')]
htmlresponse = br.open(url).read()
"""
class Yahoo_object:
    def __init__(self,title,name,snippet,description,url):
        self.title=title
        self.name=name
        self.snippet=snippet
        self.description=description
        self.url=url

class Duckduckgo_object:
    def __init__(self,title,name,snippet,description,url):
        self.title=title
        self.name=name
        self.snippet=snippet
        self.description=description
        self.url=url

class PySearchYahoo:
    
    urltype = "http://search.yahoo.com/search?p=%s"
    def __init__(self):
        pass
   
    def soup_object(self,query):     
        try:    
            htmlresponse = requests.get(self.urltype % query)
            encode = htmlresponse.encoding if 'charset' in htmlresponse.headers.get('Content-Type','').lower() else None
            if(encode is not None):   
                sp = BeautifulSoup(htmlresponse.text,from_encoding=encode)
                return sp
        except requests.ConnectionError:
            print "web site is down or doesn't existe at all !"

    def fetch_data(self,soup):
        list_of_results = []  
        inlis           = []
        if soup is not None:
            print "fetching data from yahoo! search engine"
            results = soup.find("div",attrs={"id":"web"})
            ol      = results.find("ol",attrs={"class":"mb-15 reg searchCenterMiddle"})      
            lis     = ol.find_all("li") 
            #description = lis[x].find("div",attrs={"class":"compText aAbs"}).getText()
            for lifs in lis:
                if lifs.text=='Cached':
                    continue
                inlis.append(lifs)   
            for li in inlis:
                if li is not None:
                    if li.h3 is None:
                        continue
                    titleorname  = li.h3.text
                    if li.find("div",attrs={"class":"compText aAbs"}) is None:
                        continue
                    descriptionorsnippet = li.find("div",attrs={"class":"compText aAbs"}).getText()
                    if li.a is None: 
                        continue
                    siteurl = li.a['href']
                    obj = Yahoo_object(titleorname,titleorname,descriptionorsnippet,descriptionorsnippet,siteurl)
                    list_of_results.append(obj)   
        return list_of_results
    
    def search(self,query,pages=1):
        final_list = list()
        soup       = self.soup_object(query)
        nexts      = self.parccour_pagination(soup)
        if(pages==1):
            # 1
          print "fetching results from %d page(s)" % pages
          final_list.extend(self.fetch_data(soup))
        elif(pages==2):
            # 1 + 2
          print "fetching results from %d page(s)" % pages
          #print nexts
          final_list.extend(self.fetch_data(soup)  + self.fetch_data(self.soup_object(nexts[0])))
        elif(pages==3):
            # 1 + 2 + 3
          print "fetching results from %d page(s)" % pages  
          final_list.extend(self.fetch_data(soup) + self.fetch_data(self.soup_object(nexts[0])) + self.fetch_data(self.soup_object(nexts[1])))
        elif(pages==4):
            # 1 + 2 + 3 + 4
          print "fetching results from %d page(s)" % pages  
          final_list = self.fetch_data(soup) + self.fetch_data(self.soup_object(nexts[0])) + self.fetch_data(self.soup_object(nexts[1])) + self.fetch_data(self.soup_object(nexts[2])) 
        elif(pages==5):
            # 1 + 2 + 3 + 4 + 5 
          print "fetching results from %d page(s)" % pages  
          final_list = self.fetch_data(soup) + self.fetch_data(self.soup_object(nexts[0])) + self.fetch_data(self.soup_object(nexts[1])) + self.fetch_data(self.soup_object(nexts[2]))  + self.fetch_data(self.soup_object(nexts[3])) 
        return final_list
        
    def parccour_pagination(self,soup):
        next_links = []
        pagination_section= soup.find('div',attrs={"class":"compPagination"})
        pagination_pages=pagination_section.find_all('a')
        for link in pagination_pages:
            next_links.append(link['href'].split('p=')[1])
        return next_links
    def main():
     pass


class PySearchDuckDuckgo:
    urltype = "http://duckduckgo.com/html/?q=%s"
    def __init__(self):
        pass
    def soup_object(self,query):     
        try:    
            htmlresponse = requests.get(self.urltype % query)
            encode = htmlresponse.encoding if 'charset' in htmlresponse.headers.get('Content-Type','').lower() else None
            if(encode is not None):   
                sp = BeautifulSoup(htmlresponse.text,from_encoding=encode)
                return sp
        except requests.ConnectionError:
            print "web site is down or doesn't existe at all !"
    def soup_object_mechanize(self,query):

        br     = mech.Browser()
        br.set_handle_robots(False) # ignore handling robots
        results = br.open(self.urltype % query)
        return results
    
    def fetch_data(self,soup):
        list_of_results = []  
        container       = []
        divs            = []
        if soup is not None:
            print "fetching data from Duck Duck Go search engine"
            container = soup.find("div",attrs={"id":"links"})
            divs      = container.find_all("div",attrs={"class":"links_main links_deep result__body"})     
            for div in divs:
                if div.h2 is None:
                    continue
                titleorname          = div.h2.getText()
                if div.find("a",attrs={"class":"result__snippet"}) is None:
                    continue
                descritpionorsnippet = div.find("a",attrs={"class":"result__snippet"}).getText()
                if div.find('a',attrs={"class":"result__url"}) is None:
                    continue
                url                  = "http://"+div.find('a',attrs={"class":"result__url"}).text.strip()
                obj = Duckduckgo_object(titleorname,titleorname,descritpionorsnippet,descritpionorsnippet,url)
                list_of_results.append(obj)    
            #title/name r[0].h2.getText()for i in range(0,quota):
            #description/snippet r[0].find("a",attrs={"class":"result__snippet"}).getText()
            #url r[0].find('a',attrs={"class":"result__url"}).text.strip()
            
        return list_of_results
    
    def search(self,query,quota=30):
        final_list = list()
        soup       = self.soup_object(query.replace(" ","+"))
        elements = self.fetch_data(soup)
        if quota <= len(elements):
            for i in range(0,quota):
                final_list.append(elements[i])
            del elements
        else :
            for i in range(0,len(elements)):
                final_list.append(elements[i])
            del elements
        return final_list
        
#====================================

if __name__ == '__main__':
    """
    resultas = []
    yahoo = PySearchYahoo()  
    query = "Donald Trump"  
    resultas =yahoo.search(query)
    """
    
    resultas = []
    duck = PySearchDuckDuckgo()
    resultas = duck.search("Donald Trump")
    

#====================================    
        