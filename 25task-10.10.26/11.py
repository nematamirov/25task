monthly_usage = float(input())
if monthly_usage >= 0 and monthly_usage <= 100:
    applied_rate = 0.08
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
elif monthly_usage > 100 and monthly_usage <= 300:
    applied_rate = 0.12
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
elif monthly_usage > 300: 
    applied_rate = 0.15
    print(monthly_usage)
    print(applied_rate)
    print(monthly_usage*applied_rate)
else:
    print("Invalid")