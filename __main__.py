from app import MercadonaScrapper
import pandas as pd

res = MercadonaScrapper().get_products()

pd.DataFrame(
    [p.columnas for p in res]#,
    #columns=['title', 'link', 'price']
).to_csv('result.csv')
