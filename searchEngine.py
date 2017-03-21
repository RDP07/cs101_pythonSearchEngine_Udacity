
def get_page(url):
	if url in cache:
		return cache[url]
	else:
		return None



def get_next_target(page):
	start_link = page.find('<a href =')
	if start_link < 0:
		return None, 0
	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote

def get_all_links(page):
	links = []
	while True:
		url, endpos = get_next_target(page)
		if url:
			links.append(url)
			page = page[endpos:]
		else:
			break
	return links

def crawl_web(seed):
	tocrawl = [seed]
	crawled = []
	graph = {}
	index = {}
	while tocrawl: 
		page = tocrawl.pop()
		if page not in crawled:
			content = get_page(page)
			add_page_to_index(index,page,content)
			outlinks = get_all_links(content)
			graph[page] = outlinks
			set().union(tocrawl, outlinks)
			crawled.append(page)
	return index

index = {}

def add_to_index(index,keyword,url):
	if keyword in index:
		index[keyword].append(url)
	else:
		index[keyword] = [url]

def lookup(index,keyword):
	if keyword in index:
		return index[keyword]
	return None

def add_page_to_index(index,url,content):
	words = content.split()
	for word in words:
		add_to_index(index, word, url)

print crawl_web(get_page('http://xkcd.com/353'))











