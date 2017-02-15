import csv
import itertools

year = '2015'
inputfile = year + '.csv'

weather_st_1 = 'USW00093819'
weather_st_2 = 'USW00053842'
weather_st_3 = 'USC00124260'
weather_st_4 = 'USC00121326'
weather_st_5 = 'USC00121303'
weather_st_6 = 'USC00124286'
weather_st_7 = 'USC00124272'

opf1 = weather_st_1 + '-' + year + '.csv'
opf2 = weather_st_2 + '-' + year + '.csv'
opf3 = weather_st_3 + '-' + year + '.csv'
opf4 = weather_st_4 + '-' + year + '.csv'
opf5 = weather_st_5 + '-' + year + '.csv'
opf6 = weather_st_6 + '-' + year + '.csv'
opf7 = weather_st_7 + '-' + year + '.csv'

fieldnames = ['Date', 'Tmax', 'Tmin', 'Tavg', 'Prec', 'Snow', 'Snwd']

with open(inputfile, 'rt') as infile:
    with open(opf1, 'wt', newline='') as outfile1:
        with open(opf2, 'wt', newline='') as outfile2:
            with open(opf3, 'wt', newline='') as outfile3:
                with open(opf4, 'wt', newline='') as outfile4:
                    with open(opf5, 'wt', newline='') as outfile5:
                        with open(opf6, 'wt', newline='') as outfile6:
                            with open(opf7, 'wt', newline='') as outfile7:

                                writer1 = csv.DictWriter(outfile1, fieldnames=fieldnames)
                                writer2 = csv.DictWriter(outfile2, fieldnames=fieldnames)
                                writer3 = csv.DictWriter(outfile3, fieldnames=fieldnames)
                                writer4 = csv.DictWriter(outfile4, fieldnames=fieldnames)
                                writer5 = csv.DictWriter(outfile5, fieldnames=fieldnames)
                                writer6 = csv.DictWriter(outfile6, fieldnames=fieldnames)
                                writer7 = csv.DictWriter(outfile7, fieldnames=fieldnames)

                                writer1.writeheader()
                                writer2.writeheader()
                                writer3.writeheader()
                                writer4.writeheader()
                                writer5.writeheader()
                                writer6.writeheader()
                                writer7.writeheader()

                                def fill_values(row, weather_st, writer):
                                    date = row[1]
                                    tmin = 0
                                    tmax = 0
                                    prec = 0
                                    snow = 0
                                    snwd = 0
                                    tavg = 0
                                    while (row[0] == weather_st):
                                        if (row[2] == 'TMIN'):
                                            tmin = row[3]
                                        elif (row[2] == 'TMAX'):
                                            tmax = row[3]
                                        elif (row[2] == 'PRCP'):
                                            prec = row[3]
                                        elif (row[2] == 'SNOW'):
                                            snow = row[3]
                                        elif (row[2] == 'SNWD'):
                                            snwd = row[3]
                                        elif (row[2] == 'TAVG'):
                                            tavg = row[3]
                                        row = next(itertools.islice(csv.reader(infile), 1))
                                    writer.writerow(
                                        {'Date': date, 'Tmax': tmax, 'Tmin': tmin, 'Tavg': tavg, 'Prec': prec, 'Snow': snow,
                                         'Snwd': snwd})

                                for row in itertools.islice(csv.reader(infile), 0, None):
                                    if (row[0] == weather_st_1):
                                        fill_values(row, weather_st_1, writer1)

                                    elif (row[0] == weather_st_2):
                                        fill_values(row, weather_st_2, writer2)

                                    elif (row[0] == weather_st_3):
                                        fill_values(row, weather_st_3, writer3)

                                    elif (row[0] == weather_st_4):
                                        fill_values(row, weather_st_4, writer4)

                                    elif (row[0] == weather_st_5):
                                        fill_values(row, weather_st_5, writer5)

                                    elif (row[0] == weather_st_6):
                                        fill_values(row, weather_st_6, writer6)

                                    elif (row[0] == weather_st_7):
                                        fill_values(row, weather_st_7, writer7)