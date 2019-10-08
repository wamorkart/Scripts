from ROOT import *
nbins = 40
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/SignalComparison_2016and2017/'
Vars = []
Vars.append(['pho1_pt',';P_{T}(#gamma_{1}) [GeV]; Normalized Yields',nbins,28,100])
Vars.append(['pho2_pt',';P_{T}(#gamma_{2}) [GeV]; Normalized Yields',nbins,28,100])
Vars.append(['pho3_pt',';P_{T}(#gamma_{3}) [GeV]; Normalized Yields',nbins,10,70])
Vars.append(['pho4_pt',';P_{T}(#gamma_{4}) [GeV]; Normalized Yields',nbins,10,70])


Files_2016 = []
Files_2016.append(['/eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_Tree/signal_m_60.root','m(a) = 60 GeV; 2016 MC','h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons'])

Files_2017 = []
Files_2017.append(['/eos/user/t/twamorka/newCatalog_fixVtx_2017_7Oct2019/hadd_Tree/signal_m_60.root','m(a) = 60 GeV; 2017 MC','h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCP5_13TeV_pythia8_13TeV_4photons'])

mass  = [60,55,50,45,40,35,30,25,20,15,10,5,1]

files = [] ## [file name 2016,label name 2016, tree name 2016, file name 2017, label name 2017, tree name 2017]
files.append(['/eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_Tree/signal_m_','m(a) = 60 GeV; 2016 MC','_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons','/eos/user/t/twamorka/newCatalog_fixVtx_2017_7Oct2019/hadd_Tree/signal_m_','m(a) = 60 GeV; 2017 MC','_TuneCP5_13TeV_pythia8_13TeV_4photons'])
