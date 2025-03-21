import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"

try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

#ex3
paraCount = len(soup.find_all(['p']))
headCount = len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6' ]))
linkCount = len(soup.find_all(['a']))

print("The number of paragraphs", paraCount)
print("The number of headings", headCount)
print("The number of links", linkCount)

#ex4
keyword = input("Please enter a keyword: ").strip()
count = 0
textinWeb = soup.get_text()
words = textinWeb.lower().split()
for word in words:
    strippedWord = "".join(char for char in word if char.isalnum())
    if strippedWord == keyword.lower():
        count+= 1

print("The keyword appears in the webpage", count)

#ex5
stack = {}
for word in words:
    strippedWord = "".join(char for char in word if char.isalnum())
    if strippedWord in stack:
        stack[strippedWord] += 1
    else:
        stack[strippedWord] = 1

wordDiction = sorted(stack.items(), key=lambda x: x[1], reverse=True)
top = wordDiction[:5]

print("The most frequently occuring words are: ")
for word, count in top:
    print(f"{word}: {count}")

#ex6
benchmarkWord = 5
maxCount = 0
paragraphs = soup.find_all(['p'])

for paragraph in paragraphs:
    wordsInPara = paragraph.get_text().split()
    countWord = len(wordsInPara)

    if countWord >= benchmarkWord and countWord > maxCount:
        maxCount = countWord
        maxpara = paragraph.get_text()

print("The number of words in the longest paragraph is", maxCount)
print("The longest paragraph is:\n", maxpara)

#ex7
labels = ['Headings', 'Links', 'Paragraphs']
values = [headCount, linkCount, paraCount]
plt.bar(labels, values)
plt.title('34')
plt.ylabel('Count')
plt.show()
