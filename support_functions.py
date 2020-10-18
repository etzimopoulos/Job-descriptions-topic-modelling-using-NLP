import re
import pandas as pd


# Function to extract "e-mail" from dataframe column
# Input: 
#     * Dataframe "df" 
#     * Column "df_column" to extract e-mail from  
# Output: Enriched dataframe with addional column labelled "Email"
def extract_email_from_column(df, df_column):
    info = []
    for text in df_column:
        #email = re.findall(r'\w+@\w+.\w{3}',text)[:1]
        #email = re.findall(r'\S+@\S+', text)[:1]
        email = re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", text)[:1]
        info.append(email)
        
    # Add extracted list of emails to dataframe as a column
    df['Email'] = pd.DataFrame(info)
    
    return df

# Function to extract "company name" from "E-mail" dataframe column
# Input: 
#     * Dataframe "df" 
#     * Column "df_column" to extract company name from  
# Output: Enriched dataframe with addional column labelled "Company"
def extract_company_from_column(df, df_column):
    comp_name = []
    for email in df_column:
        if email == None:
            name = 'None'
            comp_name.append(name)
        else:
            name = email[ email.find("@")+1 : email.find(".")] 
            comp_name.append(name)
    
    # Add extracted list of Company names as new dataframe Column
    df["Company"] = pd.DataFrame(comp_name)
    
    return df

