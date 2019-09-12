import ROOT
from ROOT import *
import optparse
import argparse

parser = argparse.ArgumentParser(description='make WS')

parser.add_argument('--isData', metavar='isData', type=int, help='is Data',required=True)
parser.add_argument('--mass', metavar='mass', type=str, help='mass of a',required=False)

args = parser.parse_args()

isData = args.isData


if isData=0:
   mass = args.mass 
   print "m(a) = ",mass
   file = '/eos/cms/store/user/twamorka/NTuples_17Feb2019/Signal/signal_m_' + str(mass) + '.root'
   chain = ROOT.TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+ str(mass) +'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
   chain.Add(file)
