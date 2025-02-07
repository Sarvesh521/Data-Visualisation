import plotly.express as px
import pandas as pd

def calculate_cat_time_occ(time_occ):
    if int(time_occ) % 100 < 30:
        x = int(time_occ / 100) * 100
    else:
        x = (int(time_occ / 100) + 1) * 100
    x = str(x).zfill(4)
    return x[:2] + ':' + x[2:]

def load_data():
    df = pd.read_csv('Cleaned_LA_Dataset.csv')
    df['Cat_Time_Occ'] = df['TIME OCC'].apply(calculate_cat_time_occ)
    df['Vict Sex Label'] = df['Vict Sex'].map({'M': 'Male', 'F': 'Female', 'X': 'Unknown'})

    print("Data loaded successfully")
    return df

def create_treemap(df, path, title, labels, branchvalues, color=None, color_discrete_map=None):
    fig = px.treemap(
        df,
        path=path,
        values='Cnt_Crm_Cd',
        title=title,
        labels=labels,
        branchvalues=branchvalues,
        color=color,
        color_discrete_map=color_discrete_map
    )
    return fig

def save_figure(fig, filename_prefix):
    fig_json = fig.to_json()
    with open(f'{filename_prefix}.json', 'w') as f:
        f.write(fig_json)
    fig.write_html(f'{filename_prefix}.html')
    print(f"Treemap data saved to {filename_prefix}.json")
    print(f"Treemap HTML saved to {filename_prefix}.html")

def process_gender_time_crime(df):
    df['Cnt_Crm_Cd'] = df.groupby(['Vict Sex', 'Cat_Time_Occ', 'Part 1-2'])['Crm Cd'].transform('count')
    paths = [
        ('total', 'crime_victsex_hr_total'),
        ('remainder', 'crime_victsex_hr_remainder')
    ]
    for branchvalues, filename in paths:
        fig = create_treemap(
            df,
            path=[px.Constant('Victims'), 'Vict Sex Label', 'Cat_Time_Occ', 'Part 1-2', 'Cnt_Crm_Cd'],
            title='Gender-wise Distribution of Crimes by Time of Day and Crime Seriousness',
            labels={'Cnt_Crm_Cd': 'Number of Crimes Committed'},
            branchvalues=branchvalues
        )
        save_figure(fig, filename) 

def process_gender_premises_crime(df):
    df['Part 1-2'] = df['Part 1-2'].astype(str)
    df_agg = df.groupby(['Vict Sex Label', 'Premis Desc', 'Part 1-2']).agg({'Crm Cd': 'count'}).reset_index()
    df_agg.rename(columns={'Crm Cd': 'Cnt_Crm_Cd'}, inplace=True)
    paths = [
        ('total', 'crime_victsex_premis_type_total'),
        ('remainder', 'crime_victsex_premis_type_remainder')
    ]
    for branchvalues, filename in paths:
        fig = create_treemap(
            df_agg,
            path=[px.Constant('Victims'), 'Vict Sex Label', 'Premis Desc', 'Part 1-2', 'Cnt_Crm_Cd'],
            title='Gender-wise Distribution of Crimes by Premises Type and Crime Seriousness',
            labels={
                'Cnt_Crm_Cd': 'Number of Crimes Committed',
                'Premis Desc': 'Premises Description'
            },
            branchvalues=branchvalues
        )
        save_figure(fig, filename)

def process_crime_description(df):
    df['Cnt_Crm_Cd'] = df.groupby(['Crm Cd Desc', 'Vict Sex', 'Part 1-2'])['Crm Cd'].transform('count')
    df_agg = df.groupby(['Crm Cd Desc', 'Vict Sex', 'Part 1-2']).agg({'Cnt_Crm_Cd': 'sum'}).reset_index()
    df_agg['Vict Sex'] = df_agg['Vict Sex'].map({'M': 'Male', 'F': 'Female', 'X': 'Unknown'})
    df_agg = df_agg[df_agg['Vict Sex'] != 'Unknown']
    paths = [
        ('total', 'crime_crimedesc_victsex_crimetype_total'),
        ('remainder', 'crime_crimedesc_victsex_crimetype_remainder')
    ]
    for branchvalues, filename in paths:
        fig = create_treemap(
            df_agg,
            path=[px.Constant('Crime Description'), 'Crm Cd Desc', 'Vict Sex', 'Cnt_Crm_Cd'],
            title='Distribution of Crimes by Description, Gender, and Crime Seriousness',
            labels={
                'Cnt_Crm_Cd': 'Number of Crimes Committed',
                'Crm Cd Desc': 'Crime Description',
                'Vict Sex': 'Gender',
                'Part 1-2': 'Crime Seriousness (1: Serious Crimes, 2: Non-Serious Crimes)'
            },
            branchvalues=branchvalues,
            color='Part 1-2',
            color_discrete_map={'1': 'darkred', '2': 'orange', '(?)': 'grey'}
        )
        save_figure(fig, filename)

def process_victim_descent(df):
    df1 = df.copy()
    df1 = df1[df1['Vict Descent'] != 'X']
    df1 = df1[df1['Weapon Desc'] != 'Unknown']
    df1 = df1.dropna(subset=['Premis Desc', 'Weapon Desc', 'Vict Descent'])
    vict_desc_mapping = {
        'A': 'Other Asian', 'B': 'Black', 'C': 'Chinese', 'D': 'Cambodian', 'F': 'Filipino',
        'G': 'Guamanian', 'H': 'Hispanic/Latin/Mexican', 'I': 'American Indian/Alaskan Native',
        'J': 'Japanese', 'K': 'Korean', 'L': 'Laotian', 'O': 'Other', 'P': 'Pacific Islander',
        'S': 'Samoan', 'U': 'Hawaiian', 'V': 'Vietnamese', 'W': 'White', 'Z': 'Asian Indian'
    }
    df1['Vict Descent'] = df1['Vict Descent'].map(vict_desc_mapping)
    df1['Cnt_Crm_Cd'] = df1.groupby(['Vict Descent', 'Premis Desc', 'Weapon Desc', 'Part 1-2'])['Crm Cd'].transform('count')
    paths = [
        ('total', 'crime_victdesc_crimedesc_weapondesc_crimetype_total'),
        ('remainder', 'crime_victdesc_crimedesc_weapondesc_crimetype_remainder')
    ]
    for branchvalues, filename in paths:
        fig = create_treemap(
            df1,
            path=[px.Constant('Victim Descent'), 'Vict Descent', 'Premis Desc', 'Weapon Desc', 'Part 1-2', 'Cnt_Crm_Cd'],
            title='Distribution of Crimes by Victim Descent, Premises, Weapon Description, and Crime Seriousness',
            labels={'Cnt_Crm_Cd': 'Number of Crimes Committed'},
            branchvalues=branchvalues
        )
        save_figure(fig, filename)

def main():
    df = load_data()
    process_gender_time_crime(df)
    process_gender_premises_crime(df)
    process_crime_description(df)
    process_victim_descent(df)

if __name__ == '__main__':
    main()