#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#class franchise Model
class FranchiseModel:
    def __init__(self, initial_franchisees: int, growth_rate: float, num_years: int, franchise_fee: float):
        self.initial_franchisees = initial_franchisees
        self.growth_rate = growth_rate
        self.num_years = num_years
        self.franchise_fee = franchise_fee
        
    def simulate(self):
        franchisees = [self.initial_franchisees]
        franchise_fees = [0.0]
        
        for year in range(1, self.num_years + 1):
            #new franchisees based on growth rate
            new_franchisees = franchisees[-1] * (1 + self.growth_rate)
            
            #franchise fee revenue
            revenue = new_franchisees * self.franchise_fee
            
            #append data to lists
            franchisees.append(new_franchisees)
            franchise_fees.append(revenue)
        
        return franchisees, franchise_fees
    
    def plot_simulation(self):
        franchisees, franchise_fees = self.simulate()
        years = list(range(self.num_years + 1))
        
        plt.figure(figsize=(15, 6))
        plt.plot(years, franchisees, label="Franchisees", color="blue")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Years', fontsize=14)
        plt.ylabel('Number of Franchisees', fontsize=14)
        plt.title('Franchise Model Franchisee Growth', fontsize=16)
        plt.legend()
        plt.show()
        
        plt.figure(figsize=(15, 6))
        plt.plot(years, franchise_fees, label="Franchise Fees Revenue", color="green")
        plt.grid(linestyle='--', color='gray', alpha=0.5)
        plt.xlabel('Years', fontsize=14)
        plt.ylabel('Franchise Fees Revenue', fontsize=14)
        plt.title('Franchise Model Franchise Fees Revenue', fontsize=16)
        plt.legend()
        plt.show()

    def to_dataframe(self):
        franchisees, franchise_fees = self.simulate()
        years = list(range(self.num_years + 1))
        data = {'Year': years, 'Franchisees': franchisees, 'Franchise Fees Revenue': franchise_fees}
        df = pd.DataFrame(data)
        return df

#parameters
initial_franchisees = 10
#annual growth rate
growth_rate = 0.1 
num_years = 10
#franchise fee per new franchisee
franchise_fee = 50000  

#FranchiseModel instance
franchise_model = FranchiseModel(initial_franchisees, growth_rate, num_years, franchise_fee)
franchise_model.plot_simulation()
franchise_df = franchise_model.to_dataframe()
print(franchise_df)
