import os
import pandas as pd
import plotly.express as px
import json
import streamlit as st
from streamlit_option_menu import option_menu

path = "D:/pulse-master/data/aggregated/transaction/country/india/state"
state_list = os.listdir(path)

#function to correct the state name
def alt(data):
  data['State'] = data['State'].str.replace("-", " ")
  data['State'] = data['State'].str.title()
  data['State'] = data['State'].str.replace("Andaman & Nicobar Islands", "Andaman & Nicobar")
  data['State'] = data['State'].str.replace("Dadra & Nagar Haveli & Daman & Diu", "Dadra and Nagar Haveli and Daman and Diu")
  return data


#aggregated transation

path1 = "D:/pulse-master/data/aggregated/transaction/country/india/state/"
Agg_state_list = os.listdir(path1)

clm = {'State':[], 'Year':[], 'Quater':[], 'Transacion_type':[], 'Transacion_count':[], 'Transacion_amount':[]}

for i in Agg_state_list:
    p_i = path1+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D1 = json.load(Data)
            for z in D1['data']['transactionData']:
              Name = z['name']
              count = z['paymentInstruments'][0]['count']
              amount = z['paymentInstruments'][0]['amount']
              clm['Transacion_type'].append(Name)
              clm['Transacion_count'].append(count)
              clm['Transacion_amount'].append(amount)
              clm['State'].append(i)
              clm['Year'].append(j)
              clm['Quater'].append(int(k.strip('.json')))

Agg_Trans = pd.DataFrame(clm)
Agg_Trans = alt(Agg_Trans)

#aggregated user

path2 = "D:/pulse-master/data/aggregated/user/country/india/state/"
Agg_state_list = os.listdir(path2)

clm2={'State':[], 'Year':[],'Quater':[],'Brands':[], 'Transacion_count':[], 'Percentage':[]}
for i in Agg_state_list:
    p_i=path2+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D2=json.load(Data)
            try:
              for y in D2['data']['usersByDevice']:
                brand=y['brand']
                count=y['count']
                percentage=y['percentage']
                clm2['Brands'].append(brand)
                clm2['Transacion_count'].append(count)
                clm2['Percentage'].append(percentage)
                clm2['State'].append(i)
                clm2['Year'].append(j)
                clm2['Quater'].append(int(k.strip('.json')))
            except:
              pass
Agg_user=pd.DataFrame(clm2)
Agg_user=alt(Agg_user)



#aggregated insurance

path3="D:/pulse-master/data/aggregated/insurance/country/india/state/"
Agg_state_list=os.listdir(path3)

clm3={'State':[], 'Year':[],'Quater':[],'Insurance_count':[], 'Total_amount':[],}
for i in Agg_state_list:
    p_i=path3+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D3=json.load(Data)
            try:
              for y in D3['data']['transactionData'][0]['paymentInstruments']:
                count=y['count']
                amount=y['amount']
                clm3['Insurance_count'].append(count)
                clm3['Total_amount'].append(amount)
                clm3['State'].append(i)
                clm3['Year'].append(j)
                clm3['Quater'].append(int(k.strip('.json')))
            except:
              pass
Agg_insu=pd.DataFrame(clm3)
Agg_insu=alt(Agg_insu)


#map transaction

path4="D:/pulse-master/data/map/transaction/hover/country/india/state/"
Agg_state_list=os.listdir(path4)

clm4={'State':[], 'Year':[],'Quater':[],'District':[], 'Transacion_count':[], 'Transacion_amount':[]}

for i in Agg_state_list:
    p_i=path4+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D4=json.load(Data)
            for z in D4['data']['hoverDataList']:
              Name=z['name']
              count=z['metric'][0]['count']
              amount=z['metric'][0]['amount']
              clm4['District'].append(Name)
              clm4['Transacion_count'].append(count)
              clm4['Transacion_amount'].append(amount)
              clm4['State'].append(i)
              clm4['Year'].append(j)
              clm4['Quater'].append(int(k.strip('.json')))
map_Trans=pd.DataFrame(clm4)
map_Trans=alt(map_Trans)

#map user

path5="D:/pulse-master/data/map/user/hover/country/india/state/"
Agg_state_list=os.listdir(path5)

