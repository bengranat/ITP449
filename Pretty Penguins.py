""" Benjamin Granat
    ITP-449
    Assignment 4
    Produces visualizations - Scatterplot matrix and single Scatterplot
    Data: Palmer Penguins dataset
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    #Reads penguins file
    file_path = "penguins.csv"
    penguins_df = pd.read_csv(file_path)
    #Creates subplots
    fig, ax = plt.subplots(4, 4)
    plt.figure(1)
    #Converts pandas data frame columns into lists
    data_a = penguins_df.bill_length_mm.tolist()
    data_b = penguins_df.bill_depth_mm.tolist()
    data_c = penguins_df.flipper_length_mm.tolist()
    data_d = penguins_df.body_mass_g.tolist()

    #Plots each individual subplot (since we were not allowed to use pandas for plotting)
    #Labels for x and y axises for each can be found at the bottom/left of the page
    #Individual line charts are titled by the metric they show
    ax[0, 0].plot(data_a)
    ax[0, 0].set_title('bill_length_mm', fontsize = 9)
    ax[0, 0].set_ylabel('bill_length_mm', fontsize = 6)
    ax[0, 1].scatter(data_a, data_b, s = 2)
    ax[0, 2].scatter(data_a, data_c, s = 2)
    ax[0, 3].scatter(data_a, data_d, s = 2)

    ax[1, 1].plot(data_b)
    ax[1, 1].set_title('bill_depth_mm', fontsize = 9)
    ax[1, 0].scatter(data_b, data_a, s = 2)
    ax[1, 0].set_ylabel('bill_depth_mm', fontsize = 6)
    ax[1, 2].scatter(data_b, data_c, s = 2)
    ax[1, 3].scatter(data_b, data_d, s = 2)

    ax[2, 2].plot(data_c)
    ax[2, 2].set_title('flipper_length_mm', fontsize = 9)
    ax[2, 0].scatter(data_c, data_a, s = 2)
    ax[2, 0].set_ylabel('flipper_length_m', fontsize = 6)
    ax[2, 1].scatter(data_c, data_b, s = 2)
    ax[2, 3].scatter(data_c, data_d, s = 2)

    ax[3, 3].plot(data_d)
    ax[3, 3].set_title('body_mass_g', fontsize = 9)
    ax[3, 3].set_xlabel('body_mass_g', fontsize = 6)
    ax[3, 0].scatter(data_d, data_a, s = 2)
    ax[3, 0].set_ylabel('body_mass_g', fontsize = 6)
    ax[3, 0].set_xlabel('bill_length_mm', fontsize = 6)
    ax[3, 1].scatter(data_d, data_b, s = 2)
    ax[3, 1].set_xlabel('bill_depth_mm', fontsize = 6)
    ax[3, 2].scatter(data_d, data_c, s = 2)
    ax[3, 2].set_xlabel('flipper_length_mm', fontsize = 6)
    fig.tight_layout()
    fig.suptitle('Penguins Attributes Scatterplot Matrix')
    plt.savefig('penguins_attributes_scatterplot_matrix.png')

    #Converts all species values into a list
    data_e = penguins_df.species.tolist()
    color_list = []
    color = ''
    #Branched if statements to output color depending on species values
    for i in data_e:
        if i == "Adelie":
            color = 'r'
            color_list.append(color)
        if i == "Chinstrap":
            color = 'b'
            color_list.append(color)
        if i == "Gentoo":
            color = 'g'
            color_list.append(color)
    #Figure 2 - Single Scatter plot
    fig2, ax2 = plt.subplots()
    plt.figure(2)
    plt.scatter(data_a, data_c, c=color_list, s = 10)
    ax2.set_title('bill_length vs. flipper_length_mm')
    ax2.set_xlabel('bill_length_mm')
    ax2.set_ylabel('flipper_length_mm')
    ax2.legend(color_list[0])
    plt.savefig('penguins_bill_flipper_by_species.png')

    #Unfortunately, when I try to set ax.legend to -
    #ax2.legend(color_list, data_e, etc.)
    # - it does not work. As a result, the second png only has a legend that contains the color red.
    #I am not exactly sure how to get around this. Please let me know. Thank you.


if __name__ == '__main__':
    main()