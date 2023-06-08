"""
Benjamin Granat
    ITP-449
    Assignment 5
    Produces visualizations from data contained
    in Avocados dataset.
"""
import pandas as pd
import matplotlib.pyplot as plt


def main():
    # Makes sure all columns in df are printed:
    pd.set_option('display.width', None)
    # Import file into pandas df
    file_path = 'avocado.csv'
    # Read csv file
    df_avocados = pd.read_csv(file_path)
    # Drop unneeded attributes
    df_slimmed = df_avocados[['Date', 'AveragePrice', 'Total Volume']]
    # Convert to datetime
    df_slimmed['Date'] = pd.to_datetime(df_slimmed['Date'])
    # Creates dataframe
    df = pd.DataFrame(df_slimmed)
    # Sorts values by date
    df.sort_values(by='Date', inplace=True)

    # Creates subplots
    fig, ax = plt.subplots(2, 3)
    date_list = df['Date'].tolist()

    # Scatter plots of raw data
    ax[0, 0].scatter(df['Date'], df['AveragePrice'])
    ax[0, 0].set_title('Raw', fontsize=9)
    ax[0, 0].set_ylabel('Average Price (USD)', fontsize=9)
    ax[0, 0].set_xticklabels(date_list, fontsize=5, rotation='vertical')
    ax[1, 0].scatter(df['Date'], df['Total Volume'])
    ax[1, 0].set_ylabel('Total Volume (millions)', fontsize=9)
    ax[1, 0].set_xlabel('Date', fontsize=9)
    ax[1, 0].set_xticklabels(date_list, fontsize=5, rotation='vertical')

    # Plots of aggregated averagePrice & Total Volume vs. Time
    # Calulates total revenue and recalculates average price
    df['TotalRevenue'] = df['AveragePrice'] * df['Total Volume']
    df = df.groupby('Date').sum()
    df['AveragePrice'] = df['TotalRevenue'] / df['Total Volume']
    ax[0, 1].plot(df['AveragePrice'])
    ax[0, 1].set_title('Aggregated', fontsize=9)
    ax[0, 1].set_xticklabels(date_list, fontsize=5, rotation='vertical')
    ax[1, 1].plot(df['Total Volume'])
    ax[1, 1].set_xlabel('Date', fontsize=9)
    ax[1, 1].set_xticklabels(date_list, fontsize=5, rotation='vertical')

    # Plots of smoothed and aggregated averagePrice & total volume vs. time
    df = df.rolling(20).mean()
    ax[0, 2].plot(df['AveragePrice'])
    ax[0, 2].set_title('Smoothed and Aggregated', fontsize=9)
    ax[0, 2].set_xticklabels(date_list, fontsize=5, rotation='vertical')
    ax[1, 2].plot(df['Total Volume'])
    ax[1, 2].set_xlabel('Date', fontsize=9)
    ax[1, 2].set_xticklabels(date_list, fontsize=5, rotation='vertical')

    # Converts figure's layout and title
    # Saves file as a png
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.suptitle('Avocado Prices and Volume Time Series')
    plt.savefig('avocados_prices_volume_time_series.png')
    print(df['Date']['Total Volume'])


if __name__ == '__main__':
    main()