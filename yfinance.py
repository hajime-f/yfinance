from Stock import Stock

if __name__ == '__main__':
    
    code = 2158  # FRONTEO
    p_day = 30
    p_minute = 5

    stock = Stock(code, p_day, p_minute)
    
    stock_data = stock.fetch_stock_data()
    
    stock.show_graph(stock_data)


    