clm5={'State':[], 'Year':[],'Quater':[],'District':[], 'Registered_Users':[], 'app_Opens':[]}
for i in Agg_state_list:
    p_i=path5+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D5=json.load(Data)
            for y in D5['data']['hoverData'].items():
              district=y[0]
              reg_user=y[1]['registeredUsers']
              appopen=y[1]['appOpens']
              clm5['District'].append(district)
              clm5['Registered_Users'].append(reg_user)
              clm5['app_Opens'].append(appopen)
              clm5['State'].append(i)
              clm5['Year'].append(j)
              clm5['Quater'].append(int(k.strip('.json')))
map_user=pd.DataFrame(clm5)
map_user=alt(map_user)


#map insurance

path6="D:/pulse-master/data/map/insurance/hover/country/india/state/"
Agg_state_list=os.listdir(path6)

clm6={'State':[], 'Year':[],'Quater':[],'District':[], 'Insurance_count':[], 'Total_amount':[]}
for i in Agg_state_list:
    p_i=path6+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D6=json.load(Data)
            for y in D6['data']['hoverDataList']:
              district=y['name']
              count=y['metric'][0]['count']
              amount=y['metric'][0]['amount']
              clm6['District'].append(district)
              clm6['Insurance_count'].append(count)
              clm6['Total_amount'].append(amount)
              clm6['State'].append(i)
              clm6['Year'].append(j)
              clm6['Quater'].append(int(k.strip('.json')))
map_insu=pd.DataFrame(clm6)
map_insu=alt(map_insu)


#top transation

path7="D:/pulse-master/data/top/transaction/country/india/state/"
Agg_state_list=os.listdir(path7)

