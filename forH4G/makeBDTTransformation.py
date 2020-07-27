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
  parser.add_argument( "-d", "--dir",    dest="dir",  required=True, type=str, help="variable" )
  parser.add_argument( "-m", "--mass",    dest="mass", required=False, type=str, help="variable" )
  parser.add_argument( "-t", "--transform",    dest="transform",  required=True, type=str, help="variable" )

  opt = parser.parse_args()
  var = opt.var
  dir = opt.dir
  mass = opt.mass
  cumulativeGraph_sig = TFile(opt.transform).Get('cumulativeGraph_sig')

  print "Var    = ", var
  print "Mass   = ", mass


  fileName_sig_trans= dir+'signal_m_'+str(mass)+'.root'
  treeName_sig_trans = 'SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0'
  f_sig_trans = TFile(fileName_sig_trans)
  t_sig_trans = f_sig_trans.Get(treeName_sig_trans)

  # xmin = -1.
  # xmax = 1.
  # # precision = 0.000001
  # precision = 0.00001

  # selection = "(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && pho1_MVA > -999. && pho2_MVA > -999. && pho3_MVA > -999. && pho4_MVA > -999)"
  # selection = "(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && (tp_mass > 110 && tp_mass < 180) && pho1_MVA>-0.9 && pho2_MVA>-0.9 && pho3_MVA>-0.9 && pho4_MVA>-0.9)"
  # selection = "(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && (tp_mass > 110 && tp_mass < 180))"


  print "Signal to transform: ", dir+"signal_m_"+str(mass)+"_transformedMVA_finerBinning_27jul2020.root"
  f_sigTransformed = TFile.Open(dir+"signal_m_"+str(mass)+"_transformedMVA_finerBinning_27jul2020.root","recreate")
  chain_sig = TChain(t_sig_trans.GetName())
  chain_sig.Add(fileName_sig_trans)
  copyTree = chain_sig.CopyTree("")
  copyTree.SetName(treeName_sig_trans)
  copyTree.SetTitle(treeName_sig_trans)

  transfMVA = array( 'f', [ 0. ] )
  transfBranch = copyTree.Branch("bdtTransformed",transfMVA,"bdtTransformed/F");

  for i,event in enumerate(copyTree):
     if i>copyTree.GetEntries():break

     mva = event.bdt
     transfMVA[0] = cumulativeGraph_sig.Eval(mva)
     print i, "  " , transfMVA[0]
     transfBranch.Fill()

  f_sigTransformed.Write()
  f_sigTransformed.Close()

  # f_sigTransformed = TFile(dir+'signal_m_'+str(mass)+'_transformedMVA_differentselection_27jul2020.root')
  # t_sigTransformed = f_sigTransformed.Get(treeName_sig_trans)
  # histoMVAtrans_sig = TH1F("histoMVAtrans_sig","histoMVAtrans_sig",100,0.,xmax)
  # histoMVAtrans_sig.Sumw2()
  # t_sigTransformed.Draw("bdtTransformed >> histoMVAtrans_sig","weight*36*"+selection,"goff")
  #
  # print "Total signal integral: ", histoMVAtrans_sig.Integral()
