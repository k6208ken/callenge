import csv
import os 

def stock_input(file_name):

	stocks = []
	with open(file_name) as csvfile:
		rows = csv.DictReader(csvfile)
		for row in rows:
			integer = int(float(row['Adj Close']))
			stocks.append(integer)
	return stocks	


def three_days(data):
    output = []
    for i in range(len(data)):
        if i < 3:
            output.append(0)
        elif data[i] > data[i-1] > data[i-2] > data[i-3]:
            output.append(1)
        elif data[i] < data[i-1] < data[i-2] < data[i-3]:
            output.append(-1)
        else:
            output.append(0)
    return output

def count_gain(output,stock):
	out = []
	gain = 0
	count = 0
	for o in output:
		count += o
		print(count)
		if count > 1:
			out.append(0)
		elif count < -1:
			out.append(0)
		else:
			out.append(o)
	print(out)
	
	for i, j in zip(out, stock):
		gain += (i * j)
	print ('總共獲利{}元'.format(gain * 1000))
	
	# gain = [i * j for i, j in zip(out, stock)]
	


	# print(gain)
	

	
if __name__ == '__main__':
	stock = stock_input('2330.csv')
	output = three_days(stock)
	count_gain(output,stock)
	