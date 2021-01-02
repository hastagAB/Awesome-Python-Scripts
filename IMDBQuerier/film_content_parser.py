"""
Parse strings obtained from the html to get the film metadata.
Fix metadata and create an film object to be use it later.
"""

from ClassFilm import Film
import re

"""
Eliminate parenthesis from the text.
'(2019)' -> '2019'
"""
def parse_film_year(year_text):
    found_numbers = re.findall("[0-9]", year_text)
    return ''.join(found_numbers[0:4])


"""
Obtain decimal value of the score from its text.
'7'  -> 70
'7,9'-> 79
"""
def parse_imdb_score(score_text):
    units_digit = 0
    if ',' in score_text:
        tens_digit, units_digit = score_text.split(',')
    else:
        tens_digit = score_text.split(',')[0]
    return int(tens_digit) * 10 + int(units_digit)


"""
Parse runtime in minutes from runtime text.
"134 min" -> 134
"""
def parse_runtime(runtime_text):
    return runtime_text.split(' ')[0]


"""
From the string of genres, obtain the genres list.
Remove extra spaces and new line characters.
Return genres in a list.
"""
def obtain_all_genres(genres_text):
    obtained_genres = []
    for genre in genres_text.split(','):
        obtained_genres.append(genre.replace('\n', '').replace(' ', ''))
    return obtained_genres


"""
Storyline obtained as text from the html yet some characters must be deleted
from it.
"""
def obtain_story_line(story_text):
    return story_text.replace('\n', '')

"""
Determine the film type from the year text.
A TV-series will include '-' but a film will not include.
"""
def determine_film_type(year_text):
    if '–' in year_text:
        return 'tv-series'
    return 'film'

"""
Sometimes images cannot be loaded and its src will be a placeholder.
For such cases, loadlate tag will be the real source.
"""
def obtain_image_source(img_html):
    if 'loadlate' in img_html.attrs:
        return img_html['loadlate']
    else:
        return img_html['src']


"""
Take a html block representing the film item
Apply parsing and return film object
"""
def obtain_film_object(content, image_raw):
    # Runtime and score of a film might not given in the list item.
    runtime = "unknown"
    point = "unknown"

    raw_name_with_link = content.find('a')
    raw_name = raw_name_with_link.text
    film_imdb_link = raw_name_with_link['href']
    raw_year = content.find("span", class_="lister-item-year text-muted unbold").text
    raw_runtime = content.find("span", class_="runtime")

    if raw_runtime is not None:
        raw_runtime = raw_runtime.text
        runtime = int(parse_runtime(raw_runtime))

    raw_genre = content.find("span", class_="genre").text
    raw_point = content.find("span", class_="ipl-rating-star__rating")

    if raw_point is not None:
        raw_point = raw_point.text
        point = int(parse_imdb_score(raw_point))

    raw_storyline = content.find("p", class_="").text

    year = parse_film_year(raw_year)
    genre_list = obtain_all_genres(raw_genre)
    storyline = obtain_story_line(raw_storyline)
    f_type = determine_film_type(year)
    image_source = obtain_image_source(image_raw)

    return Film(raw_name, year, point, genre_list, runtime, storyline, f_type, image_source, film_imdb_link)
