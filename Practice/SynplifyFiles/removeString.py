import csv
import pandas as pd
'''
def createCSV(self):
		#Generate a CSV file with measurement data
	    csv_filename = str(dt.datetime.now().strftime("%Y%m%d_%H-%M"))+"_temperature.csv"
	    #filepath = "S:\\Engineering\\"+csv_filename
	    filepath = os.getcwd()+"\\"+csv_filename
	    print(filepath)
	    row = ["Time(s)", "Temp(C)", "Heat Power(%)", "Temp Setpoint(C)", 
	    		"Goldbar Temp (C)", "Ambient Temp (C)", "Torque (V)"]
	    with open(filepath, 'w', newline='') as csvFile:
	        writer = csv.writer(csvFile)
	        writer.writerow(row)
	    csvFile.close()
	    return filepath
'''

if __name__ == "__main__":
	'''
	input_file = open('top_legos_dm1_files.csv')
	output_file = open('output.csv', 'w')
	writer = csv.writer(output_file)
	with input_file as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		for row in csv_reader:
			#print(row.replace('"', ''))			
			#print(row)
			row = [value.replace('"', '')] for value in row
			writer.writerow(row)

	input_file.close()
	output_file.close()
	'''
	#https://stackoverflow.com/questions/11033590/change-specific-value-in-csv-file-via-python
	df = pd.read_csv("top_legos_v3ms_files.csv")
	split = df["Original"].str.split(" ", n=2, expand = True)
	df["add_file"] = split[0]
	df["group"] = split[1]
	df["filepath '' "] = split[2]
	
	df['group'] = df["group"].str.replace('-','')
	df['filepath'] = df["filepath '' "].str.replace('"', '')
	df.drop(["filepath '' "], axis=1, inplace = True)
	#df2 = df['Remove string']
	#df2.to_csv('clean.csv')
	
	#print(df)
	
	#df.dtypes
	df.to_csv('clean.csv')