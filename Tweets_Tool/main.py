import sys
assert sys.version_info >= (3, 0)
import pandas as pd
import numpy as np
from multiprocessing.pool import ThreadPool
import Tool


def main(filepath):
	assert isinstance(filepath, str)
	videogames = pd.read_csv(filepath, skiprows=1, names=['games', 'start_date', 'end_date'])
	videogames = videogames.values
	pool = ThreadPool(250)
	text_results = pool.map(Tool.TweetObtain().TweetObtain_function,
	                        videogames)
	pool.close()
	pool.join()
	text_results = pd.DataFrame(
	    np.vstack(text_results))
	text_results.to_csv('tweets.csv')
	return

if __name__ == "__main__":
	main(sys.argv[1]) 
