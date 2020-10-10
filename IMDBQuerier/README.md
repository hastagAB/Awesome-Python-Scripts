# IMDBQuerier

This project is written to parsing films from IMDB user lists based on some attributes. It uses Selenium and BeautifulSoup to obtain and parse the film data.

Until now, the project can parse films based on their:

* Runtime
* Score
* Year
* Genre
* Type (TV show or film)

Currently, one can make the exact queries on the refine section at the bottom of each user list. However, it is hard to apply your selections to all lists.

Checkout [original repo](https://github.com/Bekci/IMDBQuerier) for the latest version.
## Requirements

Selenium and BeautifulSoup modules are necessary for the project. Other than that, you will need a WebDriver. The project is using ChromeDriver but you can change it to the other supported browsers easily.

If you have changed the driver, make sure to change the below code accordingly.

```
# main.py line 16
driver = webdriver.Chrome()
```

[Here is a link for the Firefox driver.](https://github.com/mozilla/geckodriver/releases)

## Usage

First of all, change the values in the `parse_options` dictionary in the [parser_config.py](parser_config.py).

Then, change the value of `list_url` variable in the [main.py](main.py)  code to the list wanted to be parsed.

 Run the code, the output html will apear in list_htmls folder.

## Common Driver Error

The used version of the browser driver can be out-dated. Always use the latest version in case of an error. 

[Firefox Driver](https://github.com/mozilla/geckodriver/releases)

[Chrome Driver](https://chromedriver.chromium.org/)