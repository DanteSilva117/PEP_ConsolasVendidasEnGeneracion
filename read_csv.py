import csv

# CSV reading function
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = [h.strip() for h in next(reader)]
        data = []
        for row in reader:
            row = [r.strip() for r in row]
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data