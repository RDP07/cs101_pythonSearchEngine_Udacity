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

def entry_in_bucket(bucket, key):
	for entry in bucket:
		if entry[0] == key:
			return entry
	return None

def hashtable_lookup(htable, key):
	entry = entry_in_bucket(hashtable_get_bucket(htable, key), key)
	if entry:
		return entry[1]
	return None

def hashtable_update(htable, key, value):
	bucket = hashtable_get_bucket(htable, key)
	entry = entry_in_bucket(bucket, key)
	if entry:
		entry[1] = value
	else:
		bucket.append([key, value])

##Data to for testing below

table = make_hashtable(5)

hashtable_add(table,'Bill', 17)
hashtable_add(table,'Coach', 4)
hashtable_add(table,'Ellis', 11)
hashtable_add(table,'Francis', 13)
hashtable_add(table,'Louis', 29)
hashtable_add(table,'Nick', 2)

print table

print hashtable_lookup(table, 'Bill')
print hashtable_lookup(table, 'Coach')


hashtable_update(table, 'Rochelle', 94)
hashtable_update(table, 'Zed', 68)
hashtable_update(table, 'Luke', 7)

print table