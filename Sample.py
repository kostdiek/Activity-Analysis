# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 09:43:59 2016

@author: Karen
"""

def sample(date='', detector=''):
    import pandas as pd
    
    #date='Apr22\\'
    filepath='C:\\Users\\Karen\\Research\\60Fe\\Activity Measurement\\Planar\\2014\\'
    filefull=filepath+date
    
    columns=['energy']
    energy=pd.DataFrame(columns=columns) 
    allruns=pd.DataFrame()
    time=0.0
    
    
    firstfileA=filefull+'ISO'+str(detector)+'0.dat'
    energytableA=pd.read_csv(firstfileA, delim_whitespace=True, header=None)
    energytableA_data=energytableA.ix[8:]
    energytableA_data.rename(columns={energytableA_data.columns[1]:'energy'}, inplace=True)
    for index, row in energytableA_data.iterrows():
        energy.loc[8+len(energy)]=[row['energy']]
    energy=energy.astype('float64')
    
    for i in range(72):
        filetotal=filefull+'ISO'+str(detector)+str(i)+'.dat'
        table=pd.read_csv(filetotal, delim_whitespace=True, header=None)
        table_info=table.ix[:7]
        table_data=table.ix[8:]
        #table_data.rename(columns={table_data.columns[1]:'energy'}, inplace=True)
        table_data.rename(columns={table_data.columns[2]:'counts'}, inplace=True)
        time=time+int(table_info.iloc[1,4])
        #print time
        
        for index, row in table_data.iterrows():
            allruns['ISO'+str(detector)+str(i)]=table_data['counts']
    
    allruns=allruns.astype('float64')
    #for index, row in allruns.iterrows():
        #allruns.loc[len(allruns)]=allruns.sum(axis=0)
    
    allruns['sum']=allruns.sum(axis=1)     
    #allruns.to_csv(filepath+'allruns.dat')    
        
        
        #for row in table_data['counts']:
            #counts.append(table_data['counts'])
            #print counts  
        #allruns['ISOA'+str(i)]=counts
        #print allruns
    results=pd.concat([energy,allruns],axis=1)
    
        
    peakcolumns=['energy', 'sum']
    fepeak=pd.DataFrame(columns=peakcolumns)
    
    start=0.0
    en=0.0
    for index, row in results.iterrows():
        if row['energy']>55 and row['energy']<61:
            if row['sum']>start:
                start=row['sum']
                en=row['energy']
                
    #print start
    #print en
    total=0.0
    num=0
    
    for index, row in results.iterrows():
        if row['energy']>=en-1.5 and row['energy']<=en+1.5:
            num=num+1
            total=total+row['sum']
            fepeak.loc[len(fepeak)]=[row['energy'], row['sum']]
            
    left=0.0
    numl=0
    
    for index, row in results.iterrows():
        if row['energy']>=en-3.0 and row['energy']<=en-1.5:
            numl=numl+1
            left=left+row['sum']
    
    #print left
    #print numl   

    right=0.0
    numr=0

    for index, row in results.iterrows():   
        if row['energy']>=en+1.5 and row['energy']<=en+3.0:
            numr=numr+1
            right=right+row['sum']
            
    
    #print right
    #print numr
          
    rise=fepeak.iloc[len(fepeak)-1,1]-fepeak.iloc[0,1]
    run=fepeak.iloc[len(fepeak)-1,0]-fepeak.iloc[0,0]
    intercept=fepeak.iloc[0,1]
    
    uncorrected=0.0
    background=0.0
    
    for index, row in fepeak.iterrows():
        uncorrected=uncorrected+row['sum']
        background=background+(rise/run)*(row['energy']-fepeak.iloc[0,0])+intercept
        
    corrected=uncorrected-background
    
    print 'Data for ' + str(date)
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
    print results.plot(x='energy',y='sum', xlim=(50,70), ylim=(0,2000))
    #print energy
    #print allruns.iloc[:,74]
    return 
