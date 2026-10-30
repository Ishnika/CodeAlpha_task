#before vs during lockdown
before = df[df['Date'] < '2020-03-25'][rate].mean()
after = df[df['Date'] >= '2020-03-25'][rate].mean()

print("Before lockdown:", round(before, 2))
print("After lockdown:", round(after, 2))
