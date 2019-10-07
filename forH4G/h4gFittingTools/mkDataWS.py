import ROOT
from ROOT import *

file = '/eos/user/t/twamorka/newCatalog_30Sep2019/hadd_tree/data_all2016.root'

chain = ROOT.TChain('h4gCandidateDumper/trees/Data_13TeV_4photons')
chain.Add(file)

print chain.GetEntries()

outputLoc = '/eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_WS/reducedWS/'

name_root_file_with_workspace = outputLoc + "w_data_2016.root"

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
w.factory("tp_mass[100,180]")
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

wsVars = ROOT.RooArgSet()
# wsVars.add(w.var("weight"))
# wsVars.add(w.var("dZ"))
wsVars.add(w.var("dZ_zeroVtx"))
wsVars.add(w.var("dZ_hggVtx"))
# wsVars.add(w.var("dZ_randomVtx"))
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

data_RooDataSet = ROOT.RooDataSet( "Data_13TeV_fourphotons", "Data_13TeV_fourphotons", chain, wsVars )

data_reduced_RooDataSet = data_RooDataSet.reduce("pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) &&  (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 100 && tp_mass < 180" )

print data_reduced_RooDataSet.numEntries()

getattr(w,'import')(data_reduced_RooDataSet,RooCmdArg())

w.Write()
