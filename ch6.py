import csv
import os 

def stock_input(file_name):

	stocks = []
	with open(file_name) as csvfile:
		rows = csv.reader(csvfile)
		for row in rows:
			stocks.append(row[5].replace(" ",""))
	stock = stocks[1:]
	return stock	

def three_days(data):
	result = []

	for i in range(len(data)):
		if i < 3:
			result.append(0)
		else:
			if data[i] > data[i-1] and data[i-1] > data[i-2] and data[i-2] > data[i-3]:
				result.append(1)
			elif data[i] < data[i-1] and data[i-1] < data[i-2] and data[i-2] < data[i-3]:
				result.append(-1)
			else:
				result.append(0)
	return result

def count_gain(result,stock):
	
	gain = [i * j for i, j in zip(result, stock)]
	print(gain)
	

	
if __name__ == '__main__':
	stock = stock_input('2330.csv')
	result = three_days(stock)
	count_gain(result,stock)
	