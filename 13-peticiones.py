import request

url = "https://jocarsa.com/"

try :
    response = request.get(url, timeout = 10)
    response.raise_for_status() #Raise an error for bad status codes (4xx, 5xx)
    html = respnse.text # or response.content for bytes
    print(html)
except request.exceptions.RequestException as e:
    print("Error")