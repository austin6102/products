import os


products = []
if os.path.isfile('products.csv'):
	print('have file')
	with open('products.csv' , 'r' ) as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name,price=line.strip().split(',')
			products.append([name,price])
	if(len(products)>0):
		for a in products:
			print(products)	

else:
	print('no file')

#讀取檔案
products =[]


#讓使用者輸入
while True:
	name = input('請輸入商品名稱:' )
	if name == 'q':
		break 
	price = input('請輸入商品價格: ')
	products.append([name , price])

if(len(products)>=2):	
	print(products)

#印出檔案
for p in products:
	print(p[0],'的價格是' , p[1])

with open('products.csv' , 'w') as f:
	f.write('商品' + ',' + '價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')