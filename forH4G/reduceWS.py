import ROOT
from ROOT import *
import argparse

parser = argparse.ArgumentParser(description='reduce signal WS')
parser.add_argument('--min',metavar='min', type=str, help='min of window around signal mass',required=True)
parser.add_argument('--max',metavar='max', type=str, help='max of window around signal mass',required=True)
parser.add_argument('--size',metavar='size', type=str, help='percent of events in the window',required=True)


args = parser.parse_args()
min = args.min
max = args.max
size = args.size

#mass = [15,20,25,30,35,40,45,50,55,60]
mass = [60]
# cut = ['avg_dp_mass > 14.7 && avg_dp_mass < 15.25 ','avg_dp_mass > 19.6 && avg_dp_mass < 20.3 ','avg_dp_mass > 24.45 && avg_dp_mass < 25.3 ','avg_dp_mass > 29.35 && avg_dp_mass < 30.4 ','avg_dp_mass > 34.2 && avg_dp_mass < 35.4 ','avg_dp_mass > 39.35 && avg_dp_mass < 40.65 ','avg_dp_mass > 44.2 && avg_dp_mass < 45.7 ','avg_dp_mass > 49.15 && avg_dp_mass < 50.8','avg_dp_mass > 54 && avg_dp_mass < 55.75 ','avg_dp_mass > 58.8 && avg_dp_mass < 60.85 ']
for mi, m  in enumerate(mass):
    print "Looking at mass = ", m
    # # inFile = '/eos/user/t/twamorka/Signal_Oct28_Lumi_1e3/hadd_Tree/signal_m_'+str(m)+'.root'
    # inFile = '/eos/user/t/twamorka/H4G_2016_wScalesnSmearings/Signal/Trees/signal_m_'+str(m)+'.root'
    # # print "input file", inFile
    # #inFile = '/afs/cern.ch/work/t/twamorka/ThesisAnalysis/CMSSW_10_5_0/src/flashgg/output.root'
    # chain = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(m)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
    # # chain = TChain('h4gCandidateDumper/trees/_13TeV_4photons')
    # chain.Add(inFile)
    # print chain.GetEntries()
    # h = ROOT.TH1F("hist","Avg, Diphoton mass;Mass[GeV];# of events",100, 0, 500)
    # chain.Draw('avg_dp_mass >> hist','pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 100 && tp_mass < 180')

    # fitResultPtr = h.Fit("gaus","S")
    # mean = fitResultPtr.GetParams()[1]
    # sigma = fitResultPtr.GetParams()[2]

    # print "mean =",mean, " ", "mean + 2sigma =", mean + 2*sigma, " ", "mean - 2sigma =", mean - 2*sigma
    # print '/eos/user/t/twamorka/HtoAAto4Gamma_2019/2016Analysis/forCombine/17Sep2019/Signal/'+str(m)+'/output_SUSYGluGluToHToAA_AToGG_M-'+str(m)+'_TuneCUETP8M1_13TeV_pythia8.root'
    #inFileWS = '/afs/cern.ch/work/t/twamorka/ThesisAnalysis/CMSSW_10_5_0/src/flashgg/output.root'
    # inFileWS = '/eos/user/t/twamorka/Oct22_Signal_2016/'+str(m)+'/output_SUSYGluGluToHToAA_AToGG_M-'+str(m)+'_TuneCUETP8M1_13TeV_pythia8.root '
    # inFileWS = '/eos/user/t/twamorka/Signal_Oct28_Lumi_1e3/hadd_WS/signal_m_'+str(m)+'_WS.root'
    #inFileWS = '/eos/user/t/twamorka/Nov11_wScalesandSmearings/Signal/signal_m_'+str(m)+'_ws.root'
    # inFileWS = '/eos/user/t/twamorka/Ntuples_wBDTDiPhotonPairing/2016/m_60/signal_m_60_ws.root'
    inFileWS = '/eos/user/t/twamorka/Dec_2019/m_60/hadd/signal_m_60_ws.root'
    print inFileWS
    # inFileWS = '/eos/user/t/twamorka/19Signal2019/Signal/'+str(m)+'/output_SUSYGluGluToHToAA_AToGG_M-'+str(m)+'_TuneCUETP8M1_13TeV_pythia8.root '
    # inFileWS = '/afs/cern.ch/work/t/twamorka/ThesisAnalysis/CMSSW_10_5_0/src/flashgg/Signal_Jul15_ver5/signal_'+str(m)+'/output_SUSYGluGluToHToAA_AToGG_M-'+str(m)+'_TuneCUETP8M1_13TeV_pythia8.root'

    ws_name = 'h4gCandidateDumper/cms_h4g_13TeV'
    dataset_name = 'SUSYGluGluToHToAA_AToGG_M_'+str(m)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons'
    #print dataset_name
    #dataset_name = '_13TeV_4photons'
    temp_ws = TFile(inFileWS).Get(ws_name)
    temp_ws.Print()
    temp_ws.data(dataset_name).Print()
    temp_dataset = temp_ws.data(dataset_name).Clone('cms_h4g_13TeV_fourphotons')
    temp_dataset.Print()
    print temp_dataset.numEntries()
    # temp_dataset_reduced = temp_dataset.reduce('pho1_pt > 30 && pho2_pt > 20 && pho3_pt > 10 && pho4_pt > 10 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) &&  (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 100 && tp_mass < 180')
    # temp_dataset_reduced = temp_dataset.reduce('1>0')
    #print "CUT", 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 100 && tp_mass < 180 &&'+cut[mi]
    temp_dataset_reduced = temp_dataset.reduce('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 110 && tp_mass < 180 && avg_dp_mass > '+str(min) +' && avg_dp_mass < ' + str(max))
    # print temp_dataset_reduced.numEntries()

    ## Get the important variables
    tp_mass = temp_ws.var("tp_mass")
    avg_dp_mass = temp_ws.var("avg_dp_mass")
    dZ_hggVtx = temp_ws.var("dZ_hggVtx")
    dZ_zeroVtx = temp_ws.var("dZ_zeroVtx")
    dZ_bdtVtx = temp_ws.var("dZ_bdtVtx")
    weight = temp_ws.var("weight")

    # outFileWS = '/eos/user/t/twamorka/Nov11_wScalesandSmearings/Signal/signal_m_'+str(m)+'_ws_reduced_60p_coverage.root'
    # outFileWS = '/eos/user/t/twamorka/Nov11_wScalesandSmearings/Signal/pho3pho4_10PtCut/signal_m_'+str(m)+'_ws_reduced.root'
    # outFileWS = '/eos/user/t/twamorka/Ntuples_wBDTDiPhotonPairing/2016/m_60/reduceWS/signal_m_'+str(m)+'_ws_reduced.root'
    outFileWS = '/eos/user/t/twamorka/Dec_2019/m_60/hadd/signal_m_'+str(m)+'_ws_reduced_'+str(size)+'.root'
    output = TFile(outFileWS,'Recreate')
    output.mkdir('tagsDumper')
    output.cd('tagsDumper')
    ws_new = RooWorkspace('cms_h4g_13TeV_fourphotons','cms_h4g_13TeV_fourphotons')
    temp_dataset_reduced_var = temp_dataset_reduced.reduce(RooArgSet(tp_mass,avg_dp_mass,dZ_hggVtx,dZ_zeroVtx,dZ_bdtVtx,weight))
    # getattr(ws_new,'import')(temp_dataset_reduced,RooArgSet(tp_mass))
    getattr(ws_new,'import')(temp_dataset_reduced_var,RooCmdArg())
    # getattr(ws_new,'import')(temp_dataset_reduced,RooCmdArg())
    ws_new.Write()
    output.Close()
    print "Created reduced workspace for mass point = ", str(m)
