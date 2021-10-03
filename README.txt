HOW TO OPERATE:

0) install the datefinder library
	pip install datefinder
1) Place every csv to be mapped within the same folder as the file “Final Mapping Program.py”
2) Edit the config file named "config.json"
3) Set EXAMPLES to an integer for the number of example users
4) Set each category in DESTINATIONS to true if you would like the program to map that category of fields
5) adjust any search terms as need in the "SEARCH_TERMS" as needed to the corresponding field
6) set INPUTFILE to the singular csv file you would like to be mapped
7) Execute the file named “Final Mapping Program.py”
8) A new file will be generated named "MappedFields.csv”

METHOD DEFINITIONS

read_json()
	Parameters: file_path
		file_path is the path to the config.json file
	Operation:
		reads a json file
	Output: 
		returns the data from the json file

createDictionary()
	Parameters:
		none
	Operation: 
		Creates a dictionary with the keys: "email","gender","dob","firstName","lastName","state","city","zipcode","address","customer_status","mem_status","pkg_interval_count","dob","join_date","mem_start_date","mem_end_date","mobile_phone","total_price","payment_provider","mem_type","pkg_name","mem_id","pkg_id","plan_name","currency","item_info","title","duration","period_start","period_end","payment_paid_date","video_published_date" and assigns an empty array to each key
	Output:
		Returns a dictionary with the keys and empty arrays

findFullrow()
	Parameters: df 
		df is a data frame object
	Operation:
		the method will iterate down each column of the data frame inputed so that each value in the sample row is a non empty/NaN value 
	Output: 
		the method will output an array the length of the number of columns of the data frame with a sample value for each column and an array with a tuple for the location in the data frame of every sample data value in the other array

searchRow()
	Parameters: df, fullrow, fullrowAddy
		df is a data frame, fullrow is an array of sample data values from the dataframe, fullrowAddy is an array with tuples of the location of all of the sample data values at their corresponding index
	Operations: 
		the method iterates each sample value one location further in the data frame and updates both the sample data array and updates the location of the data in the array of the data's location
	Output:
		the method outputs an array of sample data from every columns of the dataframe and an array with tuples for the location in the data frame for the corresponding sample data at the index as the sample data 

phoneNumber()
	Parameters: item
		item is a value from the data frame
	Operations:
		the method searches in the item using a regex pattern that finds phone numbers
	Output:
		returns true or false if the search was successful or not

findName()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the term "name" and the search terms can edited in "name" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findEmail()
	Parameters: item
		item is a value from the data frame
	Operations:
		the method searches in the item using a regex pattern that finds emails
	Output:
		returns true or false if the search was successful or not

findState()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms  and the search terms can edited in "state" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findCity()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "city" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findZip()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "zip" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findAddress()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "address" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findGender(item)
	Parameters: item
		item is a value from the data frame
	Operations:
		the method searchs the item if it contains any key terms such as "male" or "female" and the search terms can edited in "gender" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findContractState()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "contractState" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findMembershipType()
	Parameters: item
		item is a value from the data frame
	Operations:
		the method searchs the item if it contains any key terms such as "month" or "year" and the search terms can edited in "interval" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findAgreement()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "agreement" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findProductName()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the term "name" or "offer" and the search terms can edited in "productName" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findMemberNumber()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the term "id" and the search terms can edited in "memberNumber" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findCurrency()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the search terms can edited in "currency" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findProductId()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the term "id", "info", or "name" and the search terms can edited in "productId" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findTitle()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms \and the search terms can edited in "title" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findDuration()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms \and the search terms can edited in "duration" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findPaymentSource()
	Parameters: item
		item is a value from the data frame
	Operations:
		the method searchs the item if it contains any key terms such as "month" or "year" and the search terms can edited in "paymentSource" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findStartDates()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the "date" and the search terms can edited in "startDates" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findEndDates()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the "date" and the search terms can edited in "endDates" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findPaidDates()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the "date" and the search terms can edited in "paidDates" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findPublishDates()
	Parameters: column
		column is the name of a column from the data frame
	Operations:
		the method searchs the column name if it contains any key terms and the column must include the "date" and the search terms can edited in "paidDates" in "SEARCH_TERMS"
	Output:
		returns true or false if the search was successful or not

findDates()
	Parameters: df, fullrow
		df is the source data frame and fullrow is a row from the data frame completed with non NaN values 
	Operations:
		this method searches each item in the fullrow with the datefinder library to search for any dates. The method then sorts all of the potetnial dates into chonological order while also creating an index array for all the dates to match to their corresponding column names. Then the method sorts the dates into chronological order.
	Output:
		returns the sorted dates array with the index array 
findDob()
	Parameters: dates, dateIndex
		dates is the sorted array of dates from findDates() and dateIndex is never used
	Operations:
		the method checks the first two dates to check if the distance is 10 years or more to verfify if the first date is the user's birthday
	Output:
		returns true or false if the search was successful or not

checkColumns()
	Paramters: df, dataDict, config
		df is the source data frame; dataDict is the dictionary mapping the array of potential matches to the mapped variables, and config is the config json file
	Operations:
		the method checks the config file variables to check which "DESTINATIONS" are true. then the method performs each check involving columns in df at each column name until each column has been checked. if the check returns true it adds it to the mapped variable list in dataDict
	Output:
		no output

checkRow()
	Parameters: df, fullrow, dataDict,config
		df is the source data frame; dataDict is the dictionary mapping the array of potential matches to the mapped variables; fullrow is a row from the data frame completed with non NaN values, and config is the config json file
	Operations:
		the method checks the config file variables to check which "DESTINATIONS" are true. then the method performs each check involving items in fullrow at each item until each item has been checked. if the check returns true it adds it to the mapped variable list in dataDict
	Output:
		no output

searchAllRows()
	Parameters:
		df is the source data frame; dataDict is the dictionary mapping the array of potential matches to the mapped variables; fullrow is a row from the data frame completed with non NaN values; fullrowAddy is an array corresponding to the index of every item in fullrow, and config is the config json file
	Operations:
		the method creates a dictionary complete that maps to each searched field in the method whether a potential match has been found. The method loops through all rows unless all the keys in the complete dictionary are true. The method starts with a searchRow() call for a new fullrow since the searches were started in the checkRow() method. The method then checks the "DESTINATIONS" section in the config file. If true, the method checks at each item and appends the column name to the corresponding key in dataDict and changes its corresponding key in complete to true. The method returns once all of complete is true.
	Output:
		no output

arraytoString()
	Parameters: array
		the array that is to be formatted
	Operations:
		the method takes an array and beautifies it to print in the output without the brackets, quotes, or commas
	Output:
		A beautified string of the input array

builddf()
	Parameters: none
		none 
	Operations:
		the method loads the config file. the method loads the "INPUTFILE" as a data frame. the method creates the dictionary to map the field names. the method calls checkColumns(), checkRow(), searchAllRows() to map the fields. output is created as a data frame. for every key in dictionary a row is created showing the mapped field names and example data values as potential users based on the number of examples specifed in "EXAMPLES" 
	Output:
		the output is the final data frame

the main functions writes the output of builddf() to the csv file "MappedFields.csv"