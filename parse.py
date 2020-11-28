from bs4 import BeautifulSoup
import requests
import csv

url = "https://www.chess.com/members/search?country=116&coaches=&streamers=&titledMembers=&sortBy=last_login_date"

def parsePage(url):
	result = requests.get(url)
	resultList = []
	result = requests.get(url)
	soup = BeautifulSoup(result.content, 'html.parser')
	userList = soup.select('.members-list-username')

	for userName in userList:
		resultRow = []
		resultRow.append(userName.get('title'))
		# print(userName.get('title'))
		resultList.append(resultRow)
	return resultList

def writeToFile(dataList):
	with open('users.csv', 'a', encoding='utf8') as f:
		for row in dataList:
			writer = csv.writer(f)
			writer.writerow(row)

rowList = parsePage(url)
writeToFile(rowList)