clm71={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Transcation_count':[], 'Total_amount':[]}
for i in Agg_state_list:
    p_i=path7+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D7=json.load(Data)
            for z in D7['data']['pincodes']:
              pincode=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              clm71['Pincode'].append(pincode)
              clm71['Transcation_count'].append(count)
              clm71['Total_amount'].append(amount)
              clm71['State'].append(i)
              clm71['Year'].append(j)
              clm71['Quater'].append(int(k.strip('.json')))



top_trans_pin=pd.DataFrame(clm71)
top_trans_pin=alt(top_trans_pin)


#top user

path8="D:/pulse-master/data/top/user/country/india/state/"
Agg_state_list=os.listdir(path8)

clm81={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'registeredUsers':[]}
for i in Agg_state_list:
    p_i=path8+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D8=json.load(Data)
            for y in D8['data']['pincodes']:
              pincode=y['name']
              registeredUsers=y['registeredUsers']
              clm81['Pincode'].append(pincode)
              clm81['registeredUsers'].append(registeredUsers)
              clm81['State'].append(i)
              clm81['Year'].append(j)
              clm81['Quater'].append(int(k.strip('.json')))


top_user_pin=pd.DataFrame(clm81)
top_user_pin=alt(top_user_pin)


#top insurance

path9="D:/pulse-master/data/top/insurance/country/india/state/"
Agg_state_list=os.listdir(path9)

clm91={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Insurance_count':[], 'Total_amount':[]}
for i in Agg_state_list:
    p_i=path9+i+"/"
    Agg_yr=os.listdir(p_i)
    for j in Agg_yr:
        p_j=p_i+j+"/"
        Agg_yr_list=os.listdir(p_j)
        for k in Agg_yr_list:
            p_k=p_j+k
            Data=open(p_k,'r')
            D9=json.load(Data)
            for z in D9['data']['pincodes']:
              pincode=z['entityName']
              count=z['metric']['count']
              amount=z['metric']['amount']
              clm91['Pincode'].append(pincode)
              clm91['Insurance_count'].append(count)
              clm91['Total_amount'].append(amount)
              clm91['State'].append(i)
              clm91['Year'].append(j)
              clm91['Quater'].append(int(k.strip('.json')))

top_ins_pin=pd.DataFrame(clm91)
top_ins_pin=alt(top_ins_pin)

#Code sql part

import sqlite3
conn=sqlite3.connect('raw.db')
cursor=conn.cursor()

Agg_Trans.to_sql("AT", conn, if_exists="append", index=False)
Agg_user.to_sql("AU", conn, if_exists="append", index=False)
Agg_insu.to_sql("AI", conn, if_exists="append", index=False)
map_Trans.to_sql("MT", conn, if_exists="append", index=False)
map_user.to_sql("MU", conn, if_exists="append", index=False)
map_insu.to_sql("MI", conn, if_exists="append", index=False)
top_trans_pin.to_sql("TTP", conn, if_exists="append", index=False)
top_user_pin.to_sql("TUP", conn, if_exists="append", index=False)
top_ins_pin.to_sql("TIP", conn, if_exists="append", index=False)

analysis1=pd.read_sql_query('''SELECT State,sum(Transacion_amount) as 'Transacion_amount' from AT GROUP BY State ORDER BY Transacion_amount desc''',conn)
analysis2=pd.read_sql_query('''SELECT Year,sum(Transacion_amount) as 'Transacion_amount' from AT group by Year''',conn)
analysis3=pd.read_sql_query('''SELECT Transacion_type,sum(Transacion_amount) as 'Transacion_amount' from AT group by Transacion_type''',conn)
analysis4=pd.read_sql_query('''SELECT Transacion_type,sum(Transacion_count) as 'Transacion_count' from AT group by Transacion_type''',conn)
analysis5=pd.read_sql_query('''SELECT Brands,sum(Transacion_count) as Transacion_count from AU GROUP BY Brands ORDER BY Transacion_count desc''',conn)
analysis6=pd.read_sql_query('''SELECT State, sum(Insurance_count) as Insurance_count,sum(Total_amount) as Total_amount from AI GROUP BY State ORDER BY Insurance_count desc''',conn)
analysis7=pd.read_sql_query('''SELECT District,sum(Transacion_amount) as 'Transacion_amount' from MT GROUP BY District ORDER BY Transacion_amount desc''',conn)
analysis8=pd.read_sql_query('''SELECT State,sum(Registered_Users) as Registered_Users from MU GROUP BY State ORDER BY Registered_Users desc''',conn)
analysis9=pd.read_sql_query('''SELECT District,sum(Registered_Users) as Registered_Users from MU GROUP BY District ORDER BY Registered_Users desc''',conn)
analysis10=pd.read_sql_query('''SELECT District,sum(Insurance_count) as Insurance_count from MI GROUP BY District ORDER BY Insurance_count desc''',conn)
analysis11=pd.read_sql_query('''SELECT District,sum(Total_amount) as Total_amount from MI GROUP BY District ORDER BY Total_amount desc''',conn)
analysis12=pd.read_sql_query('''SELECT CAST(Pincode AS TEXT) as Pincode,sum(Total_amount) as Total_amount from TTP GROUP BY Pincode ORDER BY Total_amount desc''',conn)
analysis13=pd.read_sql_query('''SELECT Pincode,sum(registeredUsers) as registeredUsers from TUP GROUP BY Pincode ORDER BY registeredUsers desc''',conn)
analysis14=pd.read_sql_query('''SELECT Pincode,sum(Total_amount) as Total_amount from TIP GROUP BY Pincode ORDER BY Total_amount desc''',conn)

YEAR18=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2018' ''',conn)
YEAR19=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2019' ''',conn)
YEAR20=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2020' ''',conn)
YEAR21=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2021' ''',conn)
YEAR22=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2022' ''',conn)
YEAR23=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2023' ''',conn)
YEAR24=pd.read_sql_query('''SELECT State,Year,Quater,Transacion_amount from AT WHERE Year=='2024' ''',conn)

YEAR18.to_sql("YEAR18", conn, if_exists="append", index=False)
YEAR19.to_sql("YEAR19", conn, if_exists="append", index=False)
YEAR20.to_sql("YEAR20", conn, if_exists="append", index=False)
YEAR21.to_sql("YEAR21", conn, if_exists="append", index=False)
YEAR22.to_sql("YEAR22", conn, if_exists="append", index=False)
YEAR23.to_sql("YEAR23", conn, if_exists="append", index=False)
YEAR24.to_sql("YEAR24", conn, if_exists="append", index=False)

#year 18
Quater181=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR18 WHERE Quater== '1'GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater182=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR18 WHERE Quater== '2'GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater183=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR18 WHERE Quater== '3'GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater184=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR18 WHERE Quater== '4'GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)

