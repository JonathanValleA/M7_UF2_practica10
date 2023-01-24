import matplotlib.pyplot as plt
from ejercicio3A import load_data, total_cases_per_month_per_country, total_deaths_per_month_per_country, reproduction_rate_per_month_per_country
if __name__ == '__main__':
    data = load_data('df_covid19_countries.csv')
    df_cases = total_cases_per_month_per_country(data)
    df_deaths = total_deaths_per_month_per_country(data)
    df_rr = reproduction_rate_per_month_per_country(data)

    top_10_countries = total_cases_per_month_per_country(data)

    plt.figure(figsize=(13, 7))
    plt.title('Total cases per month per country')
    for country in top_10_countries['location'].unique():
        plt.plot(top_10_countries.loc[top_10_countries['location'] == country, 'month'],
                 top_10_countries.loc[top_10_countries['location'] == country, 'total_cases'],
                 label=country)
    plt.legend()
    plt.show()