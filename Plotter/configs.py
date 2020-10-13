##################################################
##################################################
## Configuration parameters to run MakeStack.py ##
##################################################
##################################################
doSignalOnly = True
doBlind = True
doSignalRegion = False
doKinCut = True
doHggMVALoose = False
doHggMVATight = False
doEGMVA = False
doHiggsWindow = True
mvaWP = 'veryLoose'
bkgtype = 'mix'
doreweight = True


doDataDriven = True
year = 2017 ## year == 1 refers to full run 2
isPhoCR = False
hideData = False
lumi = 1
#do pile up reweighting
doPUweight = False
doSignal = False

file_json = ''

dirName = '/eos/user/t/twamorka/www/H4G_Training_CombinedMass_PerYear/LowStatDataMix/'

SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'

if (year==2016):
   lumi = 35.9
   file_json = 'datasets/Datasets_Mix_2016.json'
elif (year==2017):
    lumi = 41.5
    file_json = 'datasets/Datasets_Mix_2017.json'
elif (year==2018):
    lumi = 54.38
    file_json = 'datasets/Datasets_Mix_2018.json'
elif (year==1):
    lumi = 35.9+41.5+54.38
    file_json = 'datasets/Datasets_Mix_FullRun2.json'
signalFactor = 1

# print year
# print lumi

print file_json
data_file = open(file_json)

#number of bins in histograms
nbin = 30

prefix = ''

#plots to be made
plots = []
plots.append(["cosThetaStarCS_dM","cosThetaStarCS_dM","Cos #theta*",nbin,-1,1])
plots.append(["cosTheta_a1_dM","cosTheta_a1_dM","Cos #theta_{#gamma a_{1}}",nbin,-1,1])
plots.append(["cosTheta_a2_dM","cosTheta_a2_dM","Cos #theta_{#gamma a_{2}}",nbin,-1,1])
plots.append(["a1_mass_dM","a1_mass_dM","M(a1) [GeV]",nbin,0,100])
plots.append(["a2_mass_dM","a2_mass_dM","M(a2) [GeV]",nbin,0,100])
plots.append(["a1_a2_dR_dM","a1_a2_dR_dM","#Delta R (a1,a2)",nbin,0,7])
plots.append(["a1_dR_dM","a1_dR_dM","#Delta R (#gamma1, #gamma2)",nbin,0,4])
plots.append(["a2_dR_dM","a2_dR_dM","#Delta R (#gamma3, #gamma4)",nbin,0,4])
plots.append(["a1_pt_dM","a1_pt_dM","a1 (pT) [GeV]",nbin,0,230])
plots.append(["a2_pt_dM","a2_pt_dM","a2 (pT) [GeV]",nbin,0,200])
plots.append(["a1_energy_dM","a1_energy_dM","a1 (energy) [GeV]",nbin,0,260])
plots.append(["a2_energy_dM","a2_energy_dM","a2 (energy) [GeV]",nbin,0,260])
plots.append(["a1_a2_MassDiff","a1_mass_dM-a2_mass_dM","(a1 M - a2 M) [GeV]",nbin,-100,100])

plots.append(["tp_mass","tp_mass","Higgs Mass [GeV]",nbin,110,180])
plots.append(["tp_pt","tp_pt","Higgs pT [GeV]",nbin,0,200])
plots.append(["tp_eta","tp_eta","Higgs #eta",nbin,-4,4])
plots.append(["pho1_MVA","pho1_MVA","#gamma1 MVA",nbin,-1,1])
plots.append(["pho2_MVA","pho2_MVA","#gamma2 MVA",nbin,-1,1])
plots.append(["pho3_MVA","pho3_MVA","#gamma3 MVA",nbin,-1,1])
plots.append(["pho4_MVA","pho4_MVA","#gamma4 MVA",nbin,-1,1])
plots.append(["pho1_pt","pho1_pt","#gamma1 pT [GeV]",nbin,30,100])
plots.append(["pho2_pt","pho2_pt","#gamma2 pT [GeV]",nbin,18,100])
plots.append(["pho3_pt","pho3_pt","#gamma3 pT [GeV]",nbin,15,100])
plots.append(["pho4_pt","pho4_pt","#gamma4 pT [GeV]",nbin,15,70])
plots.append(["pho1_eta","pho1_eta","#gamma1 #eta",nbin,-2.5,2.5])
plots.append(["pho2_eta","pho2_eta","#gamma2 #eta",nbin,-2.5,2.5])
plots.append(["pho3_eta","pho3_eta","#gamma3 #eta",nbin,-2.5,2.5])
plots.append(["pho4_eta","pho4_eta","#gamma4 #eta",nbin,-2.5,2.5])

# plots.append(["bdt_datamixSigRegion","bdt","BDT",nbin,-1,1])
# plots.append(["bdtTransformed_datamixSigRegion","bdtTransformed","Transformed MVA",nbin,0,1])


#cuts to be used to make plots
Cut = "1>0"
Cut_Signal = "1>0"
Cut_Bkg = "1>0"
