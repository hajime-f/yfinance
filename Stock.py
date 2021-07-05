import matplotlib.pyplot as plt
from datetime import datetime as dt
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError

class Stock:

    code = None
    p_day = None
    p_minute = None

    def __init__(self, code, p_day, p_minute):

        self.code = code
        self.p_day = p_day
        self.p_minute = p_minute


    # 銘柄コード code の株価データを取得する
    def fetch_stock_data(self):

        company_code = str(self.code) + '.T'
        my_share = share.Share(company_code)
        stock_data = None
        
        try:
            stock_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                                 self.p_day,
                                                 share.FREQUENCY_TYPE_MINUTE,
                                                 self.p_minute)
        except YahooFinanceError as e:
            print(e.message)
            exit()
        
        return stock_data


    # リストに格納された int 型のミリ秒を datetime 型に変換する
    def convert_to_datetime_list(self, millisecond_list):

        return [dt.utcfromtimestamp(m / 1000) for m in millisecond_list]


    # 株価の折れ線グラフを描く
    def show_graph(self, stock_data):
        
        x_axis = self.convert_to_datetime_list(stock_data['timestamp'])
        y1_axis = stock_data['open']
        y2_axis = stock_data['high']
        y3_axis = stock_data['low']
        y4_axis = stock_data['close']

        plt.plot(x_axis, y1_axis, linestyle="solid")
        plt.plot(x_axis, y2_axis, linestyle="dashed")
        plt.plot(x_axis, y3_axis, linestyle="dashed")
        plt.plot(x_axis, y4_axis, linestyle="solid")

        plt.show()
        


        

