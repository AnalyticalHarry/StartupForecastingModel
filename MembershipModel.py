#importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#class Membership Model
class MembershipModel:
    def __init__(self, initial_members: int, growth_rates: list, membership_fee: float):
        self.initial_members = initial_members
        self.growth_rates = growth_rates
        self.num_years = len(growth_rates)
        self.membership_fee = membership_fee
    #method for simulation
    def simulate(self):
        members = [self.initial_members]
        membership_revenue = [self.initial_members * self.membership_fee]
        for year in range(1, self.num_years):
            growth_rate = self.growth_rates[year - 1]
            new_members = members[-1] * (1 + growth_rate / 100)
            membership_revenue.append(new_members * self.membership_fee)
            members.append(new_members)

        return members, membership_revenue
    #method simulation plot
    def plot_simulation(self):
        members, membership_revenue = self.simulate()
        years = list(range(1, self.num_years + 1))

        fig, ax1 = plt.subplots(figsize=(15, 6))

        #Membership Revenue on the left y-axis
        ax1.plot(years, membership_revenue, label="Membership Revenue", color="blue")
        ax1.set_xlabel('Years', fontsize=14)
        ax1.set_ylabel('Membership Revenue', fontsize=14, color="blue")
        ax1.tick_params(axis='y', labelcolor="blue")
        ax1.grid(linestyle='--', color='gray', alpha=0.5)

        ax2 = ax1.twinx()

        #Membership Count on the right y-axis
        ax2.plot(years, members, label="Membership Count", color="green")
        ax2.set_ylabel('Membership Count', fontsize=14, color="green")
        ax2.tick_params(axis='y', labelcolor="green")

        plt.title('Membership Model', fontsize=16)
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        lines = lines1 + lines2
        labels = labels1 + labels2
        plt.legend(lines, labels)
        plt.show()

    def to_dataframe(self):
        members, membership_revenue = self.simulate()
        years = list(range(1, self.num_years + 1))
        data = {'Year': years, 'Membership Count': members, 'Membership Revenue': membership_revenue}
        df = pd.DataFrame(data)
        return df

#parameters
initial_members = 100
#growth rate each years
growth_rates = [1, 3, 5, 10]  
membership_fee = 299 

#MembershipModel instance
membership_model = MembershipModel(initial_members, growth_rates, membership_fee)
membership_model.plot_simulation()
membership_df = membership_model.to_dataframe()
print(membership_df)
