import Algorithmia

input = "https://news.ycombinator.com/rss"
client = Algorithmia.client('YOUR_API_KEY')
algo = client.algo('tags/ScrapeRSS/0.1.6')
algo.set_options(timeout=300) # optional
print(algo.pipe(input).result)