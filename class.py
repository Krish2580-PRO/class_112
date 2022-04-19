import pandas as pd
import plotly.express as pe
import plotly.graph_objects as go
import statistics as st
import csv
import numpy as nu
import plotly.figure_factory as ff


data = pd.read_csv("class.csv")

savingData = data["quant_saved"].tolist()
remAny = data["rem_any"].tolist()

total = len(savingData)

# ------------------------------ finding total no of people who were reminded and not reminded ----------------------------------------
peopleWhoReminded = 0

for i in remAny:
    if i == 1:
        peopleWhoReminded += 1

# print(peopleWhoReminded)

peopleWhoNotReminded = total - peopleWhoReminded

# print (peopleWhoNotReminded)

# -------------------------------------------- plotting the graph for rem and not rem --------------------------------------------------

fig = go.Figure(go.Bar(x =[ "peopleWhoReminded" , "peopleWhoNotReminded"] , y = [peopleWhoReminded , peopleWhoNotReminded] ))
# fig.show()

# --------------------------------------- mean/med/mode/stdev of all the data for everyone(savingsdata) ------------------------------------------------------
mean = st.mean(savingData)
median = st.median(savingData)
mode = st.mode(savingData)
stdev = st.stdev(savingData)

print("-------------------------------------------------------------------------------")

print("Mean of saving for everyone : " , mean)
print("Mode of saving for everyone : " , mode)
print("Median of saving for everyone : " , median)
print("Stdev of saving for everyone : " , stdev)


# --------------------------------------- mean/med/mode/stdev of people who were reminded ------------------------------------------------------

with open("class.csv") as f:
    r = csv.reader(f)
    savingsD = list(r)

savingsD.pop(0)

remindedSavings = []
notRemindedSavings = []

for i in savingsD:
    if int(i[3]) == 1:
        remindedSavings.append(float(i[0]))
    else :
        notRemindedSavings.append(float(i[0]))


mean = st.mean(remindedSavings)
median = st.median(remindedSavings)
mode = st.mode(remindedSavings)
stdev = st.stdev(remindedSavings)

print("-------------------------------------------------------------------------------")
print("Mean of saving for those who were reminded : " , mean)
print("Mode of saving for those who were reminded : " , mode)
print("Median of saving for those who were reminded : " , median)
print("Stdev of saving for those who were reminded : " , stdev)


# --------------------------------------- mean/med/mode/stdev of people who were not reminded ------------------------------------------------------

mean = st.mean(notRemindedSavings)
median = st.median(notRemindedSavings)
mode = st.mode(notRemindedSavings)
stdev = st.stdev(notRemindedSavings)

print("-------------------------------------------------------------------------------")
print("Mean of saving for those who were not reminded : " , mean)
print("Mode of saving for those who were not reminded : " , mode)
print("Median of saving for those who were not reminded : " , median)
print("Stdev of saving for those who were not reminded : " , stdev)



# ----------------------------------- finding correlation coeff in between age and savings -------------------------------------------

age = []
savings = []

savings = data["quant_saved"].tolist()
age = data["age"].tolist()

corcoef = nu.corrcoef(savings, age )
print("Correlation coeff in between age and savings : " , corcoef[0,1])



fig = ff.create_distplot([savingData], ["savings"])
fig.show()

