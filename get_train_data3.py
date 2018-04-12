import csv

def transalte_label(filename):
    out = open('second.kddcup.data.corrected.csv', 'a', newline="")
    csv_write = csv.writer(out, dialect="excel")
    with open(filename, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            line = line.split(',')
            data = []
            data.extend(line[22:24])
            data.extend(line[31:33])
            data.append(line[28])
            data.append(line[35])
            data.append(line[37])
            data.append(line[41])
            # print(data)
            csv_write.writerow(data)

if __name__ == "__main__":
    transalte_label('dos.kddcup.data.corrected.csv')