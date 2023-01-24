import pandas as pd


def load_data(filepath):
    data = pd.read_csv(filepath)
    data['date'] = pd.to_datetime(data['date'])
    return data

def total_cases_per_month_per_country(data):
    data_grouped = data.groupby(['location']).sum(numeric_only=True)
    top_10_countries = data_grouped.nlargest(10, 'total_cases')
    data = data.query('location in @top_10_countries')
    data = data.groupby(['location', data['date'].dt.month])['total_cases'].sum().reset_index()
    return data

def total_deaths_per_month_per_country(data):
    df = data.groupby(['location', data['date'].dt.month])['total_deaths'].sum().reset_index()
    return df

def reproduction_rate_per_month_per_country(data):
    df = data.groupby(['location', data['date'].dt.month])['reproduction_rate'].mean().reset_index()
    return df