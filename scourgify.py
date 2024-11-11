import sys
import csv


if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif sys.argv[1].endswith(".csv"):
    name_house = []
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            entry = []
            for line in reader:
                name = line['name'].split(",")
                name.reverse()
                name[0] = name[0].strip()
                name_house.append({"first" : name[0], "last": name[1], "house": line["house"]})
            with open(f"{sys.argv[2]}" , "w+") as file:
                writer = csv.DictWriter(file, fieldnames=["first" , "last", "house"])
                writer.writeheader()
                for line in name_house:
                    writer.writerow(line)

        print(name_house)


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


#spit the first and last name
#store the first name, last name, and house all in there own dictionaries
#print those values into a after.csv
