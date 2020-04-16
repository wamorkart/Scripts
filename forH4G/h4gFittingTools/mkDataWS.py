import ROOT
from ROOT import *
import argparse

parser = argparse.ArgumentParser(description='reduce data WS')
parser.add_argument('--min',metavar='min', type=str, help='min of window around signal mass',required=True)
parser.add_argument('--max',metavar='max', type=str, help='max of window around signal mass',required=True)
parser.add_argument('--size',metavar='size', type=str, help='percent of events in the window',required=True)


args = parser.parse_args()
min = args.min
max = args.max
size = args.size

# file = '/eos/user/t/twamorka/Oct21_Data_2016/hadd_Tree/alldata_2016.root'
# file = '/eos/user/t/twamorka/Nov11_wScalesandSmearings/Data/data_2016.root'
#file = '/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/data_2016.root'
# file = '/eos/user/t/twamorka/Ntuples_wBDTDiPhotonPairing/2016/m_60/data_2016.root'
file = '/eos/user/t/twamorka/Dec_2019/m_60/hadd/data_2016.root'
chain = ROOT.TChain('h4gCandidateDumper/trees/Data_13TeV_4photons')
chain.Add(file)

print chain.GetEntries()

# outputLoc = '/eos/user/t/twamorka/Oct21_Data_2016/WS/'
# outputLoc = '/eos/user/t/twamorka/Nov11_wScalesandSmearings/Data/'
#outputLoc = '/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/WS/'
# outputLoc = '/eos/user/t/twamorka/Ntuples_wBDTDiPhotonPairing/2016/m_60/reduceWS'
outputLoc = '/eos/user/t/twamorka/Dec_2019/m_60/hadd/'
# name_root_file_with_workspace = outputLoc + 'w_data_2016_'+str(size)+'.root'
name_root_file_with_workspace = outputLoc + 'w_data_2016_test.root'

root_file_with_workspace = ROOT.TFile (name_root_file_with_workspace, "RECREATE")
root_file_with_workspace.mkdir("tagsDumper")
root_file_with_workspace.cd("tagsDumper")

w = ROOT.RooWorkspace("cms_h4g_13TeV")
IntLumi = 1000.0
# w.factory("weight[0,10e-06]")
w.factory("dZ_zeroVtx[-100000,1000000]")
w.factory("dZ_hggVtx[-100000,1000000]")
w.factory("dZ_bdtVtx[-100000,1000000]")

w.factory("IntLumi[1000.]")
# w.factory("avg_dp_mass[0,1000]")
w.factory("tp_mass[110,180]")
w.factory("pho1_pt[0,1000]")
w.factory("pho2_pt[0,1000]")
w.factory("pho3_pt[0,1000]")
w.factory("pho4_pt[0,1000]")
w.factory("pho1_eta[-1000,1000]")
w.factory("pho2_eta[-1000,1000]")
w.factory("pho3_eta[-1000,1000]")
w.factory("pho4_eta[-1000,1000]")
w.factory("pho1_MVA[-1000,1000]")
w.factory("pho2_MVA[-1000,1000]")
w.factory("pho3_MVA[-1000,1000]")
w.factory("pho4_MVA[-1000,1000]")
w.factory("pho1_pixelseed[-1000,1000]")
w.factory("pho2_pixelseed[-1000,1000]")
w.factory("pho3_pixelseed[-1000,1000]")
w.factory("pho4_pixelseed[-1000,1000]")
w.factory("avg_dp_mass[0,1000]")
# w.factory("npho[0,1000]")

wsVars = ROOT.RooArgSet()

wsVars.add(w.var("dZ_zeroVtx"))
wsVars.add(w.var("dZ_hggVtx"))
wsVars.add(w.var("dZ_bdtVtx"))


wsVars.add(w.var("IntLumi"))
# wsVars.add(w.var("avg_dp_mass"))
wsVars.add(w.var("tp_mass"))
wsVars.add(w.var("pho1_pt"))
wsVars.add(w.var("pho2_pt"))
wsVars.add(w.var("pho3_pt"))
wsVars.add(w.var("pho4_pt"))
wsVars.add(w.var("pho1_eta"))
wsVars.add(w.var("pho2_eta"))
wsVars.add(w.var("pho3_eta"))
wsVars.add(w.var("pho4_eta"))
wsVars.add(w.var("pho1_MVA"))
wsVars.add(w.var("pho2_MVA"))
wsVars.add(w.var("pho3_MVA"))
wsVars.add(w.var("pho4_MVA"))
wsVars.add(w.var("pho1_pixelseed"))
wsVars.add(w.var("pho2_pixelseed"))
wsVars.add(w.var("pho3_pixelseed"))
wsVars.add(w.var("pho4_pixelseed"))
wsVars.add(w.var("avg_dp_mass"))
# wsVars.add(w.var("npho"))

data_RooDataSet = ROOT.RooDataSet( "Data_13TeV_fourphotons", "Data_13TeV_fourphotons", chain, wsVars )
cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 110 && tp_mass < 180'
# cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 110 && tp_mass < 180 && avg_dp_mass > '+str(min) +' && avg_dp_mass < ' + str(max)
#cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 110 && tp_mass < 180 && avg_dp_mass > 50 && avg_dp_mass < 70'
# cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 110 && tp_mass < 180 && avg_dp_mass > 50 && avg_dp_mass < 70'
data_reduced_RooDataSet = data_RooDataSet.reduce(cut)

print data_reduced_RooDataSet.numEntries()

getattr(w,'import')(data_reduced_RooDataSet,RooCmdArg())

w.Write()
