#importing libraries
import numpy as np
import pandas as pd
import matplotlib.ticker as ticker
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

        fig, ax1 = plt.subplots(figsize=(15, 6))

        #plot the first set of data on the left y-axis
        ax1.plot(years, franchisees, label="Franchisees", color="blue")
        ax1.set_xlabel('Years', fontsize=14)
        ax1.set_ylabel('Number of Franchisees', fontsize=14)
        ax1.tick_params(axis='y', labelcolor="blue")

        #create a secondary y-axis on the right side
        ax2 = ax1.twinx()

        #plot the second set of data on the right y-axis
        ax2.plot(years, franchise_fees, label="Franchise Fees Revenue", color="green")
        ax2.set_ylabel('Franchise Fees Revenue', fontsize=14, color="green")
        ax2.tick_params(axis='y', labelcolor="green")

        #apply custom formatting function to both y-axes to remove exponential notation
        def format_func(value, tick_number):
            if value >= 1e6:
                return f'{int(value/1e6)}M'
            elif value >= 1e3:
                return f'{int(value/1e3)}K'
            else:
                return int(value)

        ax1.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
        ax2.yaxis.set_major_formatter(ticker.FuncFormatter(format_func))
        ax1.grid(linestyle='--', color='gray', alpha=0.5)
        plt.title('Franchise Model', fontsize=16)
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        lines = lines1 + lines2
        labels = labels1 + labels2
        plt.legend(lines, labels)
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
