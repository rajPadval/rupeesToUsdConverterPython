import requests
# url = "http://api.quotable.io/random"
url = "https://api.exchangerate-api.com/v4/latest/usd"
res = requests.get(url)
data = res.json()
msg = data["rates"]["USD"]
print(data,msg)
# print("Motivational quote for the day is : \n",data["content"],"\n Author is :",data["authorSlug"],"\n Posted at :",data["dateAdded"])