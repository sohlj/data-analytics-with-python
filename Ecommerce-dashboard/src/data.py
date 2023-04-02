import datetime


def filter_dataframe(df, start_date, end_date, payment_type, login_type, device_type):
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

    dff = df[
        (df['Order_Date'].dt.date >= start_date) &
        (df['Order_Date'].dt.date <= end_date) &
        (df['Payment_method'].isin(payment_type)) & 
        (df['Customer_Login_type'].isin(login_type)) &
        (df['Device_Type'].isin(device_type))
        ]
    
    return dff




def product_cat(df, product_mainsub):
    
    # Gender Distribution by Category or Product
    # select information to extract
    customer_profile = ['Gender', 'Main-category', 'Sub-category', 'Sales','Profit'] 
    df_customer = df[customer_profile]

    # Data preparation - Main Category
    df_grouped = df_customer.groupby([product_mainsub, 'Gender']).size().to_frame('Count') # grouping data 
    df_grouped.reset_index(inplace=True)
    df_grouped = df_grouped.pivot(index=product_mainsub, columns='Gender', values='Count') # pivot table
    df_grouped.reset_index(inplace =True)
    df_grouped['Total'] = df_grouped['Male'] + df_grouped['Female'] # add 'Total' column
    df_grouped['Percent_Male']=round(df_grouped['Male']/df_grouped['Total']*100)
    df_grouped['Percent_Female']=round(df_grouped['Female']/df_grouped['Total']*100)


    return df_grouped