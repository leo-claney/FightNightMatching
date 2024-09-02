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
    print(groups)

    with open('Fight Night Rankings - Test Auditionee Rankings.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        columns = reader.fieldnames
        rows = list(reader)
        auditionees = {x: [] for x in columns}
        for column in columns:
            for row in rows:
                if row[column] != '':
                    auditionees[column].append(row[column])
    print(auditionees)
            
test_csv()