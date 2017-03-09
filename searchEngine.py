page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find('<a href=') + 9
end_link = page.find('.com') + 4
url = page[start_link:end_link]

print url

def get_next_target(page):
	start_link = page.find('<a href =')

	if start_link < 0:
		return None, 0

	start_quote = page.find('"', start_link)
	end_quote = page.find('"', start_quote + 1)
	url = page[start_quote + 1:end_quote]
	return url, end_quote