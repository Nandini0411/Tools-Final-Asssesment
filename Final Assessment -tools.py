import pandas as pd
import matplotlib.pyplot as plt

raw_data=pd.read_csv(r"C:\Users\nandi\Documents\PythonData1200\survey.csv")
raw_data.head()

def freq_mental_health_by_countries(df,sort_val,col_name):
    """
    This function will give us the distribution of frequency of mental health country wise
    df: The survey dataset as an argumnent
    col_name: a user-defined column
    sort_val: a user-defined sorting value
    It also calls the visulaise function for country wise displaye of mental health
    """
    
    #dataset with the count of total patient with mental health issue
    freq_country_total_df=df.groupby(sort_val)[col_name].count().reset_index()
    freq_country_total_df=freq_country_total_df.sort_values(col_name,ascending=False)
    print(freq_country_total_df)
    sorted_df=df[df[col_name]=='Yes']
    #dataset with the count of patient with mental health issue who sought for treatment
    freq_country_df=sorted_df.groupby(sort_val)[col_name].count().reset_index()
    freq_country_df=freq_country_df.sort_values(col_name,ascending=False)
    print(freq_country_df)
    #Calling the visualisation function to plot the two datasets
    visualise_country_wise(freq_country_total_df,freq_country_df,sort_val,col_name)

def visualise_country_wise(freq_country_total_df,freq_country_df,sort_val,col_name):
    
    #Plotting total patients country wise
    fig, ax=plt.subplots(figsize=(10,5))
    ax.bar(x=freq_country_total_df.Country,height=freq_country_total_df.treatment)
    plt.title("Country vs Total Patients")
    plt.xticks(rotation='vertical')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.tight_layout(h_pad=5)
    #Plotting patients that sought for treatment country wise
    fig1, ax1=plt.subplots(figsize=(10,5))
    ax1.bar(x=freq_country_df.Country,height=freq_country_df.treatment)
    plt.title("Country vs Patient who sought treatment")
    plt.xticks(rotation='vertical')
    plt.xlabel('Country')
    plt.ylabel('Count')
    plt.tight_layout(h_pad=5)

#Calling the function

freq_mental_health_by_countries(raw_data,"Country","treatment")


def visualise_state_wise(freq_state_total_df,freq_state_df,sort_val,col_name):
    
    #Plotting total patients country wise
    fig, ax=plt.subplots(figsize=(10,5))
    ax.bar(x=freq_state_total_df.state,height=freq_state_total_df.treatment)
    plt.title("State vs Total Patients")
    plt.xticks(rotation='vertical')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.tight_layout(h_pad=5)
    #Plotting patients that sought for treatment country wise
    fig1, ax1=plt.subplots(figsize=(10,5))
    ax1.bar(x=freq_state_df.state,height=freq_state_df.treatment)
    plt.title("State vs Patient who sought treatment")
    plt.xticks(rotation='vertical')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.tight_layout(h_pad=5)

def freq_mental_health_by_state(df,country_name,sort_val,col_name):
    """
    This function will give us the distribution of frequency of mental health state wise
    df: The survey dataset as an argument
    col_name: a user-defined column
    sort_val: a user-defined sorting value
    country_name: country specified by the user
    It also calls the visulaise function for country wise displaye of mental health
    """
    df1=df[df['Country']==country_name]
    #dataset with the count of total patient with mental health issue
    freq_state_total_df=df1.groupby(sort_val)[col_name].count().reset_index()
    freq_state_total_df=freq_state_total_df.sort_values(col_name,ascending=False)
    print(freq_state_total_df)
    sorted_df=df1[(df1[col_name]=='Yes') & (df1['Country']==country_name)]
    #dataset with the count of patient with mental health issue who sought for treatment
    freq_state_df=sorted_df.groupby(sort_val)[col_name].count().reset_index()
    freq_state_df=freq_state_df.sort_values(col_name,ascending=False)
    print(freq_state_df)
    #Calling the visualisation function to plot the two datasets
    visualise_state_wise(freq_state_total_df,freq_state_df,sort_val,col_name)

#Calling the function

country_name=input("Enter the country you want to sort by:")
freq_mental_health_by_state(raw_data,country_name,"state","treatment")


