import json


with open('reviews.json', 'r') as json_file:
    json_data = json.load(json_file)

reviews = [item["Review:"].strip() for item in json_data]
output_file_name = 'converted.txt'

with open(output_file_name, 'w') as txt_file:
    for review in reviews:
        txt_file.write(review + '\n')

print('done')