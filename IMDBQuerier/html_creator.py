"""
Create a new html file from selected films.
Save the file under lists directory.
"""
import os
HTML_DIRS = 'list_htmls'

def crete_directory():
    if not os.path.exists(HTML_DIRS):
        os.mkdir(HTML_DIRS)

def start_html(list_name):
    return """
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
      <link rel="stylesheet" href="../css/list_style.css">
        <meta charset="utf-8">
        <title>Selected Films</title>
      </head>
      <body>
      <span class="list_title"><h2> %s </h2></span>
        <ul>
    """ % list_name

def close_html():
    return """
        </ul>
      </body>
    </html>
    """

def create_table_from_object(film_object):
    return """
            <br>
            <li>
             <table>
                <tr>
                    <td rowspan="5">%s</td>
                    <td colspan="3"> %s</td>
                </tr>
                <tr>
                <td colspan="3">Year: %s</td>
                </tr>
                <tr>
                    <td> %s mins</td>
                    <td>%s </td>
                    <td>IMDB Rating: %s </td>
                </tr>
                <tr>
                    <td colspan="3">%s</td>
                </tr>
            </table>
            </li>
            <br>
    """ % (film_object.get_image_html(), film_object.get_title(), film_object.year, film_object.runtime,
            film_object.get_genres_string(), film_object.get_rating(), film_object.storyline)

def create_html_file(film_objects_list, list_name):
    film_html_str = ""
    # Generate html list
    for film_object in film_objects_list:
        film_html_str += create_table_from_object(film_object)

    crete_directory()

    html_file = open(os.path.join(HTML_DIRS, list_name + '.html'), "w", encoding='utf-8')
    html_file.write(start_html(list_name) + film_html_str + close_html() )
