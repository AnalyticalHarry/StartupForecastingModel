#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#class ads model
class AdvertisingModel:
    def __init__(self, initial_users: int, growth_rate: float, num_months: int, ad_impression_rate: float, ad_revenue_per_impression: float):
        self.initial_users = initial_users
        self.growth_rate = growth_rate
        self.num_months = num_months
        self.ad_impression_rate = ad_impression_rate
        self.ad_revenue_per_impression = ad_revenue_per_impression
    #method simulate to predict outcome
    def simulate(self):
        users = [self.initial_users]
        ad_impressions = [0]
        ad_revenue = [0.0]
        
        for month in range(1, self.num_months + 1):
            #new users based on growth rate
            new_users = users[-1] * (1 + self.growth_rate)
            
            #ad impressions based on user count and impression rate
            impressions = new_users * self.ad_impression_rate
            
            #ad revenue based on impressions and revenue per impression
            revenue = impressions * self.ad_revenue_per_impression
            
            #data to lists
            users.append(new_users)
            ad_impressions.append(impressions)
            ad_revenue.append(revenue)
        
        return users, ad_impressions, ad_revenue

     #method to plot return
    def plot_simulation(self):
        users, ad_impressions, ad_revenue = self.simulate()
        months = list(range(self.num_months + 1))
        
        plt.figure(figsize=(15, 6))
        plt.plot(months, users, label="Users", color="blue")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Number of Users', fontsize=14)
        plt.title('Advertising Model User Growth', fontsize=16)
        plt.legend()
        plt.show()
        
        plt.figure(figsize=(15, 6))
        plt.plot(months, ad_impressions, label="Ad Impressions", color="green")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Number of Ad Impressions', fontsize=14)
        plt.title('Advertising Model Ad Impressions', fontsize=16)
        plt.legend()
        plt.show()
        
        plt.figure(figsize=(15, 6))
        plt.plot(months, ad_revenue, label="Ad Revenue", color="orange")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Months', fontsize=14)
        plt.ylabel('Ad Revenue', fontsize=14)
        plt.title('Advertising Model Ad Revenue', fontsize=16)
        plt.legend()
        plt.show()
    #method which return dataframe
    def to_dataframe(self):
        users, ad_impressions, ad_revenue = self.simulate()
        months = list(range(self.num_months + 1))
        data = {'Month': months, 'Users': users, 'Ad Impressions': ad_impressions, 'Ad Revenue': ad_revenue}
        df = pd.DataFrame(data)
        return df

#parameters
initial_users = 1000
growth_rate = 0.05
num_months = 12
#average ad impressions per user per month
ad_impression_rate = 0.2  
#revenue per ad impression (e.g., $0.01 per impression)
ad_revenue_per_impression = 0.01  
#AdvertisingModel instance
advertising_model = AdvertisingModel(initial_users, growth_rate, num_months, ad_impression_rate, ad_revenue_per_impression)
advertising_model.plot_simulation()
advertising_df = advertising_model.to_dataframe()
print(advertising_df)
