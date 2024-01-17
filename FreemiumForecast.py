#importging libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating class for freemium customer growth forecast
class FreemiumCustomerGrowthForecast:
    def __init__(self, free_users: int, premium_users: int, year: int, growth_rate: float, premium_fee: float):
        self.free_users = free_users
        self.premium_users = premium_users
        self.year = year
        self.growth_rate = growth_rate
        self.premium_fee = premium_fee  # Fee charged to premium users
    #method for forecast
    def calculate_forecast(self):
        months = 12 * self.year
        free_user_growth = []
        premium_user_growth = []
        total_users = []
        #track revenue from premium users
        premium_revenue = []  
        
        for month in range(1, months + 1):
            free_user_growth.append(self.free_users)
            premium_user_growth.append(self.premium_users)
            total_users.append(self.free_users + self.premium_users)
            
            #revenue from premium users
            monthly_premium_revenue = self.premium_users * self.premium_fee
            premium_revenue.append(monthly_premium_revenue)
            
            #applying growth rate to both free and premium users
            self.free_users *= (1 + self.growth_rate)
            self.premium_users *= (1 + self.growth_rate)
        return free_user_growth, premium_user_growth, total_users, premium_revenue
      
    #method to plot forecast
    def plot_forecast(self):
        free_user_growth, premium_user_growth, total_users, premium_revenue = self.calculate_forecast()
        months = list(range(1, 12 * self.year + 1))

        #user growth plot 
        plt.figure(figsize=(15, 6))
        plt.plot(months, free_user_growth, label="Free Users", color="blue")
        plt.plot(months, premium_user_growth, label="Premium Users", color="orange")
        plt.plot(months, total_users, label="Total Users", color="green")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Number of Users', fontsize=14)
        plt.title('Freemium Model User Growth Forecast', fontsize=16)
        plt.legend()
        plt.show()
        
        #premium revenue over time
        plt.figure(figsize=(15, 6))
        plt.plot(months, premium_revenue, label="Premium Revenue", color="purple")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Premium Revenue', fontsize=14)
        plt.title('Premium User Revenue Forecast', fontsize=16)
        plt.ticklabel_format(axis="y", style="plain")  # Format y-axis as plain numbers
        plt.legend()
        plt.show()

    def to_dataframe(self):
        free_user_growth, premium_user_growth, total_users, premium_revenue = self.calculate_forecast()
        months = list(range(1, 12 * self.year + 1))
        data = {'Month': months, 'Free Users': free_user_growth, 'Premium Users': premium_user_growth, 
                'Total Users': total_users, 'Premium Revenue': premium_revenue}
        df = pd.DataFrame(data)
        return df

#parameters
#total free user
free_users = 1000
#premium user
premium_users = 500
#total time perid
year = 5
#each month growth rate
growth_rate = 0.05
#fee charged to premium user
premium_fee = 9.99 

#plotting forecast
forecast = FreemiumCustomerGrowthForecast(free_users, premium_users, year, growth_rate, premium_fee)
forecast_df = forecast.to_dataframe()
forecast_plot = forecast.plot_forecast()
