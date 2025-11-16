# A weather station records the temperature of n days. The station wants to count how many days 
# the temperature was above the average temperature. 
n = int(input())
temps = list(map(int, input().split()))
avg_temp = sum(temps) / n
count_above_avg = 0
for temp in temps:
    if temp > avg_temp:
        count_above_avg += 1
print(count_above_avg)
