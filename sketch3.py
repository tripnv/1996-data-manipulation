import pandas as pd

def iter_data(df,list1,list2,length, name):
    
    
    sum_list = []

    for i in range(length):
        if i != 0:
            sum_list.append(str(list1.iloc[i]) )
            sum_list.append(list2.iloc[i])

    return (sum_list)

def generate_column_names(length, name):
    
    
    sum_list = []

    for i in range(length):
        if i != 0:
            sum_list.append("P" + "_" + str(i))
            sum_list.append(name + "_" + str(i))

    return (sum_list)

def none_addition(length):
    z = ['-'] * 2 * (21-length)
    return z

def alt_transp (df, index_list_x):
    
    list_of_lists = []
    
    column_names = []

    column_names.extend(["JUD","CE", "TIP_PV", "CODU", "DEN_CIRC","TA", "TAPU", "TVVE","TVN","VVE","N_CONS_L","MCF1","MCF2"])

    column_names.extend(generate_column_names(21, "VVE"))

    column_names.extend(generate_column_names(21, "MCF1"))

    column_names.extend(generate_column_names(21, "MCF2"))

    column_names.extend(generate_column_names(21,  "X_CONS_L"))
    
    list_of_lists.append(column_names)
    
    for i_main in range(len(index_list_x)-1):
        
        #print(i_main)
    
        alt_df = df.loc[index_list_x[i_main]:index_list_x[i_main +1]].loc[1:index_list_x[i_main+1]-1]
        
        alt_df = alt_df.sort_values(by=['VVE'],ascending = False)
        
        row_list = []

        #partide
        list_DEN = alt_df["DEN1_FP"]
        #VVE
        list_VVE = alt_df["VVE"]
        #MCF_1
        list_MCF1 = alt_df["MCF1"]
        #MCF_2
        list_MCF2 = alt_df["MCF2"]
        #X_CONS_L
        list_X_CONS = alt_df["X_CONS_L"]

        first_part = df.loc[index_list_x[i_main]][["JUD","CE", "TIP_PV", "CODU", "DEN_CIRC","TA", "TAPU", "TVVE","TVN","VVE","N_CONS_L","MCF1","MCF2"]].to_list()
        row_list.extend(first_part)

        if len(alt_df) < 20:
            
            
            row_list.extend(iter_data(alt_df, list_DEN,list_VVE, len(alt_df), "VVE"))
            row_list.extend(none_addition(len(alt_df)))

            row_list.extend(iter_data(alt_df, list_DEN,list_MCF1, len(alt_df), "MCF1"))
            row_list.extend(none_addition(len(alt_df)))

            row_list.extend(iter_data(alt_df, list_DEN,list_MCF2, len(alt_df), "MCF2"))
            row_list.extend(none_addition(len(alt_df)))

            row_list.extend(iter_data(alt_df, list_DEN,list_X_CONS, len(alt_df), "X_CONS_L"))
            row_list.extend(none_addition(len(alt_df)))

            list_of_lists.append(row_list)

        else:

            row_list.extend(iter_data(alt_df, list_DEN,list_VVE, 20, "VVE"))
            row_list.append("REST_VVE")
            row_list.append(str(alt_df["VVE"].iloc[20:len(alt_df)].sum()))

            row_list.extend(iter_data(alt_df, list_DEN,list_MCF1, 20,"MCF1"))
            row_list.append("REST_MCF1")
            row_list.append(str(alt_df["MCF1"].iloc[20:len(alt_df)].sum()))

            row_list.extend(iter_data(alt_df, list_DEN,list_MCF2, 20,"MCF2"))
            row_list.append("REST_MCF2")
            row_list.append(str(alt_df["MCF2"].iloc[20:len(alt_df)].sum()))

            row_list.extend(iter_data(alt_df, list_DEN,list_X_CONS, 20, "X_CONS_L"))
            row_list.append("REST_X_CONS_L")
            row_list.append(str(alt_df["X_CONS_L"].iloc[20:len(alt_df)].sum()))

            list_of_lists.append(row_list)
    return list_of_lists
        


def find_cities (df):
    index_list =[]
    for i in range(len(df)):
        if (df["CODU"].loc[i]==0):
            index_list.append(i)
    return index_list




f_name="CONS_LOC-1996.dbf.csv"
f_df = pd.read_csv(f_name)
f_df


cities = find_cities(f_df)
cities_10=[]
for i in range(10):
    cities_10.append(cities[i])

#print(cities_10[:-1])
#print(cities_10)

x = alt_transp(f_df, cities)
z = pd.DataFrame(x)
z.to_csv("1996_1.csv")

#print(z)
