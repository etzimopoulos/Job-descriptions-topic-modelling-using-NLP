import re
import pandas as pd
import spacy


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


# Function to display basic entity information
# Input:
#      * NLP document
# Output:
#      * No output
#      * Shows on screen basic entity information
def show_entities(document):
    if document.ents:
        for ent in document.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')

        

# Author: Olivier Grisel <olivier.grisel@ensta.org>
#         Lars Buitinck
#         Chyi-Kwei Yau <chyikwei.yau@gmail.com>
# License: BSD 3 clause
# 
# Function to print out the "n" top words in a topic
# Input:
#        * NLP model
#        * Feature names
#        * Number of top words in a topic
# Output:
#        * Prints on screen top n words per topic
def print_top_words(model, feature_names, n_top_words):
    for topic_idx, topic in enumerate(model.components_):
        message = "Topic #%d: " % topic_idx
        message += " ".join([feature_names[i]
                             for i in topic.argsort()[:-n_top_words - 1:-1]])
        print(message)
    print()
        

       

