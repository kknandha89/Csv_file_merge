import os,csv

os.chdir("C:\\Users\\Admin\\Desktop\\Pradopt\\BankFIles")

cent_to_euro = 0.000495
euro_to_dollar = 1.19
rs_to_dollar = 0.014

list_of_files = os.listdir()
list_all = []

''' CSV file - READ  '''

for i in list_of_files:

	with open(i, 'r') as source_file:

		csv_reader = csv.DictReader(source_file, delimiter=',')

		for line in csv_reader:
			dict_from_csv = dict(line).keys()
			list_of_column_names = list(dict_from_csv)

			for x in list_of_column_names:

				if 'time' in x or 'date' in x:

					try:
						if ' ' in line[x]:
							month = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
							
							splitVal = line[x].split(" ")

							for  k,v in month.items():
								if splitVal[0] == k:
									splitVal[0] = v

							if len(splitVal[1]) == 1:
								splitVal[1] = splitVal[1].zfill(2)

							full_date = splitVal[1]+ "-" + splitVal[0]+ "-" + splitVal[2]

						elif '-' in line[x]:

							splitVal = line[x].split("-")

							month = {'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}

							for k,v in month.items():
								if splitVal[1] == k:
									splitVal[1] = v

							if len(splitVal[2]) == 2:
								splitVal[2] = '20' + splitVal[2]

							full_date = splitVal[0]+ "-" + splitVal[1]+ "-" + splitVal[2]

					except:
						print("The given date format is wrong")

				elif 'type' in x or 'transaction' in x:
					type_of_cus = line[x]

				elif 'from' in x:
					from_d = line[x]

				elif 'to' in x:
					to = line[x]

				try:
					if 'amount' in x:
						amount = line[x]
						amount_in_dollars = round(float(amount) * float(rs_to_dollar),3)
						
					elif 'euro' in x:
						euro = line[x]
						cent = line['cents']
						amount_in_dollars = round(float(euro) + (float(cent) * float(cent_to_euro)),3)

				except:
 					print('Amount is in incorrect format')

			file_content = {}

			file_content['DATE'] = full_date
			file_content['TYPE'] = type_of_cus
			file_content['AMOUNT in $'] = amount_in_dollars
			file_content['FROM'] = from_d
			file_content['TO'] = to

			list_all.append(file_content)


''' CSV file - Write'''

filed_names = ['DATE','TYPE','AMOUNT in $','FROM','TO']

with open('final_file.csv','w') as target_file:

	csv_writer = csv.DictWriter(target_file, fieldnames = filed_names)
	csv_writer.writeheader()
	csv_writer.writerows(list_all)