#year 19
Quater191=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR19 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater192=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR19 WHERE Quater== '2' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater193=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR19 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater194=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR19 WHERE Quater== '4' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
#year 20
Quater201=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR20 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater202=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR20 WHERE Quater== '2' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater203=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR20 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater204=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR20 WHERE Quater== '4' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
#year 21
Quater211=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR21 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater212=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR21 WHERE Quater== '2' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater213=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR21 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater214=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR21 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)

#year 22
Quater221=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR22 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater222=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR22 WHERE Quater== '2' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater223=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR22 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater224=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR22 WHERE Quater== '4' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)

#year 23
Quater231=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR23 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater232=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR23 WHERE Quater== '2' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater233=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR23 WHERE Quater== '3' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)
Quater234=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR23 WHERE Quater== '4' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)

#year 24
Quater241=pd.read_sql_query('''SELECT State,Quater,sum(Transacion_amount) as 'Transacion amount' from YEAR24 WHERE Quater== '1' GROUP BY State ORDER BY sum(Transacion_amount) desc''',conn)

#Code for visualization

fig1 = px.bar(analysis1.head(20), x='State', y='Transacion_amount', color='State', title='Aggregated Transaction')
fig3 = px.funnel_area(analysis3, names='Transacion_type', values='Transacion_amount', title='TRANSACTION AMOUNT')
fig4 = px.funnel_area(analysis4, names='Transacion_type', values='Transacion_count', title='TRANSACTION COUNT')
fig5 = px.pie(analysis5.head(10), names='Brands', values='Transacion_count', title='Brands vs Transaction_count')
fig8 = px.bar(analysis7.head(10), x='District', y='Transacion_amount', color='District', title='District vs Transaction amount')
fig10 = px.bar(analysis9.head(10), x='District', y='Registered_Users', color='District', title='District vs Registered Users')
fig11 = px.bar(analysis10.head(10), x='District', y='Insurance_count', color='District', title='District vs Insurance count')
fig12 = px.bar(analysis11.head(10), x='District', y='Total_amount', color='District', title='District vs Total Total amount')
fig13 = px.bar(analysis12.head(10), x='Pincode', y='Total_amount', color='Pincode', title='Pincode vs Total amount', width=700)
fig14 = px.bar(analysis13.head(10), x='Pincode', y='registeredUsers', color='Pincode', title='Pincode vs Registered Users',width=700)
fig15 = px.bar(analysis14.head(10), x='Pincode', y='Total_amount', color='Pincode', title='Pincode vs Total Insurance amount',width=700)
fig6 = px.bar(analysis6.head(15), x='State', y='Insurance_count', color='State', title='State vs Insurance_count')
fig7 = px.bar(analysis6.head(15), x='State', y='Total_amount', color='State', title='State vs Insurance_amount')

