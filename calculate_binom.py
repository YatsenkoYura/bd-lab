import sqlite3
import statistics
import math
import matplotlib.pyplot as plt

connection = sqlite3.connect("movies.db")
db_cursor = connection.cursor()
db_cursor.execute("SELECT CAST(vote_count AS REAL), CAST(vote_average AS REAL) FROM movies WHERE vote_count IS NOT NULL AND vote_average IS NOT NULL")
data = db_cursor.fetchall()
connection.close()

vote_counts_list = [row[0] for row in data]
vote_averages_list = [row[1] for row in data]

avg_vote_count = statistics.mean(vote_counts_list)
avg_vote_average = statistics.mean(vote_averages_list)

num_trials = round(avg_vote_count)
success_probability = avg_vote_average / 10

expected_value = num_trials * success_probability
variance = num_trials * success_probability * (1 - success_probability)
std_deviation = math.sqrt(variance)

lower_k = max(0, int(expected_value - 3 * std_deviation))
upper_k = min(num_trials, int(expected_value + 3 * std_deviation))
k_values = list(range(lower_k, upper_k + 1))
binom_pmf = [math.exp(math.lgamma(num_trials+1)-math.lgamma(k+1)-math.lgamma(num_trials-k+1)+k*math.log(success_probability)+(num_trials-k)*math.log(1-success_probability)) for k in k_values]

print("Параметры биноминального распределения:")
print("num_trials =", num_trials)
print("success_probability =", success_probability)
print("expected_value =", expected_value)
print("std_deviation =", std_deviation)
print("Диапазон k:", k_values)
print("Вероятностная функция:")
for k, prob in zip(k_values, binom_pmf):
    print("k =", k, "P =", prob)

plt.figure(figsize=(10,6))
plt.bar(k_values, binom_pmf, color='blue')
plt.title("Биноминальное распределение")
plt.xlabel("k")
plt.ylabel("P(X=k)")
plt.savefig("binom_distribution.png")
plt.close() 