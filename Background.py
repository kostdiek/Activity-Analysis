# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 07:51:18 2016

@author: Karen
"""

def upeak(datafile='', detector=''):
    import pandas as pd
    
    filepath='C:\\Users\\Karen\\Research\\60Fe\\Activity Measurement\\Planar\\2014\\'
    filefull=filepath+datafile
    
    columns=['energy']
    energy=pd.DataFrame(columns=columns)
    backruns=pd.DataFrame()
    time=0.0
    
    firstback=filefull+'ISO'+str(detector)+'0.dat'
    energytable=pd.read_csv(firstback, delim_whitespace=True, header=None)
    energytable_data=energytable.ix[8:]
    energytable_data.rename(columns={energytable_data.columns[1]:'energy'},inplace=True)
    
    for index, row in energytable_data.iterrows():
        energy.loc[8+len(energy)]=[row['energy']]
    energy=energy.astype('float64')
    
    for i in range(12):
        filetotal=filefull+'ISO'+str(detector)+str(i)+'.dat'
        table=pd.read_csv(filetotal, delim_whitespace=True, header=None)
        table_info=table.ix[:7]
        table_data=table.ix[8:]
        table_data.rename(columns={table_data.columns[2]:'counts'}, inplace=True)
        time=time+int(table_info.iloc[1,4])
        
        for index, row in table_data.iterrows():
            backruns['ISO'+str(detector)+str(i)]=table_data['counts']
            
    backruns=backruns.astype('float64')
    
    backruns['sum']=backruns.sum(axis=1)
    
    results=pd.concat([energy, backruns],axis=1)
    
    peakcolumns=['energy', 'sum']
    upeak=pd.DataFrame(columns=peakcolumns)
    
    start=0.0
    en=0.0
    for index, row in results.iterrows():
        if row['energy']>60 and row['energy']<66:
            if row['sum']>start:
                start=row['sum']
                en=row['energy']
    
    print start
    print en
    
    total=0.0
    num=0
    for index, row in results.iterrows():
        if row['energy']>=en-1.5 and row['energy']<=en+1.5:
            num=num+1
            total=total+row['sum']
            upeak.loc[len(upeak)]=[row['energy'], row['sum']]
            
    left=0.0
    numl=0
    for index, row in results.iterrows():
        if row['energy']>=en-3.0 and row['energy']<=en-1.5:
            numl=numl+1
            left=left+row['sum']
    
    right=0.0
    numr=0

    for index, row in results.iterrows():   
        if row['energy']>=en+1.5 and row['energy']<=en+3.0:
            numr=numr+1
            right=right+row['sum']
            
    rise=upeak.iloc[len(upeak)-1,1]-upeak.iloc[0,1]
    run=upeak.iloc[len(upeak)-1,0]-upeak.iloc[0,0]
    intercept=upeak.iloc[0,1]
    
    uncorrected=0.0
    background=0.0
    for index, row in upeak.iterrows():
        uncorrected=uncorrected+row['sum']
        background=background+(rise/run)*(row['energy']-upeak.iloc[0,0])+intercept
    corrected=uncorrected-background
    
    print 'Data for ' + str(datafile)
    print 'Centroid energy is ' + str(en)    
    print "Total counts in peak is " + str(total) + ' or ' + str(uncorrected)
    print 'Counts to subtract is ' + str(background)
    print 'Background subtracted counts are : ' + str(corrected)
    print 'Max number of counts is : '+str(start)
    print "Left average is " +str(left/numl)   
    print "Right average is " +str(right/numr)
    print 'Total time is ' + str(time)
    #print results
    #print allruns['sum']
    print results.plot(x='energy',y='sum', xlim=(50,70), ylim=(0,500))
    #print energy
    #print allruns.iloc[:,74]
    return         
            