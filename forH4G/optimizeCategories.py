#!/usr/bin/python
import numpy as n
import ROOT 
import sys, getopt
from array import array
from optparse import OptionParser
import operator
import math  

def reduceTree(inTree, cut):
  small = inTree.CopyTree(str(cut))
  return small

def computeSignificance(s,b,m,d):
  significance = ((2*(s+b)*math.log(1+(s/b))) - 2*s) 
  if significance>0. and m>=8. and d>=8. and b>0.: return math.sqrt(significance)
  else: return -999.  

def sumSignificance(partition, h_sig_SR, h_bkg_SR, h_bkg_SB, h_data_SB):
  sum = 0.
  for pair in partition:
    s = h_sig_SR.Integral(pair[0],pair[1])   
    b = h_bkg_SR.Integral(pair[0],pair[1])
    m = h_bkg_SB.Integral(pair[0],pair[1])
    d = h_data_SB.Integral(pair[0],pair[1])
    significance = computeSignificance(s,b,m,d)
    #print h_sig_SR.GetBinCenter(pair[0])-h_bdt_signal_SR.GetBinWidth(pair[0])/2.,significance 
    if significance>0.: sum += significance*significance   
    else: return -999.  
  return math.sqrt(sum)

if __name__ == '__main__':

  ROOT.gROOT.SetBatch(ROOT.kTRUE)

  parser = OptionParser()
  parser.add_option( "-d", "--inDir",    dest="inDir",    default="",   type="string", help="inDir" )
  parser.add_option( "-n", "--nBins",    dest="nBins",    default=190,  type="int",    help="nBins" )
  parser.add_option( "-c", "--nCats",    dest="nCats",    default=5,    type="int",    help="nCats" )
  parser.add_option( "-o", "--outFileName",  dest="outFileName",  default="",   type="string", help="output text file")
  (options, args) = parser.parse_args()  

  nBins = options.nBins
  inDir = options.inDir
  nCats = options.nCats
  outFileName = options.outFileName
  
  #inDir = /eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_9Dec2020/dataset_PhoMVA_manyKinVars_fullRun2_datamix_old_kinWeight_dataSBScaling_m60/

  #print "inDir:",inDir
  #print "nBins:",nBins
  #print "nCats:",nCats

  inFile = ROOT.TFile(inDir+"/BDT_Histos_smoothing_SmoothSuper_bins"+str(nBins)+".root","READ")
  outFile = open(outFileName+".txt","w+") 

  h_bdt_signal_SR = inFile.Get("h_bdt_signal_SR")
  h_bdt_datamix_SR_weighted = inFile.Get("h_bdt_datamix_SR_weighted")
  h_bdt_datamix_SR_weighted_smooth = inFile.Get("h_bdt_datamix_SR_weighted_smooth")
  h_bdt_datamix_SB_weighted = inFile.Get("h_bdt_datamix_SB_weighted")
  h_bdt_datamix_SB_weighted_smooth = inFile.Get("h_bdt_datamix_SB_weighted_smooth")
  h_bdt_data_SB = inFile.Get("h_bdt_data_SB")
  h_bdt_data_SB_smooth = inFile.Get("h_bdt_data_SB_smooth") 
 
  significance_final = -999.
  partition_final = []
  
  #2 categories
  if nCats == 2:

   for i in range(1,nBins+1):
    for j in range(i+1,nBins+1): 
     partition = [[1,i],[j,nBins]]  
     if abs(i-j)==1: 
       #print partition 
       significance = sumSignificance(partition, h_bdt_signal_SR, h_bdt_datamix_SR_weighted_smooth, h_bdt_datamix_SB_weighted_smooth, h_bdt_data_SB_smooth)
       if significance>significance_final:
         significance_final = significance
         partition_final = partition 
   
   #print "Best categories: ",h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2,h_bdt_signal_SR.GetBinCenter(partition_final[1][0])-h_bdt_signal_SR.GetBinWidth(partition_final[1][0])/2,"1. --->",significance_final    
   #outFile.write( str(h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2) )
   #outFile.close()
  #3 categories
  elif nCats == 3:

   for i in range(1,nBins+1):
    for j in range(i+1,nBins+1): 
     for k in range(j+1,nBins+1):  
      partition = [[1,i],[j,k-1],[k,nBins]] 
      if abs(i-j)==1: 
        #print partition 
        significance = sumSignificance(partition, h_bdt_signal_SR, h_bdt_datamix_SR_weighted_smooth, h_bdt_datamix_SB_weighted_smooth, h_bdt_data_SB_smooth)
        if significance>significance_final:
          significance_final = significance
          partition_final = partition   
   
   #print "Best categories: ",h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[1][0])-h_bdt_signal_SR.GetBinWidth(partition_final[1][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[2][0])-h_bdt_signal_SR.GetBinWidth(partition_final[2][0])/2, "1. --->",significance_final  
   
  #4 categories
  elif nCats == 4:

   for i in range(1,nBins+1):
    for j in range(i+1,nBins+1): 
     for k in range(j+1,nBins+1):  
      for d in range(k+1,nBins+1):  
       partition = [[1,i],[j,k-1],[k,d-1],[d,nBins]]   
       if abs(i-j)==1: 
         #print partition 
         significance = sumSignificance(partition, h_bdt_signal_SR, h_bdt_datamix_SR_weighted_smooth, h_bdt_datamix_SB_weighted_smooth, h_bdt_data_SB_smooth)
         if significance>significance_final:
           significance_final = significance
           partition_final = partition   
 
   #print "Best categories: ",h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[1][0])-h_bdt_signal_SR.GetBinWidth(partition_final[1][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[2][0])-h_bdt_signal_SR.GetBinWidth(partition_final[2][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[3][0])-h_bdt_signal_SR.GetBinWidth(partition_final[3][0])/2, "1. --->",significance_final  
  
  #5 categories
  elif nCats == 5:
   for i in range(1,nBins+1):
    for j in range(i+1,nBins+1): 
     for k in range(j+1,nBins+1):  
      for d in range(k+1,nBins+1):  
       for f in range(d+1,nBins+1):  
        partition = [[1,i],[j,k-1],[k,d-1],[d,f-1],[f,nBins]]    
        if abs(i-j)==1: 
          #print partition 
          significance = sumSignificance(partition, h_bdt_signal_SR, h_bdt_datamix_SR_weighted_smooth, h_bdt_datamix_SB_weighted_smooth, h_bdt_data_SB_smooth)
          if significance>significance_final:
            significance_final = significance
            partition_final = partition 

   #print "Best categories: ",h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[1][0])-h_bdt_signal_SR.GetBinWidth(partition_final[1][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[2][0])-h_bdt_signal_SR.GetBinWidth(partition_final[2][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[3][0])-h_bdt_signal_SR.GetBinWidth(partition_final[3][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[4][0])-h_bdt_signal_SR.GetBinWidth(partition_final[4][0])/2, "1. --->",significance_final     
   #outFile.write(h_bdt_signal_SR.GetBinCenter(partition_final[0][0])-h_bdt_signal_SR.GetBinWidth(partition_final[0][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[1][0])-h_bdt_signal_SR.GetBinWidth(partition_final[1][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[2][0])-h_bdt_signal_SR.GetBinWidth(partition_final[2][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[3][0])-h_bdt_signal_SR.GetBinWidth(partition_final[3][0])/2, h_bdt_signal_SR.GetBinCenter(partition_final[4][0])-h_bdt_signal_SR.GetBinWidth(partition_final[4][0])/2)
  else: 
   #print "Number of categories not supported, choose: 2, 3, 4 or 5!"
   sys.exit()
  
  #final details
  #print "Final details:"
  for pair in partition_final:
    s = h_bdt_signal_SR.Integral(pair[0],pair[1])   
    b = h_bdt_datamix_SR_weighted_smooth.Integral(pair[0],pair[1])
    m = h_bdt_datamix_SB_weighted_smooth.Integral(pair[0],pair[1])
    d = h_bdt_data_SB_smooth.Integral(pair[0],pair[1])
    significance = computeSignificance(s,b,m,d)
    #print h_bdt_signal_SR.GetBinCenter(pair[0])-h_bdt_signal_SR.GetBinWidth(pair[0])/2., h_bdt_signal_SR.GetBinCenter(pair[1])+h_bdt_signal_SR.GetBinWidth(pair[1])/2., " --> Significance:", significance, " - N Sig:", s, "N DataMix_SR:", b, "N DataMix_SB:", m, "N Data_SB:", d
    outFile.write(str(h_bdt_signal_SR.GetBinCenter(pair[0])-h_bdt_signal_SR.GetBinWidth(pair[0])/2.))
    outFile.write("  ")
    outFile.write(str(h_bdt_signal_SR.GetBinCenter(pair[1])+h_bdt_signal_SR.GetBinWidth(pair[1])/2.))
    outFile.write("  Significance: %s"%(str(significance)) )
    outFile.write(" NSig: %s"%(s))
    outFile.write(" NDataMix_SR: %s"%(b))
    outFile.write(" NDataMix_SB: %s"%(m))
    outFile.write(" NData_SB: %s"%(d))
    outFile.write("\n")
  outFile.write("\n")
  outFile.write("Tot_Significance: %s"%(significance_final))
  outFile.close()
