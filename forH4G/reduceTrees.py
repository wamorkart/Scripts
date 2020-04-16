import ROOT
import argparse

parser =  argparse.ArgumentParser(description='Apply Pairing BDT')
parser.add_argument('-i', '--i', dest='i', required=True, type=str)
parser.add_argument('-m', '--m', dest='m', required=True, type=str)
opt = parser.parse_args()

f1 = ROOT.TFile(opt.i+'.root')
ntuple = f1.Get('SUSYGluGluToHToAA_AToGG_M_'+opt.m+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
f2 = ROOT.TFile(opt.i+'_skim.root','recreate')
small = ntuple.CopyTree('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1  && tp_mass > 110 && tp_mass < 180')
small.Write()
