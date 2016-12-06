from bs4 import BeautifulSoup as bs
from bs4 import Comment
from collections import OrderedDict
import requests
import slugify
import json
import csv
import os

url = 'http://www.pro-football-reference.com/teams/nwe/2016.htm'

r = requests.get(url)
text = r.text.encode(encoding="utf-8")
structure = bs(text, 'html.parser')
rootname = slugify.slugify(structure.find('meta', { 'name' : 'Description' })['content'])
allTables = []
uncommentedTables = structure.findAll('table', { 'class' : 'stats_table' })

for table in uncommentedTables:
	allTables.append(table)

comments = structure.findAll(text=lambda text:isinstance(text, Comment))

for comment in comments:
	fixed = bs(comment.extract().encode(encoding="utf-8"), 'html.parser')
	commentedTables = fixed.findAll('table', { 'class' : 'stats_table' })
	for table in commentedTables:
		allTables.append(table)

if not os.path.exists(rootname+'-tables'):
	os.makedirs(rootname+'-tables')

tableHasBeenParsed = []

for table in allTables:

	if table['id'] not in tableHasBeenParsed:
		print table['id']
		tableHasBeenParsed.append(table['id'])
		if table.find('tbody'):
			header = []
			tablename = rootname+'-tables'+'/'+table['id']
			rows = table.findAll('tr')
			newRows = []
			for row in rows:
				obj = OrderedDict()
				cells = list(row.children)
				for cell in cells:
					if cell.name == 'td' and str(type(cell)) == "<class 'bs4.element.Tag'>" and cell.has_attr('data-stat'):
						key = cell['data-stat']
						if key not in header:
							header.append(key)

						obj[key] = str(''.join(cell.stripped_strings))
				
				if bool(obj) == True:
					newRows.append(obj)

		with open(tablename+'.csv', 'w') as file:
			writer = csv.DictWriter(file, fieldnames=header,extrasaction='ignore')
			writer.writeheader()
			writer.writerows(newRows)


