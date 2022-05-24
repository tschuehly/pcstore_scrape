import csv
import re

if __name__ == '__main__':
    adresse = []
    with open('adressen.csv', newline='', encoding='utf-8') as csvfile:
        spamreader = csv.DictReader(csvfile, dialect='excel')
        for row in spamreader:
            print(row)
            dict = {}
            dict["webseite"] = row["webseite"]
            dict["email"] = row["email"]
            dict["name"] = row["name"]
            dict["telefonnummer"] = row["telefonnummer"]
            adr = re.split("([0-9]{5})", row["adresse"])
            dict["straße"] = adr[0].strip()
            dict["plz"] = adr[1].strip()
            dict["ort"] = adr[2].strip()
            adresse.append(dict)
    print(adresse)

    with open('adressen_geteilt.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['webseite', 'straße', 'plz', 'ort', 'email', 'name', 'telefonnummer']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in adresse:
            writer.writerow(item)