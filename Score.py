#Importar Librerias
import yfinance as yf
import pandas as pd

#Identificar algunas empresas
Port1= ["GFI","GOLD","NEM","AEM"]

#identificar solicitud financiera transformada por cada variable 
yf.Ticker("GOLD").financials.iloc[:,0]["Net Income"]

#identificar solicitud fecha financiera transformada por cada variable 
date = yf.Ticker("GOLD").balance_sheet.columns[0].strftime("%Y-%m-%d")
print(date)

tax_rate = 0.35  # Tax Rate

###DEFINIR LA FUNCION F-PIOTROSKI YEARLY
def get_stock_data(au):
  stock = yf.Ticker(au)

  try:
    Net_Income = stock.financials.iloc[:,0]["Net Income"]
    Total_Assets = stock.balance_sheet.iloc[:,0]["Total Assets"]
    Net_Income2 = stock.financials.iloc[:,1]["Net Income"]
    Total_Assets2 = stock.balance_sheet.iloc[:,1]["Total Assets"]
    Current_Assets = stock.balance_sheet.iloc[:,0]["Current Assets"]
    Current_Liabilities= stock.balance_sheet.iloc[:,0]["Current Liabilities"]
    Current_Assets2 = stock.balance_sheet.iloc[:,1]["Current Assets"]
    Current_Liabilities2= stock.balance_sheet.iloc[:,1]["Current Liabilities"]
    Shares =stock.balance_sheet.iloc[:,0]["Ordinary Shares Number"]
    Shares2=stock.balance_sheet.iloc[:,1]["Ordinary Shares Number"]
    date =  stock.balance_sheet.columns[0].strftime("%Y-%m-%d")
    date2 =  stock.balance_sheet.columns[1].strftime("%Y-%m-%d")
    tot_deb=stock.balance_sheet.iloc[:,0]["Total Debt"]
    tot_deb2=stock.balance_sheet.iloc[:,1]["Total Debt"]
    wc=stock.balance_sheet.iloc[:,0]["Working Capital"]
    wc2=stock.balance_sheet.iloc[:,1]["Working Capital"]
    tc=stock.balance_sheet.iloc[:,0]["Total Capitalization"]
    tc2=stock.balance_sheet.iloc[:,1]["Total Capitalization"]
    tl=stock.balance_sheet.iloc[:,0]["Total Liabilities Net Minority Interest"]
    tl2=stock.balance_sheet.iloc[:,1]["Total Liabilities Net Minority Interest"]
    tn1=stock.balance_sheet.iloc[:,0]["Total Non Current Liabilities Net Minority Interest"]
    tn2=stock.balance_sheet.iloc[:,1]["Total Non Current Liabilities Net Minority Interest"]


##Método Indirecto: Comienza desde la utilidad neta y ajusta por los cambios en cuentas relacionadas con las operaciones
#(como cuentas por cobrar, inventarios, cuentas por pagar) y los gastos no monetarios (como depreciación y amortización).
#Este método es más común porque parte del estado de resultados y el balance, que son más fáciles de obtener que un desglose
#completo de los flujos de efectivo.

    depreciation = stock.financials.iloc[:,0]["Reconciled Depreciation"] # Reconciled Depreciation
    total_unusual_items = stock.financials.iloc[:,0]["Total Unusual Items"]* (1 - tax_rate) # Total Unusual

 #OPERATION CASH FLOW
    OPC= stock.cashflow.iloc[32,0]

# CRPY =stock.balance_sheet["12-31-2023"]["Current Ratio Previous Year"]
    Long_debt=stock.balance_sheet.iloc[:,0]["Long Term Debt"]
    Long_debt2=stock.balance_sheet.iloc[:,1]["Long Term Debt"]
    gross_profit=stock.financials.iloc[:,0]["Gross Profit"]
    gross_profit2=stock.financials.iloc[:,1]["Gross Profit"]
    tot_revenue =stock.financials.iloc[:,0]["Total Revenue"]
    tot_revenue2 =stock.financials.iloc[:,1]["Total Revenue"]
    df = {"Variable": [
        f"{date} Net Income",
        f"{date} Total Assets",
        f"{date2} Net Income ",
        f"{date2} Total Assets",
        f"{date} Current Assets",
        f"{date} Current Liabilities",
        f"{date2} Current Assets ",
        f"{date2} Current Liabilities  ",
        f"{date} Ordinary Shares Number",
        f"{date2} Ordinary Shares Number",
        f"{date} Reconciled Depreciation",
        f"{date} Total Unusual Items",
        f"{date} Operating Cash Flow (OPC)",
        f"{date} Long Term Debt",
        f"{date2} Long Term Debt",
        f"{date} Gross Profit",
        f"{date2} Gross Profit",
        f"{date} Total Revenue",
        f"{date2} Total Revenue",
        f"{date} Total Debt",
        f"{date2} Total Debt ",

          f"{date} Working Capital",
        f"{date2} Working Capital",

          f"{date} Total Capitalization",
        f"{date2} Total Capitalization",

          f"{date} Total Liabilities Net Minority Interest",
        f"{date2} Total Liabilities Net Minority Interest ",

          f"{date} Total Non Current Liabilities Net Minority Interest",
        f"{date2} Total Non Current Liabilities Net Minority Interest ",
        ],"Value": [
        Net_Income,
        Total_Assets,
        Net_Income2,
        Total_Assets2,
        Current_Assets,
        Current_Liabilities,
        Current_Assets2,
        Current_Liabilities2,
        Shares,
        Shares2,
        depreciation,
        total_unusual_items,
        OPC,
        Long_debt,
        Long_debt2,
        gross_profit,
        gross_profit2,
        tot_revenue,
        tot_revenue2,
        tot_deb,
        tot_deb2,
        wc,
        wc2,
        tc,
        tc2,
        tl,
        tl2,
        tn1,
        tn2



        ]}


    df = pd.DataFrame(df)
    pd.options.display.float_format = '{:,.2f}'.format
    return df
  except Exception as e:
      print(f"Error al obtener datos: {e}")
      return None
