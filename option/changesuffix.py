import csv
inpath='/data/shibaorong/data/kidney/results/KIPR/process_list_autogen.csv'
topath='/data/shibaorong/data/kidney/results/KIPR/nosuffix_autogen.csv'

if __name__=='__main__':
    res=[]

    with open(inpath,'r') as f:
        reader=csv.reader(f)
        for index,row in enumerate(reader):
            row[0]=row[0].replace(".svs","")
            res.append(row)

    with open(topath,'w') as t:
        writer=csv.writer(t)
        for i in res:
            writer.writerow(i)
