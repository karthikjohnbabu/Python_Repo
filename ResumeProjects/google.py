try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "python"

for j in search(query, tld="co.in", num=20, stop=10, pause=2):
	print(j)
