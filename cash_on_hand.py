def coh_function():
    from pathlib import Path
    import csv

    # create a file path to csv file.
    fp = Path('C:\project_group\csv_report\Cash_on_Hand.csv')

    # read the csv file.
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader) # skip header

        # create an empty list for cash on hand
        CoH=[] 

        # append cash on hand into the CoH list
        for row in reader:
            CoH.append([row[0],row[1]])   

    diff_dict={}
    previous = 0  
    for day in CoH:
        """
        finds the difference in cash on hand per day
        """
        # convert cash on hand to variable cash
        Cash = int(day[1])
        # find the difference between the day and the day before
        Difference = Cash - previous
        # set previous value for the next day
        previous = Cash
        #add the difference to the dictionary with the key as the day
        dayNo=str(day[0])
        diff_dict[dayNo] = Difference

    #now, find out whether the data in diff_dict is always increasing, decreasing, or fluctuating
    Differences = diff_dict.values()
    final_dict={}
    # always increasing
    if all(diff > 0 for diff in Differences):
        file_path = Path(r'C:\project_group\summary_report.txt')
        with file_path.open(mode='a', encoding='UTF-8') as file:
            file.write(f'\n[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS')
            
            #sort the dictionary in ascending order so that the biggest gain is last
            sorted_dict = dict(sorted(final_dict.items(), key=lambda item: item[1]))
            #split the dictionary into two lists so that they can easily be referred to
            key_list=list(sorted_dict.keys())
            value_list=list(sorted_dict.values())
            # -1 index is used to take the last value in the list
            file.write(f'''
[HIGHEST CASH SURPLUS] DAY:{key_list[-1]} AMOUNT: SGD{-value_list[-1]}
''')
    # always decreasing
    elif all(diff < 0 for diff in Differences):
        file_path = Path(r'C:\project_group\summary_report.txt')
        with file_path.open(mode='a', encoding='UTF-8') as file:
            file.write(f'\n[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS')
            
            #sort the dictionary in ascending order so that the biggest loss is first
            sorted_dict = dict(sorted(final_dict.items(), key=lambda item: item[1]))
            #split the dictionary into two lists so that they can easily be referred to
            key_list=list(sorted_dict.keys())
            value_list=list(sorted_dict.values())
            # 0 index is used to take the first value in the list
            file.write(f'''
[HIGHEST CASH DEFICIT] DAY:{key_list[0]} AMOUNT: SGD{-value_list[0]}
''')
    # fluctuate
    else:
        for day in diff_dict:
            dayNo1=str(day)
            #sort all the days with loss into a final dictionary 
            if diff_dict[day] < 0:
                final_dict[dayNo1]=diff_dict[day]
        file_path = Path(r'C:\project_group\summary_report.txt')
        with file_path.open(mode='a', encoding='UTF-8') as file:
        # this loops through the dictionary and writes a statement for every day with a cash deficit
        # negative sign before the deficit amount gives its absolute value for formatting purposes
            for day, cash_on_hand in final_dict.items():
                file.write(f'\n[CASH DEFICIT] DAY:{day} AMOUNT: SGD{-cash_on_hand}')
            
            #sort the dictionary in ascending order so that the biggest loss is first
            sorted_dict = dict(sorted(final_dict.items(), key=lambda item: item[1]))
            #split the dictionary into two lists so that they can easily be referred to
            key_list=list(sorted_dict.keys())
            value_list=list(sorted_dict.values())
            # writes the top 3 highest deficits, if there are less than 3 days with deficit, only write out those days in order
            for value in range(len(key_list)):
                if value == 0:
                    file.write(f'\n[HIGHEST CASH DEFICIT] DAY:{key_list[value]} AMOUNT: SGD{-value_list[value]}')
                if value == 1:
                    file.write(f'\n[2nd HIGHEST CASH DEFICIT] DAY:{key_list[value]} AMOUNT: SGD{-value_list[value]}')
                if value == 2: 
                    file.write(f'\n[3rd HIGHEST CASH DEFICIT] DAY:{key_list[value]} AMOUNT: SGD{-value_list[value]}')
                    break