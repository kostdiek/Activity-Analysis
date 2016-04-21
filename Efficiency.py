# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:17:46 2016

@author: Karen
"""

def effAM(datafile=''):
    import pandas as pd

    filepath='C:\\Users\\Karen\\Research\\60Fe\\Activity Measurement\\Planar\\2014\\'
    #datafile='Apr16\\AMAWAY.dat'
    filefull=filepath+datafile
    table=pd.read_csv(filefull, delim_whitespace=True, header=None)
    table_info=table.ix[:7]
    table_data=table.ix[8:]
    table_data.rename(columns={table_data.columns[0]:'channel'}, inplace=True)
    table_data.rename(columns={table_data.columns[1]:'energy'}, inplace=True)
    table_data.rename(columns={table_data.columns[2]:'counts'}, inplace=True)
    table_data.rename(columns={table_data.columns[3]:'error'}, inplace=True)
    table_data=table_data.astype(float)

    columns=['energy', 'counts']    
    peakonly=pd.DataFrame(columns=columns)    
    
    start=0.0
    en=0.0  
    for index, row in table_data.iterrows():
        if row['energy']>50 and row['energy']<70:
            if row['counts']>start:
                start=row['counts']
                en=row['energy']
                
    
    total=0.0
    num=0

    for index, row in table_data.iterrows():
        if row['energy']>=en-1.5 and row['energy']<=en+1.5:
            num=num+1
            total=total+row['counts']
            peakonly.loc[len(peakonly)]=[row['energy'], row['counts']]
            
    
    left=0.0
    numl=0
    for index, row in table_data.iterrows():
        if row['energy']>=en-3.0 and row['energy']<=en-1.5:
            numl=numl+1
            left=left+row['counts']

    
    right=0.0
    numr=0
    for index, row in table_data.iterrows():
        if row['energy']>=en+1.5 and row['energy']<=en+3.0:
            numr=numr+1
            right=right+row['counts']
        
    rise=peakonly.iloc[len(peakonly)-1,1]-peakonly.iloc[0,1]
    run=peakonly.iloc[len(peakonly)-1,0]-peakonly.iloc[0,0]
    intercept=peakonly.iloc[0,1]
    
    uncorrected=0.0
    background=0.0
    
    for index, row in peakonly.iterrows():
        uncorrected=uncorrected+row['counts']
        background=background+(rise/run)*(row['energy']-peakonly.iloc[0,0])+intercept
       
    corrected=uncorrected-background    
    

       
     
        
    #print uncorrected    
    #print background  
    
    print 'Data file is : ' + datafile
    print "Centroid energy is " + str(en)
    print "Total counts in peak is " + str(total) 
    print 'Counts to subtract is ' + str(background)
    print 'Background subtracted counts are : ' + str(corrected)
    print 'Max number of counts is : ' +str(start)
    print "Left average is " +str(left/numl)   
    print "Right average is " +str(right/numr)
    
    print 'Total live time is ' + str(table_info.iloc[1,4])
    #print y
    #print peakonly.loc[0]
    #print peakonly.loc[len(peakonly)-1]
    #print rise/run
    #print intercept
    #print peakonly.loc[0]
    #print peakonly.loc[len(peakonly)-1]
    #print peakonly.iloc[0,0]
    #print peakonly.iloc[len(peakonly)-1, 0]    
    #print "Centroid energy is " + str(en)
    #print "Total counts in peak is " + str(total)    
    
    
    
     
    return
#print filename
#print table
#print table_info
#print table_data
#print table_data.head(5)
#print "Centroid energy is " +str(en)
#print "Total counts in peak is " +str(total)
#print "Left average is " + str(left/numl)
#print "Right average is " + str(right/numr)
