print("CAR SALES ANALYSER")
import pandas as pd 
def pricecatogary(sellingprice):
    if sellingprice>100000:
        return 'Expensive'
    elif sellingprice<100000 and sellingprice>49999:
        return 'mid range'
    else:
        return "budget"
cars=pd.read_csv('car_prices.csv')
car=pd.DataFrame(cars)
shape= car.shape
print (shape)
print('First 15 Rows')
First15rows=car.head(15)
print (First15rows)
print('Last 10 rows')
last10rows=car.tail(10)
print(last10rows)
print('8 Random rows')
random8rows=car.sample(8)
print (random8rows)
totalcars=car['sellingprice'].count()
print ("Total no of cars :",totalcars)
aver= car['sellingprice'].mean()
print('Average selling price : ',aver)
print ("Most expensive car")
expensive=car['sellingprice'].idxmax(),['make','model','year','sellingprice']
print (car.loc[expensive])
print ('Cheapest Car')
cheap=car['sellingprice'].idxmin(),['make','model','year','sellingprice']
print (car.loc[cheap])
lessthan1lakht=car[car['sellingprice']<100000]
total=(lessthan1lakht['sellingprice'].count())
print('Total cars worth less then 100000 are :',total)
print (' Some Cars worth less than 1 lakh')
lessthan1lakh=car[car['sellingprice']<100000].head(10)
print(lessthan1lakh)
year2015=car[car['year']>2014]
ave=year2015['sellingprice'].mean()
print ('Average price of cars sold from 2015 :', ave)
ford=car[car['make']=='Ford']
print ("Total ford cars sold are :",ford['sellingprice'].count())
print('Some car filtered by Price<50000 and year>2010 ')
priceyear=car[(car['sellingprice']<50000)&(car['year']>2010)]
print(priceyear.head(5))
cond=car['condition'].isnull()
print("Total cars of which condition in unknown :",cond.count())
print('Top 15 Expensive cars')
sellpri=car.sort_values('sellingprice',ascending=False)
sellingpric=sellpri[['make','model','sellingprice','year']]
print (sellingpric.head(15))
print ('10 Oldest cars')
oldestcars=cars.sort_values('year',ascending=True).head(10)[['make','model','year','sellingprice']]
print (oldestcars)
print ("Cars sorted by make and selling price ")
makepricesort=car.sort_values(by=['make','sellingprice'],ascending=[True,True])
makepricesortp=makepricesort[['make','model','year','sellingprice']]
print (makepricesortp)
print('Car as per RANKS')
sellingpric['rank']=range(1,len(sellingpric)+1)
print(sellingpric.head(20))
print ("Car distribution - Brandwise")
gbybrands=car.groupby('make')['sellingprice'].sum()
print (gbybrands)
print('Top expensive brands')
rbrands=(gbybrands.sort_values(ascending=False).head(10).reset_index())
rbrands['rank']=range(1,len(rbrands)+1)
print (rbrands)
print ('Yearwise car count and average sales')
yearwise=car.groupby('year')['sellingprice'].mean()
print (yearwise)
print('Makewise maximum and minimum price')
brandsales=car.groupby('make')['sellingprice'].sum()
print("Maximum sales were done by brand",brandsales.idxmax(),"sales amount :Rs",brandsales.max())
print("Maximum sales were done by brand",brandsales.idxmin(),"sales amount :Rs",brandsales.min())
makeyearg=car.groupby(['make','year'])['sellingprice'].mean()
print (makeyearg)
car['age']=(2026-car['year'])
print(car[['make','year','model','sellingprice','age']])
car['price catogory']=car['sellingprice'].apply(pricecatogary)
print(car[['make','year','model','sellingprice','age','price catogory']])
car['value for money']=car['sellingprice']/car['age']
print(car[['make','year','model','sellingprice','age','price catogory','value for money']])
gbycond=car.groupby("condition")['sellingprice'].mean()
print(gbycond)
missingvalues=car.isnull().sum()
print(missingvalues)
car['condition'].fillna('Unknown')
car['model'].dropna()
print(car.shape)
print ("Total cars :",totalcars)
print ("Average price :",aver)
msold=car.groupby('make')['sellingprice'].count()
print ('Most sold brand :',msold)
gbybrands.to_csv('Brandwise report.csv',index=False)