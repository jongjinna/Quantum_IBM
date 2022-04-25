from qiskit_finance import QiskitFinanceError
from qiskit_finance.data_providers import *
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# data = RandomDataProvider(
#     tickers=["TICKER1", "TICKER2"],
#     start=datetime.datetime(2016, 1, 1),
#     end=datetime.datetime(2016, 1, 30),
#     seed=1,
# )
# data.run()

# means = data.get_mean_vector()
# print("Means:")
# print(means)

# rho = data.get_similarity_matrix()
# print("A time-series similarity measure:")
# print(rho)
# plt.imshow(rho)
# plt.show()

# cov = data.get_covariance_matrix()
# print("A covariance matrix:")
# print(cov)
# plt.imshow(cov)
# plt.show()

# print("The underlying evolution of stock prices:")
# for (cnt, s) in enumerate(data._tickers):
#     plt.plot(data._data[cnt], label=s)
# plt.legend()
# plt.xticks(rotation=90)
# plt.show()

# for (cnt, s) in enumerate(data._tickers):
#     print(s)
#     print(data._data[cnt])

# data = RandomDataProvider(
#     tickers=["CompanyA", "CompanyB", "CompanyC"],
#     start=datetime.datetime(2015, 1, 1),
#     end=datetime.datetime(2016, 1, 30),
#     seed=1,
# )
# data.run()
# for (cnt, s) in enumerate(data._tickers):
#     plt.plot(data._data[cnt], label=s)
# plt.legend()
# plt.xticks(rotation=90)
# plt.show()

# Access to closing-price time-series

# token = "y81d2awzxpoE-D5Fjifi"
# https://data.nasdaq.com/?modal=register
# 토큰 어떻게 쓰는 지 모르겠음


try:
    data = YahooDataProvider(
        tickers=["AEO", "ABBY", "AEP", "AAL", "AFN", "SLV"],
        start=datetime.datetime(2018, 1, 1),
        end=datetime.datetime(2018, 12, 31),
    )
    data.run()
    for (cnt, s) in enumerate(data._tickers):
        plt.plot(data._data[cnt], label=s)
    plt.legend(loc="upper center", bbox_to_anchor=(0.5, 1.1), ncol=3)
    plt.xticks(rotation=90)
    plt.show()
except QiskitFinanceError as ex:
    data = None
    print(ex)
        