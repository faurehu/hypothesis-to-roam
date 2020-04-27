import re
import requests
import sys

# Caveat: this removes all of the breaklines and content in square brackets within a highlight

try:
    url = sys.argv[1]
    token = sys.argv[2]
except IndexError as e:
    print("Missing arguments")
    sys.exit()

try:
    useBlockquote = sys.argv[3]
except IndexError as e:
    useBlockquote = False

def getStart(row):
    selectors = row['target'][0]['selector']
    selector = next(x for x in selectors if x["type"] == "TextPositionSelector")
    return selector["start"]

def getQuote(row):
    selectors = row['target'][0]['selector']
    return next(x for x in selectors if x["type"] == "TextQuoteSelector")["exact"]

url = "https://hypothes.is/api/search?limit=200&sort=created&order=asc&url={0}".format(url)

payload = {}
headers = {
  'Accept': 'application/vnd.hypothesis.v1+json',
  'Authorization': 'Bearer {0}'.format(token)
}

response = requests.request("GET", url, headers=headers, data = payload)

if response.status_code != 200:
    print("Request error")
    sys.exit()

data = response.json()['rows']

if len(data) == 0:
    print("Empty data")
    sys.exit()

data = sorted(data, key = getStart)

blockquote = ":hiccup [:blockquote [:a {{:href \"{0}\"}} [:p \"{1}\"]]]\n"
markdown = "[{1}]({0})\n"

file = open("output.txt", "w")

for row in data:
    link = row['links']['incontext']
    quote = re.sub(r"\[[^\]]*\]", "", re.sub(r"\n"," ", getQuote(row)))
    roam = markdown.format(link, quote)

    if useBlockquote:
        roam = blockquote.format(link,quote)

    if row['text'] != "":
        text = re.sub(r"\[[^\]]*\]", "", re.sub(r"\n"," ", row["text"]))
        roam += "\t{0}\n".format(row["text"])

    file.write(roam)

file.close()
print("Done")

