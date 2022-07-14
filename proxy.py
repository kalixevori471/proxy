import httpx


with open("proxy.txt", 'w') as p:
	p.write(httpx.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes").text)