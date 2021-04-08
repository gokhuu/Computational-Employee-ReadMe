#python3
import pandas as pd 

df = pd.read_csv('../15qdup_inverse_rank_sum.csv')

sub_df = pd.read_csv('target_files/110-1.csv')

print(sub_df.head())