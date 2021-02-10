import os
import csv

data_root='/data/shibaorong/data/kidney/results'
topath='../dataset_csv/tcga_kidney.csv'

if __name__=='__main__':
    line=[['','case_id','slide_id','label']]
    count=0
    for dirpath,dirname,filename in os.walk(data_root):
        if dirpath.split('/')[-1]=='patches':
            label='TCGA-'+dirpath.split('/')[-2]
            for f in filename:
                if f.endswith('h5'):
                    case_id=f[:12]
                    slide_id=f.replace('.h5','')
                record=[str(count),case_id,slide_id,label]
                line.append(record)
                print(count)
                count+=1

    with open(topath,'w') as t:
        writer=csv.writer(t)
        for i in line:
            writer.writerow(i)
