from datetime import datetime
import csv
import shutil
from pathlib import Path
import matplotlib.pyplot as plt
base_path = Path(__file__).parent.parent.parent.parent

class DashboardDataHandler:
    
    def Todaysale(self):
        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.sales_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.today_sale_value=0
            for i in self.reader:
                if i["Sale Date"] == self.current_date:
                    self.today_sale_value = int(self.today_sale_value) + int(i["Sale value"])

        return self.today_sale_value



    def Todayprofit(self):
        self.sales_csv_filepath= base_path / "data" / "database" / "sales.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.sales_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.today_profit_value=0
            for i in self.reader:
                if i["Sale Date"] == self.current_date:
                    self.today_profit_value = int(self.today_profit_value) + int(i["Net profit"])

        return self.today_profit_value

    def Monthprofit(self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "stocklog" /"sales_log.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.month_profit_value=0
            for i in self.reader:
                if i["Sale Date"][-7:] == self.current_date[-7:]:
                    self.month_profit_value = int(self.month_profit_value) + int(i["Net profit"])

        return self.month_profit_value

    def Monthsale(self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "stocklog" /"sales_log.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.month_sale_value=0
            for i in self.reader:
                if i["Sale Date"][-7:] == self.current_date[-7:]:
                    self.month_sale_value = int(self.month_sale_value) + int(i["Sale value"])

        return self.month_sale_value

    def TotalStock(self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "inventory.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.total_stock_value=0
            for i in self.reader:
                    self.total_stock_value = int(self.total_stock_value) + int(i["Stock value"])

        return self.total_stock_value
    
    def Demandcount(self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "demand.csv"
        self.current_date=datetime.now().strftime("%d-%m-%Y")
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.demand_count=0
            for i in self.reader:
                    self.demand_count+=1

        return self.demand_count
    
    def getsaledata(date,self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "stocklog" /"sales_log.csv"
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.sale_on_date=0
            for i in self.reader:
                if i["Sale Date"] == date:
                    self.sale_on_date=int(self.sale_on_date)+int(i["Sale value"])

        return self.sale_on_date
                    


    def salesgraph(self):
        self.date_range=["01", '02','03','04','05','06','07','08','09','10','11',"12",'13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',"31"]
        self.month_sale_data={}
        self.current_date=datetime.now().strftime("-%m-%Y")
        self.sales_graph_path=base_path / "src" / "images" / "Dashboard_graphs" / "Month_sales.png"
        for i in self.date_range:
            self.month_sale_data[int(i)]=DashboardDataHandler.getsaledata(str(i)+self.current_date,self)

        self.graph_days=list(self.month_sale_data.keys())
        self.graph_sale=list(self.month_sale_data.values())

        plt.figure(figsize=(12,5),dpi=100)

        plt.plot(self.graph_days,self.graph_sale,marker="o",linestyle="-",color="blue")
        plt.title("Monthly sales")
        plt.xlabel("Day",fontsize=16)
        plt.ylabel("Sale value",fontsize=16)
        plt.savefig(self.sales_graph_path,dpi=100)
        plt.close()


    def getprofitdata(date,self):
        self.saleslog_csv_filepath= base_path / "data" / "database" / "stocklog" /"sales_log.csv"
        with open(self.saleslog_csv_filepath,"r",newline="")as f:
            self.reader=csv.DictReader(f)
            self.profit_on_date=0
            for i in self.reader:
                if i["Sale Date"] == date:
                    self.profit_on_date=int(self.profit_on_date)+int(i["Net profit"])

        return self.profit_on_date

    def profitgraph(self):
        self.date_range=["01", '02','03','04','05','06','07','08','09','10','11',"12",'13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30',"31"]
        self.month_profit_data={}
        self.current_date=datetime.now().strftime("-%m-%Y")
        self.profit_graph_path=base_path / "src" / "images" / "Dashboard_graphs" / "Month_profit.png"
        for i in self.date_range:
            self.month_profit_data[int(i)]=DashboardDataHandler.getprofitdata(str(i)+self.current_date,self)

        self.graph_days=list(self.month_profit_data.keys())
        self.graph_profit=list(self.month_profit_data.values())

        plt.figure(figsize=(12,5),dpi=100)

        plt.plot(self.graph_days,self.graph_profit,marker="o",linestyle="-",color="blue")
        plt.title("Monthly profit")
        plt.xlabel("Day",fontsize=16)
        plt.ylabel("Net profit",fontsize=16)
        plt.savefig(self.profit_graph_path,dpi=100)
        plt.close()
        
        
        

        
                    
                    
                    
                    
                    


























        
        
            
            
        
        
