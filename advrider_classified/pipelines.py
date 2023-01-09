# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class MongodbPipline(object):
#     collection_name = 'bikes'

#     def open(self, spider):
#         self.client = pymongo.MongClient('uri')
#         self.db = self.client['IMDB']

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item


# class MongodbPipline(object):
#     collection_name = 'bikes'

#     def open(self, spider):
#         self.connection =

#     def close_spider(self, spider):
#         self.client.close()

#     def process_item(self, item, spider):
#         self.db[self.collection_name].insert(item)
#         return item

from bikes.models import Category, Manufacturer, Bike, Image
from .utils import convert_date_format


class AdvriderPipeline:

    # started when spider begins execution process
    # classmethod job is to grab settings from settigns.py

    def __init__(self, *args, **kwargs):
        self.manufacturers = {
            "BMW": Manufacturer.objects.get_or_create(mfg="BMW"),
            "KTM": Manufacturer.objects.get_or_create(mfg="KTM"),
            "HONDA": Manufacturer.objects.get_or_create(mfg="HONDA"),
            "YAMAHA": Manufacturer.objects.get_or_create(mfg="YAMAHA"),
            "SUZUKI": Manufacturer.objects.get_or_create(mfg="SUZUKI"),
            "MOTO": Manufacturer.objects.get_or_create(mfg="MOTO GUZZI"),
            "TRIUMPH": Manufacturer.objects.get_or_create(mfg="TRIUMPH"),
            "DUCATI": Manufacturer.objects.get_or_create(mfg="DUCATI"),
            "KAWASAKI": Manufacturer.objects.get_or_create(mfg="KAWASKAI"),
            "HARLEY": Manufacturer.objects.get_or_create(mfg="HARLEY DAVIDSON"),
            "APRILIA": Manufacturer.objects.get_or_create(mfg="APRILIA"),
            "HUSQVARNA": Manufacturer.objects.get_or_create(mfg="HUSQVARNA"),
            "BETA": Manufacturer.objects.get_or_create(mfg="BETA"),
            "URAL": Manufacturer.objects.get_or_create(mfg="URAL"),
            "INDIAN": Manufacturer.objects.get_or_create(mfg="INDIAN"),
            "ROYAL": Manufacturer.objects.get_or_create(mfg="ROYAL ENFIELD"),
        }

    def process_item(self, item, spider):
        category = item.get("category")
        cat, _ = Category.objects.get_or_create(cat=category)
        tmp_images = item.get("images")
        images = []

        title = item.get("title").strip()

        # Parse title for mfg, price, year
        title_arr = title.split(" ")
        mfg_match = None

        mfg_arr = [mfg for mfg in self.manufacturers.keys()]
        for word in title_arr:
            if word.upper() in mfg_arr:
                mfg_match = self.manufacturers[word.upper()][0]

        # Remove bogus image urls, those that begin with 'data/'
        for image in tmp_images:
            if image[0:4] != "data":
                images.append(image)

        tmp_first_post = item.get("first_post")
        first_post = []
        for line in tmp_first_post:

            # if not mfg_match:
            #     for word in line.split(' '):
            #         if word.upper() in mfg_arr:
            #             mfg_match = self.manufacturers[word.uppers()]

            if (
                (line[0:4] != "<img")
                and (line[0:3] != "<a ")
                and (line != '"')
                and (line != '"')
            ):
                first_post.append(line.strip())

            # If there is link in this post section, it is a link to an image we need the image'
            elif (line[0:3] == "<a ") and ("<img" in line):
                tmp_arr = line.split('"')
                images.append(tmp_arr[1])

        bike = Bike(
            title=title,
            link=item.get("url").strip(),
            first_post=(" ").join(first_post),
            cat=cat,
            mfg=mfg_match,
            post_date=convert_date_format(item.get("post_date")),
        )

        bike.save()

        for image in images:
            curr = Image(image=image, bike=bike)
            curr.save()

        return item
