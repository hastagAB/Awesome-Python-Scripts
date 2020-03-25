import requests, bs4

def get_topic():
	'''Get a topic to download from user.'''

	topic_list = ['comics', 'books', 'art', 'culture', 'film', 'food', 'gaming', 'humor', 'internet-culture', 'lit', 'medium-magazine', 'music', 'photography', 'social-media', 'sports', 'style', 'true-crime', 'tv', 'writing', 'business', 'design', 'economy', 'startups', 'freelancing', 'leadersip', 'marketing', 'productivity', 'work', 'artificial-intelligence', 'blockchain', 'cryptocurrency', 'cybersecurity', 'data-science', 'gadgets', 'javascript', 'macine-learning', 'math', 'neuroscience', 'programming', 'science', 'self-driving-cars', 'software-engineering', 'space', 'technology', 'visual-design', 'addiction', 'creativity', 'disability', 'family', 'health', 'mental-health', 'parenting', 'personal-finance', 'pets', 'psychedelics', 'psychology', 'relationships', 'self', 'sexuality', 'spirituality', 'travel', 'wellness', 'basic-income', 'cities', 'education', 'environment', 'equality', 'future', 'gun-control', 'history', 'justice', 'language', 'lgbtqia', 'media', 'masculinity', 'philosophy', 'politics', 'race', 'religion', 'san-francisco', 'transportation', 'women', 'world']
	print('Welcome to Medium aricle downloader by @CoolSonu39!')
	choice = 'some-random-topic'
	print('Which domain do you want to read today?')
	while choice not in topic_list:
	    print("Enter 'list' to see the list of topics.")
	    choice = input('Enter your choice: ')
	    if choice == 'list':
	        print()
	        for i in topic_list:
	            print(i)
	        print()
	    elif choice not in topic_list:
	        print('\nTopic' + choice + 'not found :(')
	return choice


def extract_links(url):
	'''Extract article links from url'''

	html_response = requests.get(url)
	parsed_response = bs4.BeautifulSoup(html_response.text, features='html5lib')
	article_list = parsed_response.select('h3 > a')
	return article_list


def medium_text(url):
	'''Extract text from a medium article link.'''

	html_response = requests.get(url)
	parsed_response = bs4.BeautifulSoup(html_response.text, features='html5lib')
	tag_list = parsed_response.find_all(['h1', 'p', 'h2'])

	extracted_text = ''
	for j in range(len(tag_list)):
		extracted_text += tag_list[j].getText() + '\n\n'

	return extracted_text