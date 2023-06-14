#Import necessary libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder
#Function for getting the processer category
def fetch_processor(text):
    if text == 'Intel Core i7' or text == 'Intel Core i5' or text == 'Intel Core i3':
        return text
    else:
        if text.split()[0] == 'Intel':
            return 'Other Intel Processor'
        else:
            return 'AMD Processor'
            
#Function for getting OS type           
def cat_os(inp):
    if inp == 'Windows 10' or inp == 'Windows 7' or inp == 'Windows 10 S':
        return 'Windows'
    elif inp == 'macOS' or inp == 'Mac OS X':
        return 'Mac'
    else:
        return 'Others/No OS/Linux'
        
        
            
def pre_processing(df):
    #Converting categorical data to numeric data
    df.drop(columns=['laptop_ID','Product'],inplace=True)
    #Remove GB and kg in 'Ram' and 'Weight' columns
    df['Ram']=df['Ram'].str.replace('GB','')
    df['Weight']=df['Weight'].str.replace('kg','')
    #convert the 'Ram' and 'Weight' columns object to Int and float
    df['Ram']=df['Ram'].astype('int32')
    df['Weight']=df['Weight'].astype('float32')
    #create one column for touch feature in laptops
    df['TouchScreen']=df['ScreenResolution'].apply(lambda x:1 if 'Touchscreen' in x else 0)
    #Create one more for IPS functio.
    df['IPS']=df['ScreenResolution'].apply(lambda x:1 if'IPS' in x else 0)
    #now create 2 more column for resolution from ScreenResolution column
    new=df['ScreenResolution'].str.split('x',n=1,expand=True)
    #2nd column is good but 1st have some problem okay 
    df['X_res']=new[0]
    df['Y_res']=new[1]
    #now remove the strings in X_res column with the help of regular expression
    df['X_res'] = df['X_res'].str.replace(',','').str.findall(r'(\d+\.?\d+)').apply(lambda x:x[0])
    #convert both column(X_res and y_res) in integer
    df['X_res']=df['X_res'].astype('int')
    df['Y_res']=df['Y_res'].astype('int')
    #create last feature PPI (Pixel per inch) with the help of X_res,Y_res and Inches columns
    df['PPI'] = (((df['X_res']**2) + (df['Y_res']**2))**0.5/df['Inches']).astype('float')
    #now drop Inches,X_res,Y_res and ScreenResolution
    df.drop(columns=['ScreenResolution','Inches','X_res','Y_res'],inplace=True)
    #create more columns aCC. TO THE CATEGORY 
    df['Cpu_Name']=df['Cpu'].apply(lambda x:" ".join(x.split()[0:3]))
    df['Cpu_brand']=df['Cpu_Name'].apply(fetch_processor)
    #now drop Cpu and Cpu_name Column
    df.drop(columns=['Cpu','Cpu_Name'],inplace=True)
    #transform the Memory column acc. to category

    df['Memory'] = df['Memory'].astype(str).replace('\.0', '', regex=True)
    df["Memory"] = df["Memory"].str.replace('GB', '')
    df["Memory"] = df["Memory"].str.replace('TB', '000')
    new = df["Memory"].str.split("+", n = 1, expand = True)

    df["first"]= new[0]
    df["first"]=df["first"].str.strip()

    df["second"]= new[1]

    df["Layer1HDD"] = df["first"].apply(lambda x: 1 if "HDD" in x else 0)
    df["Layer1SSD"] = df["first"].apply(lambda x: 1 if "SSD" in x else 0)
    df["Layer1Hybrid"] = df["first"].apply(lambda x: 1 if "Hybrid" in x else 0)
    df["Layer1Flash_Storage"] = df["first"].apply(lambda x: 1 if "Flash Storage" in x else 0)

    df['first'] = df['first'].str.replace(r'\D', '')

    df["second"].fillna("0", inplace = True)

    df["Layer2HDD"] = df["second"].apply(lambda x: 1 if "HDD" in x else 0)
    df["Layer2SSD"] = df["second"].apply(lambda x: 1 if "SSD" in x else 0)
    df["Layer2Hybrid"] = df["second"].apply(lambda x: 1 if "Hybrid" in x else 0)
    df["Layer2Flash_Storage"] = df["second"].apply(lambda x: 1 if "Flash Storage" in x else 0)

    df['second'] = df['second'].str.replace(r'\D', '')

    df["first"] = df["first"].astype(int)
    df["second"] = df["second"].astype(int)

    df["HDD"]=(df["first"]*df["Layer1HDD"]+df["second"]*df["Layer2HDD"])
    df["SSD"]=(df["first"]*df["Layer1SSD"]+df["second"]*df["Layer2SSD"])
    df["Hybrid"]=(df["first"]*df["Layer1Hybrid"]+df["second"]*df["Layer2Hybrid"])
    df["Flash_Storage"]=(df["first"]*df["Layer1Flash_Storage"]+df["second"]*df["Layer2Flash_Storage"])

    df.drop(columns=['first', 'second', 'Layer1HDD', 'Layer1SSD', 'Layer1Hybrid',
           'Layer1Flash_Storage', 'Layer2HDD', 'Layer2SSD', 'Layer2Hybrid',
           'Layer2Flash_Storage'],inplace=True)
    #drop Memory 
    df.drop(columns=['Memory'],inplace=True)
    #remove hybrid and Flash_Storage acc. to Correlation
    df.drop(columns=['Hybrid','Flash_Storage'],inplace=True)
    #for brand name only
    df['Gpu brand'] = df['Gpu'].apply(lambda x:x.split()[0])
    #remove ARM bcz only 1 laptop 
    df = df[df['Gpu brand'] != 'ARM']
    df.drop(columns=['Gpu'],inplace=True)
    df['os'] = df['OpSys'].apply(cat_os)
    df.drop(columns=['OpSys'],inplace=True)
    return df
    
    
