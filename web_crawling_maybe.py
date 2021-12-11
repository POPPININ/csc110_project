"""
Copyright and Usage Information
===============================


"""
from newsplease import NewsPlease
import csv

# article = NewsPlease.from_url(
#     'https://www.nytimes.com/2017/02/23/us/politics/cpac-stephen-bannon-reince-priebus.html?hp')
# article2 = NewsPlease.from_url('https://www.thestar.com/opinion/editorials/2021/11/03/doug-ford-is-shirking-his-responsibility-to-patients-by-not-making-health-workers-get-their-shots.html')
# # print(article2.maintext)
# article3 = NewsPlease.from_url('https://www.theglobeandmail.com/opinion/editorials/article-yes-to-vaccine-mandates-yes-to-vaccine-passports/')
# print('article 3 \n' + article3.maintext)

articles = NewsPlease.from_file('links.txt')

import csv

# open the file in the write mode
with open('dataset.csv', 'w', encoding='UTF8', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)
    header = ['title', 'url', 'source_domain', 'description', 'authors', 'date_publish',
              'maintext']
    writer.writerow(header)
    keys = articles.keys()

    for key in keys:
        row = [articles[key].title, articles[key].url, articles[key].source_domain,
               articles[key].description, articles[key].authors, articles[key].date_publish,
               articles[key].maintext]
        writer.writerow(row)

    # write a row to the csv file
    # writer.writerow(row)
