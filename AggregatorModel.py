#Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#class for exponential Customer growth Forecast 
class ExponentialCustomerGrowthForecast:
    
    def __init__(self, fee: float, frequency: int, num_customers: int, 
                 year: int, growth: float, sample_rate: float):
        self.fee = fee
        self.frequency = frequency
        self.num_customers = num_customers
        self.year = year
        self.growth = growth
        self.sample_rate = sample_rate

    def generate_sample(self):
        #creating sample from population
        #num of customers are population or total market
        #sample_rate is the hypothesis or market captured rate
        sample = int(self.num_customers * self.sample_rate)
        return sample

    def calculate_forecast(self):
        months = 12 * self.year
        sales = []
        for month in range(1, months + 1):
            sample = self.generate_sample()
            #first month growth rate will zero growth rate
            total_customers = sample * (1 + self.growth) ** (month - 1)
            num_orders = self.frequency  
            #montly sales will sum of sample per month, fee and number of orders (frequency)
            monthly_sales = total_customers * num_orders * self.fee
            sales.append(monthly_sales)
        return sales

    def plot_forecast(self):
        sales = self.calculate_forecast()
        months = list(range(1, 12 * self.year + 1))
        plt.style.use('dark_background')
        plt.figure(figsize=(15,6))
        plt.plot(months, sales, color="white", linestyle="--")
        plt.bar(months, sales, color="red")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months',fontsize=20)
        plt.ylabel('Sales',fontsize=20)
        plt.title('Customer Sales Growth Forecast',fontsize=20)
        plt.show()

    def to_dataframe(self):
        sales = self.calculate_forecast()
        months = list(range(1, 12 * self.year + 1))
        data = {'Month': months, 'Sales': sales}
        df = pd.DataFrame(data)
        return df
    
fee = 2.99 #2.99 pounds service charge
frequency = 4 #Number of orders per customer
num_customers = 5000 #Population size
year = 5 #Number of years
growth = 0.05 #5% growth rate
sample_rate = 0.01 #5 percent of Market

forecast = ExponentialCustomerGrowthForecast(fee, frequency, num_customers, year, growth, sample_rate)
forecast_df = forecast.to_dataframe()
forecast_plot = forecast.plot_forecast()
