import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  

#Correlation
#Null Hypothesis Testing    

df = None
with open("creatine_clinical_trials.csv",'r') as csv_file:  
    #Read in CSV file into Dataframe
    df = pd.read_csv(csv_file)  
    #print(df.head())   
    #We are only checking for users that take 5g of creatine daily
    df = df[df['Creatine_Intake_g_per_day']==5]
    #Inserting column  
    df['Muscle_Mass_Change_in_8_weeks'] = df['Muscle_Mass_After_8_weeks_kg'] - df['Baseline_Muscle_Mass_kg'] 
    #Remove unecessary/irrelevant columns   
    df = df.iloc[0:, [4,7]]  
    #Sort the dataframe by hours training
    df.sort_values(by=['Resistance_Training_Hours_per_week'], inplace=True)
    #Check output  
    df.to_csv('result.csv',index=False)    
    

x = df.iloc[:,1]  
y = df.iloc[:,0]

# plt.plot(x,y)   

#Retrieve mean for each 
meanMuscleGain = df.groupby(["Resistance_Training_Hours_per_week"])["Muscle_Mass_Change_in_8_weeks"].mean()
plt.axis([0,10,0,5])   
plt.scatter(x,y,alpha=0.5, marker='x', color='orange', s=25)  
plt.yticks((0,1,2,3,4,5)) 
#Setting labels and title
plt.title("Clinical Trial: Mass Growth regarding Resistance Training") 
plt.ylabel("Training (Hours)")  
plt.xlabel("Muscle Mass (Kg)")    

#Plot the mean values
plt.scatter(meanMuscleGain,df["Resistance_Training_Hours_per_week"].unique(),color='red', s=125, label= "Mean", marker='x')  
plt.legend()

plt.grid(True, linestyle='--', alpha=0.7) 
statHours = {}
for hour in range(1,5):
    statHours[hour]= np.array(df[df['Resistance_Training_Hours_per_week']==hour]['Muscle_Mass_Change_in_8_weeks'].to_list())
for hour,values in statHours.items():
    print(f"Clinical Trial for those who worked out for {hour} hour/s had a mean of +{values.mean():2f}kgs") 
plt.show() 



    



