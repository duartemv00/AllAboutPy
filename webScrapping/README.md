
# Webscrapping (using scrapy)
### What is Webscrapping?
Programmatically send requests to a website, receive the data specified in the code and parse the data to extract specific information.

## Basic information about scrapy
### Install scrapy package

```pip install scrapy```

### Initialice scrapy project

```scrapy startproject projectName```


## Spider creation
To generate a new spider you need to input the next command while inside the spider folder.

```scrapy genspider spiderName web.direction.com```

### Before creating the script, try to extract the data using the shell
Open the shell to try the commands before creating the script.
You can use the default scrapy shell, but it is recommended to use the ipython shell instead.

#### How to configure ipython
First install it

```pip install ipython```

Then inside the settings.py file include this code:

```shell = ipython```

And using the command line you can start the shell (whether you are using ipython or not)

```scrapy shell```

#### Using the shell
Fetch the information from the web

```fetch('https://books.toscrape.com')```

Using the information from the page (html, css code) store the content
```books = response.css('article.product_pod')```

```book.css('h3 a::text').get()```

```book.css('.product_price .price_color::text').get()```

```book.css('h3 a').attrib['href']```

Then we can introduce this instructions in the actual script of the spider.

### Activate a spider 
```scrapy crawl bookspider```

### How to save spider results into a file (.json, .csv)

If you want to append the data if the current file already exists, use:

```scrapy crawl bookspider -o fileName.csv```

If you want to override the current existing file, use:

```scrapy crawl bookspider -O fileName.csv```

If you want the result to automatically be stored in a file without using the '-o filename.csv', you have to setup the settings.py

```FEEDS = { 'bookdata.csv' : {'format' : 'json'} }```

And you can emulte the functionality of '-O filename.csv' using

```FEEDS = { 'bookdata.csv' : {'format' : 'json', 'overwritte' : true } }```

or directly inside the spider class using

```custom_settings { FEEDS = { 'bookdata.csv' : {'format' : 'json'} } }```


### awhghabsjhgbashdbg
Move to another page
> response.css("li.next a ::attr(href)").get()





### xpath()
response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()



### search information in a table
table_rows = response.css("table tr")
table_rows[0].css('td::text').get()


## Scrapy Items
Useful to create actual data categories (columns)
>class BookItem(scrapy.item):
>    
>    url = scrapy.Field()


def serialize_price(value):
    return f'$ {str(value)}'


class BookItem(scrapy.item):
    """
    Book item class to store book information
    """
    url = scrapy.Field()

    

## Scrapy Pipelines
Clean data


## Bibliography
- https://www.youtube.com/watch?v=mBoX_JCKZTE&t=934s
- https://books.toscrape.com
- https://www.youtube.com/watch?v=vxk6YPRVg_o 