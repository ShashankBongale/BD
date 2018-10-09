import yaml
import csv
import glob


yaml_file_names = glob.glob('./*.yaml')

csvdata = []
#l = ['Batsman','Bowler','Runs']
#csvdata.append(l)

for idx, each_yaml_file in enumerate(yaml_file_names):
    print("Processing file ", idx+1, "of", len(yaml_file_names), "file name:", each_yaml_file)
    with open(each_yaml_file) as f:
        data = yaml.load(f)

        for main_loop in data['innings']:
            for main in main_loop:
                inning = main_loop[main]
                for first_loop in inning['deliveries']:
                    for key in first_loop:
                        level = first_loop[key]
                        batsman = level['batsman']
                        bowler = level['bowler']
                        comb = batsman + "&" + bowler
                        new_comb = ""
                        b = comb.split(" ")
                        for i in b:
                            new_comb=new_comb+"_"+i
                        runs = level['runs']
                        total_runs = runs['total']
                        if (total_runs!=0):
                            l = [new_comb,total_runs]
                            csvdata.append(l)


with open('IPL_runs.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvdata)

csvfile.close()
