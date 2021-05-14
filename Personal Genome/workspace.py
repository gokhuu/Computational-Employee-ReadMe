def create_pos_set(lst):
	pos_nested_list = [i.POS for i in lst]
	pos_list = [j for i in pos_nested_list for j in i]
	pos_set = set(pos_list)

 	return pos_set

def add_homo_ref(df, pos_set,chrm):
	#create list of current position
	curr_pos = [i for i in df.POS]

	#create list of positions the df does not have
	not_in_lst = [i for i in pos_set if i not in curr_pos]

	#create new dataframe with new positions
	to_append = [[chrm, i, 'Homozygous Reference'] for i in not_in_lst]
	col_names = df.columns
	temp = pd.Dataframe(to_append, columns = col_names)
	
	#append dataframes
	new_df = pd.concat([df, temp])
	return new_df