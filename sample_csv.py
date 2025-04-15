import csv

# Read file using default CSV reader
with open("countries.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    # This will loop through CSV file line by line. Each line is array of string.
    # for line in csv_reader:
    #     print(line)

    # Create new CSV file and write data to it line by line.
    with open("countries_default_csv.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="-")

        for line in csv_reader:
            csv_writer.writerow(line)


# Read file using DictReader
with open("countries.csv", "r") as new_file:
    csv_reader = csv.DictReader(new_file, delimiter=",")

    with open("countries_default_csv.csv", "w") as new_file:
        all_fieldnames = csv_reader.fieldnames
        fieldnames = list(filter(lambda name: name == "name" or name == "country-code" or name == "alpha-2", all_fieldnames))
        print("fieldnames: ", fieldnames)

        fieldnames_to_delete = [item for item in all_fieldnames if item not in fieldnames]
        print("fieldnames_to_delete: ", fieldnames_to_delete)

        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=",")
        csv_writer.writeheader()
        for line in csv_reader:
            for fieldname in fieldnames_to_delete:
                del line[fieldname]
            csv_writer.writerow(line)