import csv
def test_csv():
    with open('Fight Night Rankings - Test Group Rankings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        rows = list(reader)
        groups = {x: [] for x in columns}
        for column in columns:
            for row in rows:
                if row[column] != '':
                    groups[column].append(row[column])
        for key, value in groups.items():
            groupMax = value[0]
            groupRanks = value[1:]
            groups[key] = (groupMax, groupRanks)
            # groups[key] = value[1:]
            # print(key, value)
            print(key, groups[key][0], groups[key][1])
    # print(groups)

    with open('Fight Night Rankings - Test Auditionee Rankings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        rows = list(reader)
        auditionees = {x: [] for x in columns}
        for column in columns:
            for row in rows:
                if row[column] != '':
                    auditionees[column].append(row[column])
    # print(auditionees)
            
test_csv()