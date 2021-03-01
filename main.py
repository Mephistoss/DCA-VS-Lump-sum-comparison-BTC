import numpy as np
from matplotlib import pyplot as plt


def compare_dca_vs_lump(btc_price_data, dca_buy_size):

    lump_buy = 1000
    length_data = len(btc_price_data)
    lump_btc = []
    dca_btc = []
    col = []
    days_dca = 0
    days_lump = 0
    days = list(range(0, len(btc_price_data)))
    dca_margin = 0
    lump_margin = 0
    remove_days = int(lump_buy / dca_buy_size)

    for i in range(length_data):
        lump_btc.append(lump_buy / btc_price_data[i])

    for j in range(length_data - remove_days):
        dca_buy = 0
        for k in range(remove_days):
            dca_buy = dca_buy + dca_buy_size / btc_price_data[j + k]
        dca_btc.append(dca_buy)

    lump_btc = lump_btc[:len(lump_btc) - remove_days]

    for i in range(len(lump_btc)):
        if dca_btc[i] >= lump_btc[i]:
            days_dca = days_dca + 1
            dca_margin = dca_margin + ((dca_btc[i] - lump_btc[i]) / lump_btc[i] * 100)
            col.append("blue")
        else:
            days_lump = days_lump + 1
            col.append("red")
            lump_margin = lump_margin + ((lump_btc[i] - dca_btc[i]) / dca_btc[i] * 100)

    dca_margin = dca_margin / days_dca
    lump_margin = lump_margin / days_lump
    probability = days_dca/(days_dca + days_lump) * 100

##################
# Graphing disabled to increase speed


    # plt.title("Comparison of DCA vs Lump-sum investment strategies")
    # plt.ylabel("Price of BTC ($)")
    # plt.xlabel("Days since BLX tracker began")
    # for i in range(len(column_list)-remove_days):
    #     plt.scatter(days[i], btc_price_data[i], c=col[i], s=3, linewidth=0)
    # #plt.plot(days, column, "black")
    # plt.figtext(.6, .6, "Blue = DCA Superior")
    # plt.figtext(.6, .55, "Red = Lump Sum Superior")
    # plt.yscale("log")
    # plt.show()

##################
    #return probability, dca_margin, lump_margin
    return probability

price_data = np.genfromtxt("BNC BLX, 1D.csv", delimiter=",")
column = price_data[1:, 4]

column_list = column.tolist()

# perc, dca, lump = compare_dca_vs_lump(column_list, 10)
# print(perc)
# print(dca)
# print(lump)
test1 = compare_dca_vs_lump(column_list, 10)
print(test1)
test2 = compare_dca_vs_lump(column_list, 20)
print(test2)
test3 = compare_dca_vs_lump(column_list, 50)
print(test3)
test4 = compare_dca_vs_lump(column_list, 100)
print(test4)
test5 = compare_dca_vs_lump(column_list, 200)
print(test5)


