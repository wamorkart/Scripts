#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array
import operator
import math
import argparse

if __name__ == '__main__':


  parser =  argparse.ArgumentParser(description='BDT transformation')
  parser.add_argument( "-v", "--var",    dest="var", required=True, type=str, help="variable" )
  parser.add_argument( "-d", "--dir",    dest="dir",  required=True, type=str, help="input dir" )
  parser.add_argument( "-m", "--mass",    dest="mass", required=False, type=str, help="mass" )
  parser.add_argument( "-y", "--year",    dest="year", required=False, type=str, help="year" )
  parser.add_argument( "-o", "--opt",    dest="opt", required=False, type=str, help="opt" )
  parser.add_argument( "-t", "--transform",    dest="transform",  required=True, type=str, help="transformation root file" )

  opt = parser.parse_args()
  var = opt.var
  dir = opt.dir
  mass = opt.mass
  year = opt.year
  type = opt.opt
  cumulativeGraph_sig = TFile(opt.transform).Get('cumulativeGraph')

  print "Var    = ", var
  print "Mass   = ", mass
  print "Transformation Graph = ", opt.transform
  print "Type of file = ",type

  fileName_sig_trans= ''
  treename = ''
  if (type == 'sig'):
     fileName_sig_trans= dir+'signal_m_'+str(mass)+'_'+str(year)
     if (year == '2016'):
         treeName_sig_trans = 'tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0'
         treename = 'SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0'
     elif (year == '2017'):
         treeName_sig_trans = 'tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0'
         treename = 'SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0'
     else:
         treeName_sig_trans = 'tagsDumper/trees/HAHMHToAA_AToGG_MA_'+str(mass)+'GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0'
         treename = 'HAHMHToAA_AToGG_MA_'+str(mass)+'GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0'
  elif (type == 'data'):
      fileName_sig_trans= dir+'data_'+str(year)
      treeName_sig_trans = 'tagsDumper/trees/Data_13TeV_H4GTag_0'
      treename = 'Data_13TeV_H4GTag_0'
  else:
      # fileName_sig_trans= dir+'data_mix_'+str(year)
      fileName_sig_trans= dir+'data_mix_'+str(year)+'_highstat_wBDT'
      treeName_sig_trans = 'tagsDumper/trees/Data_13TeV_H4GTag_0'
      treename = 'Data_13TeV_H4GTag_0'
  print "Input tree: ",fileName_sig_trans+'.root'
  f_sig_trans = TFile(fileName_sig_trans+'.root')
  t_sig_trans = f_sig_trans.Get(treeName_sig_trans)


  # print "Signal to transform: ", dir+"signal_m_"+str(mass)+"_"+str(year)+"_transformedMVA.root"
  # f_sigTransformed = TFile.Open(dir+"signal_m_"+str(mass)+"_"+str(year)+"_transformedMVA.root","recreate")
  f_sigTransformed = TFile.Open(fileName_sig_trans+"_transformedMVA.root","recreate")
  chain_sig = TChain('tagsDumper/trees/'+str(t_sig_trans.GetName()))
  chain_sig.Add(fileName_sig_trans+'.root')
  # print chain_sig.GetEntries()
  copyTree = chain_sig.CopyTree("")
  copyTree.SetName(treename)
  copyTree.SetTitle(treename)

  # print copyTree.GetEntries()

  transfMVA = array( 'f', [ 0. ] )
  transfBranch = copyTree.Branch("bdtTransformed",transfMVA,"bdtTransformed/F");

  for i,event in enumerate(copyTree):
     if i>copyTree.GetEntries():break
     # print event.bdt
     mva = event.bdt
     # print cumulativeGraph_sig
     transfMVA[0] = cumulativeGraph_sig.Eval(mva)
     # print i, "  " , transfMVA[0]
     transfBranch.Fill()

  f_sigTransformed.Write()
  f_sigTransformed.Close()
