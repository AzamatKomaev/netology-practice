import csv
import json


i = 0
categories_with_users = []


def find_category_by_user_id(categories, user_id) -> list:
    for category in categories:
        if category["user_id"] == user_id:
            return category


with open('purchase_log.txt', 'r') as f:
    for line in f.readlines():
        d = json.loads(line)
        categories_with_users.append(d)


output_csv = open('funnel.csv', 'a')


with open('visit_log.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        # if i == 3:
        #     break
        # i += 1

        user_id, source = row[0].split(',')
        found_category_json = find_category_by_user_id(categories_with_users, user_id)

        if found_category_json is None: 
            continue

        found_category = found_category_json["category"]

        to_csv = f'{user_id},{source},{found_category}'
        with open('funnel.csv', 'a') as output_csv:
            output_csv.write(to_csv+'\n')


output_csv.close()