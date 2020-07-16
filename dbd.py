
def load_csv(fdir):
    f = open(fdir)
    data = []
    for line in f.readlines():
        atts = line.split(',')
        if len(atts) > 1:
            data.append(atts)
    return data


data = load_csv("dbpedia-2016-10.csv")

commands = ""
for row in data:
    print(row[0]+" of size: "+row[1])
    # command = "wget %s" % (row[2].strip())
    command = "wget %s" % (row[2])
    commands += command+""

script_name = "download-dbpedia-2016-10-wget.sh"
f = open(script_name, 'w')
f.write(commands)
f.close()
print("The generated download script is generated (%s)" % script_name)