def attitude_awareness(df,sort_val,col_name):
    """
    This function will calculate either the attitude of the employer or the awareness of the employee regarding the mental health
    issues country wise. Following attributes lie in the attitude and awareness:
    Attitude:
    benefits: Does your employer provide mental health benefits?
    wellness_program: Has your employer ever discussed mental health as part of an employee wellness program?
    seek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?
    leave: How easy is it for you to take medical leave for a mental health condition?
    Awareness:
    care_options: Do you know the options for mental health care your employer provides?
    mental_health_consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?
    phys_health_consequence: Do you think that discussing a physical health issue with your employer would have negative consequences?
    coworkers: Would you be willing to discuss a mental health issue with your coworkers?
    supervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?
    mental_health_interview: Would you bring up a mental health issue with a potential employer in an interview?
    phys_health_interview: Would you bring up a physical health issue with a potential employer in an interview?
    mental_vs_physical: Do you feel that your employer takes mental health as seriously as physical health?
    
    df: The survey dataset as an argumnent
    col_name: a user-defined column
    sort_val: a user-defined sorting value
    It also calls the visulaise function for country wise displays of mental health
    """
    #dataset with the count of patient with mental health issue who had answers other than yes to the question
    not_yes_df=df[df[col_name]!='Yes']
    Total_df=not_yes_df.groupby(sort_val)[col_name].count().reset_index()
    Total_df=Total_df.sort_values(col_name,ascending=False)
    print(Total_df)
    sorted_df=df[df[col_name]=='Yes']
    #dataset with the count of patient with mental health issue who had yes as the answer to the question
    Yes_df=sorted_df.groupby(sort_val)[col_name].count().reset_index()
    Yes_df=Yes_df.sort_values(col_name,ascending=False)
    print(Yes_df)
    #Calling the visualisation function to plot the two datasets
    visualise_attitude_awareness(Total_df,Yes_df,sort_val,col_name)

def visualise_attitude_awareness(Total_df,Yes_df,sort_val,col_name):
    
    #Plotting total patients country wise
    fig, ax=plt.subplots(figsize=(10,5))
    if(col_name=='benefits'):
        ax.bar(x=Total_df.Country,height=Total_df.benefits)
    elif(col_name=='wellness_program'):
        ax.bar(x=Total_df.Country,height=Total_df.wellness_program)
    elif(col_name=='seek_help'):
        ax.bar(x=Total_df.Country,height=Total_df.seek_help)
    elif(col_name=='leave'):
        ax.bar(x=Total_df.Country,height=Total_df.leave)
    elif(col_name=='care_options'):
        ax.bar(x=Total_df.Country,height=Total_df.care_options)
    elif(col_name=='mental_health_consequence'):
        ax.bar(x=Total_df.Country,height=Total_df.mental_health_consequence)
    elif(col_name=='phys_health_consequence'):
        ax.bar(x=Total_df.Country,height=Total_df.phys_health_consequence)
    elif(col_name=='coworkers'):
        ax.bar(x=Total_df.Country,height=Total_df.coworkers)
    elif(col_name=='supervisor'):
        ax.bar(x=Total_df.Country,height=Total_df.supervisor)
    elif(col_name=='mental_health_interview'):
        ax.bar(x=Total_df.Country,height=Total_df.mental_health_interview)
    elif(col_name=='mental_vs_physical'):
        ax.bar(x=Total_df.Country,height=Total_df.mental_vs_physical)
    elif(col_name=='phys_health_interview'):
        ax.bar(x=Total_df.Country,height=Total_df.phys_health_interview)
    plt.title("Count of patient who didn't say yes")
    plt.xticks(rotation='vertical')
    plt.xlabel('Country')
    plt.ylabel("Count of patients")
    plt.tight_layout(h_pad=5)
    
    #Plotting patients that sought for treatment country wise
    fig1, ax1=plt.subplots(figsize=(10,5))
    if(col_name=='benefits'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.benefits)
    elif(col_name=='wellness_program'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.wellness_program)
    elif(col_name=='seek_help'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.seek_help)
    elif(col_name=='leave'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.leave)
    elif(col_name=='care_options'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.care_options)
    elif(col_name=='mental_health_consequence'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.mental_health_consequence)
    elif(col_name=='phys_health_consequence'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.phys_health_consequence)
    elif(col_name=='coworkers'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.coworkers)
    elif(col_name=='supervisor'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.supervisor)
    elif(col_name=='mental_health_interview'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.mental_health_interview)
    elif(col_name=='mental_vs_physical'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.mental_vs_physical)
    elif(col_name=='phys_health_interview'):
        ax1.bar(x=Yes_df.Country,height=Yes_df.phys_health_interview)
    plt.title("Count of patients who said yes")
    plt.xticks(rotation='vertical')
    plt.xlabel('Country')
    plt.ylabel('Count of patients who said yes')
    plt.tight_layout(h_pad=5)

#Calling the function

attitude_awareness_var=input("Enter the information you want to know:\nAttitude:\nbenefits: Does your employer provide mental health benefits?\nwellness_program: Has your employer ever discussed mental health as part of an employee wellness program?\nseek_help: Does your employer provide resources to learn more about mental health issues and how to seek help?\nleave: How easy is it for you to take medical leave for a mental health condition?\nAwareness:\ncare_options: Do you know the options for mental health care your employer provides\nmental_health_consequence: Do you think that discussing a mental health issue with your employer would have negative consequences?\nphys_health_consequence: Do you think that discussing a physical health issue with your employer would have negative consequences?\ncoworkers: Would you be willing to discuss a mental health issue with your coworkers?\nsupervisor: Would you be willing to discuss a mental health issue with your direct supervisor(s)?\nmental_health_interview: Would you bring up a mental health issue with a potential employer in an interview?\nphys_health_interview: Would you bring up a physical health issue with a potential employer in an interview?\nmental_vs_physical: Do you feel that your employer takes mental health as seriously as physical health?")
attitude_awareness(raw_data,"Country",attitude_awareness_var)