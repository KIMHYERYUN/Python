#if we live until 90years old, how many days, weeks, months we left
#There are 365days in a year, 52 weeks in a year and 12months in a year.

age = input("What is your current age?")

left_days = (90 - int(age)) * 365
left_weeks = (90 - int(age)) * 52
left_months = (90 - int(age)) * 12

print(f"You have {left_days} days, {left_weeks} weeks, {left_months} months left.")


#다른방법
years_remaining = 90-int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, {months_remaining} months left."
print(message)
