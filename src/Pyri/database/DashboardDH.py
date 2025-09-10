from datetime import datetime
import csv
import shutil
from pathlib import Path
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



            
            
        
        
