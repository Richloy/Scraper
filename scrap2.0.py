import requests, lxml, csv
from bs4 import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
#print (html)


soup = BeautifulSoup(html, "lxml")
#print (soup.prettify())
print('.....')
print('.....')
print('.....')
print('.....')

table = soup.find('tbody', attrs={'class': 'stripe'})
#print (table.prettify())

'''for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print (cell.text)'''

'''for row in table.findAll('tr'):
    for cell in row.findAll('td'):
        print (cell.text.replace('&nbsp;', ''))'''

'''for row in table.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    print (list_of_cells)'''

list_of_rows = []
for row in table.findAll('tr'):
    list_of_cells = []
    list_of_new_cells = []
    for cell in row.findAll('td'):
        text = cell.text.replace('&nbsp;', '')
        list_of_cells.append(text)
    list_of_cells.pop(0)
    print (list_of_cells)
    print ('\n')
    list_of_rows.append(list_of_cells)

print (list_of_rows)

'''outfile = open("./inmates.csv", "w")
writer = csv.writer(outfile)
writer.writerow(["Last", "First", "Middle", "Gender", "Race", "Age", "City", "State"])
writer.writerows(list_of_rows)'''

outfile = open("./inmates.txt", "w")
outfile.write("Last,First,Middle,Gender,Race,Age,City,State\n")
col_text = ''
for row in list_of_rows:
    for col in row:
        #for x in range(0, len(col)):
        col_text = col_text + col + ','
    outfile.write(col_text + "\n")
    col_text = ''
outfile.close()


