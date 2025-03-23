import sqlite3
import statistics

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()
cursor.execute("SELECT CAST(popularity AS REAL), CAST(vote_count AS REAL), CAST(vote_average AS REAL) FROM movies")
rows = cursor.fetchall()
conn.close()

popularity = [row[0] for row in rows if row[0] is not None]
vote_count = [row[1] for row in rows if row[1] is not None]
vote_average = [row[2] for row in rows if row[2] is not None]

def get_stats(data):
    return min(data), max(data), statistics.mean(data), statistics.median(data), statistics.stdev(data)

stats_popularity = get_stats(popularity)
stats_vote_count = get_stats(vote_count)
stats_vote_average = get_stats(vote_average)

print("Popularity: min = {}, max = {}, mean = {:.2f}, median = {:.2f}, std = {:.2f}".format(*stats_popularity))
print("Vote Count: min = {}, max = {}, mean = {:.2f}, median = {:.2f}, std = {:.2f}".format(*stats_vote_count))
print("Vote Average: min = {}, max = {}, mean = {:.2f}, median = {:.2f}, std = {:.2f}".format(*stats_vote_average)) 