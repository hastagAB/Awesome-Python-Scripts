import requests 
from bs4 import BeautifulSoup as BS 
import xlwt
import time

	
def get_static_html ( search_url ) : 
	## create the soup object for the page 
	try:
		r_page = requests.get ( search_url )
	except:
		print("Connection refused by the server..")        
		time.sleep(5)
	soup_object = BS( r_page.content , 'html.parser' )
	#print ( soup_object.prettify() )
	return soup_object 

def get_url () : 
	## convert to query url , and get raw HTML for the page 
	show_name = input ( " Enter show name ")
	show_name = '+'.join ( show_name.split() ) 
	search_url = "https://www.imdb.com/find?ref_=nv_sr_fn&q="+ show_name + "&s=all"
	return search_url, show_name


def get_new_url ( soup_object ) : 
	## list of possible search results 
	list_queries = soup_object.find_all('td', class_ = "result_text") 

	show_final = None 
	## find the first TV show listing in the relevant searches
	for show in list_queries : 
		if "(TV Series)" in show.text : 
			show_final = show 
			break 

	if show_final == None : 
		print( " No relevant search ")
		exit()
	#print ( " Show found - " , show_final )

	## find the link to open the new page 
	hyperlink = show_final.find('a')
	url_change = hyperlink['href']

	show_url = "https://www.imdb.com/" + url_change + "episodes?season="
	return show_url 


def start() : 
	
	search_url , show_name = get_url() 
	soup_object = get_static_html(search_url)
	show_url = get_new_url(soup_object)
	result_file = xlwt.Workbook()
	
	season_number = 1 
	
	while True : 
		
		soup_object = get_static_html( show_url + str(season_number) )

		## verify if extra season exists
		verify_season = soup_object.find('h3' , attrs = {'id' :'episode_top'})
		curr_season =  int ( verify_season.text[6:] )  
		if not season_number == curr_season : 
			break
	
		print ("Season - ", season_number , " information extracted " )
		
		## excel file 
		result_sheet = result_file.add_sheet( verify_season.text , cell_overwrite_ok=True)
		result_sheet.write( 0 , 0 , " Name " )
		result_sheet.write( 0 , 1 , " Rating " )
		result_sheet.write( 0 , 2 , " Total votes " )
		result_sheet.write( 0 , 3 , " Summary " )
		result_sheet.col(3).width = 21000
		result_sheet.col(0).width = 10000
		
		episodes_season = soup_object.find_all('div' , class_ = 'info' )
		curr_episode = 1 
		for episode in episodes_season : 
			## get the name of the episode 
			name_episode = episode.find('strong')
			## get the rating of the episode
			rating_episode = episode.find('span' , class_ = 'ipl-rating-star__rating' )
			## total votes 
			votes_episode = episode.find('span' , class_ = 'ipl-rating-star__total-votes' )
			## summary 
			summary_episode = episode.find('div' , class_ = 'item_description' )
			
			## write to the excel file 
			if name_episode : 
				result_sheet.write( curr_episode , 0 , name_episode.text )
			if rating_episode : 
				result_sheet.write( curr_episode , 1 ,  rating_episode.text )
			if votes_episode : 
				result_sheet.write( curr_episode , 2 , votes_episode.text[1:-1] )
			if summary_episode : 
				result_sheet.write( curr_episode , 3 , summary_episode.text )
			curr_episode = curr_episode + 1 
		season_number = season_number + 1 
	
	print ( " Finished ")
	result_file.save( show_name.replace('+' , '_') + '.xls')

start() 