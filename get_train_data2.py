import csv

def transalte_label(filename):
    out = open('first.kddcup.data.corrected.csv', 'a', newline="")
    csv_write = csv.writer(out, dialect="excel")
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split(',')
            data = []
            data.extend(line[22:42])
            # print(data)
            csv_write.writerow(data)

if __name__ == "__main__":
    transalte_label('dos.kddcup.data.corrected.csv')