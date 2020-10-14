"""
Define and check rules for a film object.
"""

# Rules for the film object
parse_options = {
    'type': 'film',
    'runtime_min': 80,
    'runtime_max': 140,
    'inlude_unkown_runtime': False,
    'score_range_min': '6.9',
    'score_range_max': '10.0',
    'include_unknown_score': False,
    'year_range_oldest': 1990,
    'year_range_newest': 2019,
    'wanted_genres': ['drama'],
    'unwanted_genres': ['romance', 'musical','horror', 'documentary'],
    # Whether add or remove a film
    # whose genre neither in wanted_genres nor unwanted_genres list
    'add_not_unwanted_&_not_wanted': True,
    'include_watched': False
}

def check_runtime(film_runtime):
    if film_runtime == 'unknown':
        return parse_options['inlude_unkown_runtime']
    min_runtime = parse_options['runtime_min']
    max_runtime = parse_options['runtime_max']

    return film_runtime >= min_runtime and film_runtime <= max_runtime

def check_genre(film_genre_list):
    for genre in film_genre_list:
        if genre.lower() in parse_options['unwanted_genres']:
            return False
    if parse_options['wanted_genres'] is None or len(parse_options['wanted_genres']) == 0:
        return True
    for genre in film_genre_list:
        if genre.lower() in parse_options['wanted_genres']:
            return True
    return parse_options['add_not_unwanted_&_not_wanted']


def check_score(score_range):
    if score_range == 'unknown':
        return parse_options['include_unknown_score']
    min_score = float(parse_options['score_range_min']) * 10
    max_score = float(parse_options['score_range_max']) * 10
    return score_range >= min_score and score_range <= max_score


def check_year(year_range):
    min_year = parse_options['year_range_oldest']
    max_year = parse_options['year_range_newest']
    return int(year_range) >= min_year and int(year_range) <= max_year


def check_type(film_type):
    if  parse_options['type'] == 'both':
        return True
    elif  parse_options['type'] == film_type:
        return True
    return False

def watched_included():
    return parse_options['include_watched']

def check_film_object(film_object, watched_films=None):
    if not check_runtime(film_object.runtime):
        return False
    if not check_genre(film_object.genres):
        return False
    if not check_score(film_object.rating):
        return False
    if film_object.type == 'film' and not check_year(film_object.year):
        return False
    if not check_type(film_object.type):
        return False
    if watched_films is not None and film_object.name in watched_films:
        return False
    # All of the above rules applied for the object
    return True
