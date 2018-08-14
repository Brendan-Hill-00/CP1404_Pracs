print('Electricity bill estimator')
price_per_kwh = int(input('Enter cents per kWh: '))
price_per_kwh = price_per_kwh/100
daily_kwh_usage = float(input('Enter daily use in kWh: '))
billing_days = int(input('Enter number of billing days: '))
estimated_bill = price_per_kwh * daily_kwh_usage * billing_days
print('Estimated bill: ', estimated_bill)
