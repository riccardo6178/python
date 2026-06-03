d=dict()
with open("inifile.ini", "r+") as file:
    l=file.readlines()
    section=[]
    for line in l:
        line=line.strip()
        if len(line) <= 0:
            continue
        if line[0]== "#" or line[0]==";":
            continue
        if line=="\n":
            continue  
        if "=" in line:
            v=line.split("=")
            if section:
                d[section][v[0]]== "".join(v[1:])
            else:
                d[v[0]] = "".join(v[1:])
        if line[0]=="[" and line[-1] == "]": 
            d[line]=dict()       
            section = line[1:-1]
    
    
    file.close()

