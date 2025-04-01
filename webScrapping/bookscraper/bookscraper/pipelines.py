# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        # Remove leading and trailing whitespace from all fields except 'description'
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value[0].strip() # if isinstance(value, str) else value

        # Category and Product type should be lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        # Conver price to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            value = value.replace('£', '').replace('€', '').replace('$', '')
            adapter[price_key] = float(value)

        # Availability should be only a number value
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])

        # Convert reviews string to integer
        reviews_string = adapter.get('num_of_reviews')
        adapter['num_of_reviews'] = int(reviews_string)

        # Convert stars string to integer
        stars_string = adapter.get('stars')
        split_stars_array = stars_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        match stars_text_value:
            case 'one':
                adapter['stars'] = 1
            case 'two':
                adapter['stars'] = 2
            case 'three':
                adapter['stars'] = 3
            case 'four':
                adapter['stars'] = 4
            case 'five':
                adapter['stars'] = 5
            case _:
                adapter['stars'] = 0

        return item
