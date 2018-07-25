
#encoding:utf-8
import xlrd
def hebing(sheet, outputfile, xlsx1, xlsx2):
    xlsx1 = xlrd.open_workbook(xlsx1)
    xlsx2 = xlrd.open_workbook(xlsx2)

    table1 = xlsx1.sheets()[int(sheet)]
    table2 = xlsx2.sheets()[int(sheet)]

    nrows1 = table1.nrows
    nrows2 = table2.nrows

    dic1 = {}
    for i in range(nrows1):
        if table1.row_values(i)[0] != '':
            dic1[table1.row_values(i)[0]] = table1.row_values(i)[1]
    dic2 = {}
    for i in range(1,nrows2):
        if table2.row_values(i)[0] != '':
            dic2[table2.row_values(i)[0]] = table2.row_values(i)[1]

    allkeys = set(dic1.keys())|set(dic2.keys())
    print (allkeys)
    f = open(outputfile,'a')
    for i in allkeys:
        
        f.write("%s,%s,%s\n" % (i, table1.row_values(i), table2.row_values(i)))

hebing(0, 'result.xlsx', 'test.xlsx', 'test1.xlsx')