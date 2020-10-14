"""
Represents the film objects in the list.
"""

class Film(object):
    def __init__(self, f_name, f_year, f_rating, f_genres,
                    f_runtime, f_storyline, f_type, f_img_source, f_link):
        self.name = f_name
        self.year = f_year
        self.rating = f_rating
        self.genres = f_genres
        self.runtime = f_runtime
        self.storyline = f_storyline
        self.type = f_type
        self.image_source = f_img_source
        self.imdb_link = f_link


    def print_film(self):
        print("Film, ", self.name)
        print("Year ", self.year)
        print('Rating', self.rating)
        print("Genres", self.genres)
        print('Runtime', self.runtime)
        print('Storyline', self.storyline)
        print('Type,', self.type)

    def get_genres_string(self):
        sep = ', '
        return sep.join(self.genres)

    def get_image_html(self):
        return '<a href="https://www.imdb.com%s"> <img alt="%s" height="209" width="140" src="%s" > </a>' % (self.imdb_link, self.name, self.image_source)

    def get_title(self):
        return '<a href="https://www.imdb.com%s"><h4> %s </h4></a>' % (self.imdb_link, self.name)


    def get_rating(self):
        return '<span class="rating">  %s </span>' % str((self.rating / 10))
