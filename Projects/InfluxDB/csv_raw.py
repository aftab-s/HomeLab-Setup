import csv

# Open CSV file in RAW mode
with open('Emission.csv', mode='r') as file:
    reader = csv.reader(file)
    # Process your data here

    # For example, let's print each row and then save it to another file
    for row in reader:
        print(row)
        # Save the row to another CSV file
        with open('Emission_raw.csv', mode='a', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(row)