quaterfig181 = px.bar(Quater181.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig182 = px.bar(Quater182.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig183 = px.bar(Quater183.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig184 = px.bar(Quater184.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig191 = px.bar(Quater191.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig192 = px.bar(Quater192.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig193 = px.bar(Quater193.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig194 = px.bar(Quater194.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig201 = px.bar(Quater201.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig202 = px.bar(Quater202.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig203 = px.bar(Quater203.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig204 = px.bar(Quater204.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig211 = px.bar(Quater211.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig212 = px.bar(Quater212.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig213 = px.bar(Quater213.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig214 = px.bar(Quater214.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig221 = px.bar(Quater221.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig222 = px.bar(Quater222.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig223 = px.bar(Quater223.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig224 = px.bar(Quater224.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig231 = px.bar(Quater231.head(20), x='State', y='Transacion amount', title='Quater 1')
quaterfig232 = px.bar(Quater232.head(20), x='State', y='Transacion amount', title='Quater 2')
quaterfig233 = px.bar(Quater233.head(20), x='State', y='Transacion amount', title='Quater 3')
quaterfig234 = px.bar(Quater234.head(20), x='State', y='Transacion amount', title='Quater 4')

quaterfig241 = px.bar(Quater241.head(20), x='State', y='Transacion amount', title='Quater 1')

#Code for Map visualization
fig = px.choropleth(
    analysis1,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Transacion_amount',
    title='Indian States vs Transacion amount',
    color_continuous_scale='PRGn'
)
fig.update_geos(fitbounds="locations", visible=False)
fig9 = px.choropleth(
    analysis8,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='State',
    color='Registered_Users',
    title='Indian States vs Registered Users',
    color_continuous_scale='PRGn'
)
fig9.update_geos(fitbounds="locations", visible=False)



#Code for streamlit

st.title(":violet[PHONE PE]")
with st.sidebar:
    selected = option_menu("FILTER", ['STATE','YEAR','TRANSACTION TYPE','BRANDS','DISTRICT','PINCODE'],
        icons=['map','calendar3', 'graph-up','phone','bar-chart','geo-alt'], menu_icon="funnel", default_index=0)
if selected == "STATE":
  with st.expander("STATE VS TRANSACTION AMOUNT"):
      st.plotly_chart(fig1)
      st.plotly_chart(fig)

  with st.expander("STATE VS INSURANCE"):
      st.plotly_chart(fig6)
      st.plotly_chart(fig7)
      st.caption("Here we can see the differences between the Insurance count and Insurance amount,"
                 "even though some states have higher Insurance count they have lower Insurance amount"
                 "and some states have lower Insurance count they have higher Insurance."
                 "States like Tamil Nadu and Kerala are examples of it.")


  with st.expander("STATE VS REGISTERED USER"):
      st.plotly_chart(fig9)

if selected == "YEAR":
    with st.expander("YEAR 2018"):
        st.plotly_chart(quaterfig181)
        st.plotly_chart(quaterfig182)
        st.plotly_chart(quaterfig183)
        st.plotly_chart(quaterfig184)
    with st.expander("YEAR 2019"):
        st.plotly_chart(quaterfig191)
        st.plotly_chart(quaterfig192)
        st.plotly_chart(quaterfig193)
        st.plotly_chart(quaterfig194)
    with st.expander("YEAR 2020"):
        st.plotly_chart(quaterfig201)
        st.plotly_chart(quaterfig202)
        st.plotly_chart(quaterfig203)
        st.plotly_chart(quaterfig204)
    with st.expander("YEAR 2021"):
        st.plotly_chart(quaterfig211)
        st.plotly_chart(quaterfig212)
        st.plotly_chart(quaterfig213)
        st.plotly_chart(quaterfig214)
    with st.expander("YEAR 2022"):
        st.plotly_chart(quaterfig221)
        st.plotly_chart(quaterfig222)
        st.plotly_chart(quaterfig223)
        st.plotly_chart(quaterfig224)
    with st.expander("YEAR 2023"):
        st.plotly_chart(quaterfig231)
        st.plotly_chart(quaterfig232)
        st.plotly_chart(quaterfig233)
        st.plotly_chart(quaterfig234)
    with st.expander("YEAR 2024"):
        st.plotly_chart(quaterfig241)



if selected == "TRANSACTION TYPE":
  with st.expander("TRANSACTION TYPE VS TRANSACTION AMOUNT and TRANSACTION COUNT"):
      st.plotly_chart(fig4)
      st.plotly_chart(fig3)
      st.write("Here we can clearly see huge difference between Merchant payments count vs the Merchant payments amount,"
               "the count is very low but the amount is very high.")

if selected == "BRANDS":
  with st.expander("BRANDS VS TRANSACTION COUNT"):
      st.plotly_chart(fig5)


if selected == "DISTRICT":
  with st.expander("DISTRICT VS TRANSACTION AMOUNT"):
      st.plotly_chart(fig8)

  with st.expander("DISTRICT VS REGISTERED USERS"):
      st.plotly_chart(fig10)

  with st.expander("DISTRICT VS INSURANCE COUNT and INSURANCE AMOUNT"):
      st.plotly_chart(fig11)
      st.plotly_chart(fig12)
      st.write("Here we can see several mismatches in the position of the districts because of the differences in the Insurance amount and Insurance count.")

if selected == "PINCODE":
    with st.expander("PINCODE VS TRANSACTION AMOUNT"):
          st.plotly_chart(fig13)

    with st.expander("PINCODE VS REGISTERED USERS"):
        st.plotly_chart(fig14)

    with st.expander("PINCODE VS INSURANCE AMOUNT"):
        st.plotly_chart(fig15)




























