import csv
#csv file from which the original data is read
with open('hr.contract (8).csv') as csvfile1: 
	#csv file to which new data is written
	with open('csvfile.csv','w') as csvfile2:
		#the keys in the new csv file
		fieldnames = ['External ID', 'Allowances', 'Allowances/Amount']
		#the row values in the old csv file are assigned to "reader"
		reader = csv.DictReader(csvfile1)  
		#write the headers in the new csv file
		writer = csv.DictWriter(csvfile2,fieldnames=fieldnames)
		writer.writeheader()
		#main data conversion 
		for row in reader: 
			writer.writerow({'External ID': row['External ID'],  
				'Allowances': '__export__.hr_payroll_allowance_line_1', 
				'Allowances/Amount': row['Medical']}) 
			writer.writerow({'External ID': '',  
				'Allowances': '__export__.hr_payroll_allowance_line_2', 
				'Allowances/Amount': row['Transport']}) 
			writer.writerow({'External ID': '',  
				'Allowances': '__export__.hr_payroll_allowance_line_3', 
				'Allowances/Amount': row['Rent']}) 

			  
			
