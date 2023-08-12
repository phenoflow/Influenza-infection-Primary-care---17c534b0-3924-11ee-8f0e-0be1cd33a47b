# Chukwuma Iwundu, Clare MacRae, Eleftheria Vasileiou, 2023.

import sys, csv, re

codes = [{"code":"1143141000000112","system":"snomedct"},{"code":"2820795016","system":"snomedct"},{"code":"7267061000006115","system":"snomedct"},{"code":"2820795016","system":"snomedct"},{"code":"7267061000006115","system":"snomedct"},{"code":"XaQQp","system":"ctv3"},{"code":"XaQVd","system":"ctv3"},{"code":"XaQQp","system":"ctv3"},{"code":"XaQVd","system":"ctv3"},{"code":"4J3L.00","system":"readv2"},{"code":"65PV.00","system":"readv2"},{"code":"H2A..00","system":"readv2"},{"code":"4J3L.00","system":"readv2"},{"code":"H2A..00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('influenza-infection-primary-care-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["influenza-infection-primary-care-subtype---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["influenza-infection-primary-care-subtype---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["influenza-infection-primary-care-subtype---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)