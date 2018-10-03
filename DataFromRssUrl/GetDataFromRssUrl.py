'''
Dependencies:-
    feedparser             pip3 install feedparser
'''
import traceback, sys, re
from bs4 import BeautifulSoup
from datetime import datetime
import json
import feedparser
import requests
class GetPostFromUrl():
    def __init__(self):
        self.completed_urls = {}

    def initialize(self, parameters):
        self.user_urls = parameters.get('urls_of_sites',[])
        self.limit = 2
        self.results = []


    def get_results(self):
        for rss_url in self.user_urls:
            #print("RSS_URL:",rss_url)
            try:
                if rss_url not in self.completed_urls:
                    rss_data = feedparser.parse(rss_url)
                    self.transform(rss_url, rss_data)
                else:
                    self.results.extend(self.completed_urls[rss_url])
            except Exception as e:
                print("Exception from get_results method in GetPostFromUrl : ",e)
        return self.results


    def transform(self,rss_url,result_data):
        no_of_posts = 0
        data = []
        for each_post in result_data["entries"]:
            output = {}
            output["page_url"] = rss_url
            output["source_url"] = rss_url
            rss_url_name = rss_url.replace("http://","")
            rss_url_name = rss_url_name.replace("www.", "")
            output["page_name"] = rss_url_name
            if "description" in each_post:
                output["post_description"] = BeautifulSoup(each_post["description"],"html.parser").text
            else:
                output["post_description"] = ''
            if "title" in each_post:
                output["post_title"] = each_post["title"]
            else:
                output["post_title"] = ''
            if "link" in each_post:
                if "alerts/feeds" in rss_url:
                    remove_string = each_post["link"].find("&ct=")
                    original_post_url = each_post["link"][42:remove_string]
                    output["post_url"] = original_post_url
                else:
                    output["post_url"] = each_post["link"]
            else:
                output["post_url"] = ''
            output["post_type"] = "link"
            output["post_id"] = Utils.get_hash_code(output["post_url"])
            self.height,self.width = 0,0
            if "summary_detail" in each_post and bool(BeautifulSoup(each_post["summary_detail"]["value"], "html.parser").find()):
                image_details = BeautifulSoup(each_post["summary_detail"]["value"], 'html.parser')
                if image_details.find_all("img"):
                    for every_image_tag in image_details.find_all("img"):
                        if every_image_tag.get("src"):
                            output["post_image_url"] = every_image_tag["src"]
                            self.height = every_image_tag.get("width")
                            self.width = every_image_tag.get("height")
                            break
                        else:
                            output["post_image_url"] = ""
                else:
                    output["post_image_url"] = ""
            elif "content" in each_post and bool(BeautifulSoup(each_post["content"][0]["value"], "html.parser").find()):
                image_details = BeautifulSoup(each_post["content"][0]["value"], 'html.parser')
                if image_details.find_all("img"):
                    for every_image_tag in image_details.find_all("img"):
                        if every_image_tag.get("src"):
                            self.height = every_image_tag.get("height")
                            self.width = every_image_tag.get("width")
                            output["post_image_url"] = every_image_tag["src"]
                            break
                        else:
                            output["post_image_url"] = ""
                else:
                    output["post_image_url"] = ""
            else:
                output["post_image_url"] = ""
            if "published" in each_post:
                output["created_at"] = each_post["published"]
            else:
                output["created_at"] = ''
            if output:
                self.results.append(output)
                data.append(output)
                no_of_posts+=1
            if no_of_posts>=self.limit:
                break
        #print(len(self.results))
        if data:
            self.completed_urls[rss_url] = data

    def store_results(self,output):
        filename = "GetPostFromUrl" + ("_".join(str(datetime.now()).split(" "))).replace(":","-") + ".json"
        with open(filename,"w") as f:
            json.dump(output,f,indent=2)
        f.close()




if __name__ == '__main__':

    parameters = {}
    parameters['urls_of_sites'] = ['https://www.google.co.in/alerts/feeds/00658181146524679235/12925205973984843373']
    obj = GetPostFromUrl()
    obj.initialize(parameters)
    results = obj.get_results()
    print(json.dumps(results))
    #obj.store_results(results)
