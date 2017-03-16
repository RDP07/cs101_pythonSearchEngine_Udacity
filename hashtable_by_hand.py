##This is a hash table coded manually without the help of Python Dictionary

def make_hashtable(nbuckets):
	table = []
	for unused in range(0, nbuckets):
		table.append([])
	return table

def hash_string(keyword, buckets):
	out = 0 
	for c in keyword:
		out = (out + ord(c))
	return out % buckets

def hashtable_get_bucket(htable, keyword):
	return htable[hash_string(keyword, len(htable))]

def hashtable_add(htable, key, value):
	hashtable_get_bucket(htable, key).append([key, value])

##Data to for testing below

table = make_hashtable(5)

hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)

print table