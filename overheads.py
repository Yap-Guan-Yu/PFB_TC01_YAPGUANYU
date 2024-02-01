def overhead_function(): 
    from pathlib import Path
    import csv
# create a file path to the CSV file
    fp = Path('C:\project_group\csv_report\Overheads.csv')


# read the CSV file
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip header

        # create an empty dictionary for OH
        OH = {}

        # append overheads into the OH dictionary
        for row in reader:
            # get the category of expense and value from the file
            # and add to the OH dictionary
            if len(row) >= 2:
                key = row[0] 
                value = row[1]  
                OH[key] = value

    #sort it in ascending order so the highest overhead is last in the dictionary
    sorted_dict = dict(sorted(OH.items(), key=lambda item: item[1]))
    #split the dictionary into two lists so that they can easily be referred to
    key_list=list(sorted_dict.keys())
    value_list=list(sorted_dict.values())
    file_path = Path(r'C:\project_group\summary_report.txt')
    with file_path.open(mode='a', encoding='UTF-8') as file:
        file.write(f'[HIGHEST OVERHEAD]: {key_list[-1]}: {value_list[-1]}% ')

