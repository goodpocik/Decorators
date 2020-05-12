from decors import speedtest
@speedtest(iterations = 10)
def search(url):
    import requests
    s = requests.get(url)
    return s
webpage = search('https://google.com/')
print(webpage)

