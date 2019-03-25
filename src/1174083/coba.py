import pandas

df = pandas.read_csv('1174083.csv', 
            index_col='npm', 
            parse_dates=['namalengkap'],
            header=0, 
            names=['npm', 'namalengkap', 'kelas'])
    df.to_csv('1174083_edit.csv')
    print(df)