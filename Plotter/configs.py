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
year = 2016
isPhoCR = False
hideData = False
lumi = 36

#do pile up reweighting
doPUweight = False
doSignal = False


#Luminosity to normalize backgrounds
# if (year=='2016'):
#    lumi = 35.9
# elif (year=='2017'):
#     lumi = 41.5
# signalFactor = 1

print year
print lumi

data_file = open('datasets/Datasets_Mix_test.json')
# data_file = open('datasets/HToAATo4Gamma_2016Analysis_VBF_DataDriven.json')
# data_file = open('datasets/Datasets_2016_flashgg_March2020_4Photons.json')
#number of bins in histograms
nbin = 30

#plots will be saved in dirName
prefix = ""
# dirName = '25May2020_test'
# dirName = '7June2020_vLooseMVACut'
dirName = '8Jul2020_noweight'
# dirName = '23May2020_m60_CatTrain_phoMVA_BDTPair_nophoMVACut_nomixweight'
# dirName = '5May2020_m15_BDTPairing_CatTrain_phoMVA_nophoMVACut_nomixweight'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/15May2020_WithReweight_m60Training/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/4May2020_CommonTraining_VBF_Gamma34_Loose/CatTrain_allVars_combined_plusOthers/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/1May2020_BDTPairing_withoutdeltaMVar_m60_phoMVA_BDTPair/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/30April2020_BDTPairing_VBF_m60/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/24April2020_withreweighting_phoMVA_BDTPair_m15/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/27April2020_afterReweighting_commonPairingTraining_m60/30April2020_ModifiedMixing/noPresel/'
# dirName = ''

bkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/2016/hadd/'
dataLocation = '/eos/user/t/twamorka/h4g_fullRun2/2016/hadd/'
signalLocation = '/eos/user/t/twamorka/h4g_fullRun2/2016/hadd/'
# bkgLocation = '/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/CatTrain_phoMVA/'
# dataLocation = '/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/CatTrain_phoMVA/'
# signalLocation = '/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/CatTrain_phoMVA/'
# bkgLocation = '/eos/user/t/twamorka/5May2020_m15_BDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# dataLocation = '/eos/user/t/twamorka/5May2020_m15_BDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# signalLocation = '/eos/user/t/twamorka/5May2020_m15_BDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# bkgLocation = '/eos/user/t/twamorka/2May2020_CommonBDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# dataLocation = '/eos/user/t/twamorka/2May2020_CommonBDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# signalLocation = '/eos/user/t/twamorka/2May2020_CommonBDTPairing/CatTrain_phoMVA_nophoMVACut_nomixweight/'
# bkgLocation = '/eos/user/t/twamorka/1May2020_BDTPairing_withoutdeltaMVar_m60/1May2020_BDTPairing_withoutdeltaMVar_m60_phoMVA_BDTPair/'
# dataLocation = '/eos/user/t/twamorka/1May2020_BDTPairing_withoutdeltaMVar_m60/1May2020_BDTPairing_withoutdeltaMVar_m60_phoMVA_BDTPair/'
# signalLocation = '/eos/user/t/twamorka/1May2020_BDTPairing_withoutdeltaMVar_m60/1May2020_BDTPairing_withoutdeltaMVar_m60_phoMVA_BDTPair/'
# bkgLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/nvtx_Mixing/'
# dataLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/'
# signalLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/'


# dirName = '/eos/user/t/twamorka/www/H4Gamma/17April2020_Mixing2_BeforeReweighting_BDTPairing_M60/17April2020_NoReweighting_PhoMVA_PairBDT/'

# bkgLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_15/27April2020_withreweighting_phoMVA_BDTPair/'
# dataLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_15/27April2020_withreweighting_phoMVA_BDTPair/'
# signalLocation = '/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_15/27April2020_withreweighting_phoMVA_BDTPair/'

# bkgLocation = '/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_15/24April2020_withreweighting_phoMVA_BDTPair/'
# dataLocation = '/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_15/24April2020_withreweighting_phoMVA_BDTPair/'
# signalLocation = '/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_15/24April2020_withreweighting_phoMVA_BDTPair/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/16April2020_Mixing2_BeforeReweighting/'

# bkgLocation = '/eos/user/t/twamorka/16April2020_Ntuples_OldPairing/Mixing_2/'
# signalLocation = '/eos/user/t/twamorka/16April2020_Ntuples_OldPairing/'
# dataLocation = '/eos/user/t/twamorka/16April2020_Ntuples_OldPairing/'

# dirName = '16April_VBFCR_Plots'
# dirName = '14April_Mix_Reweight'
# dirName = '16April2020_Mix_reweight_aptvars'
# dirName = '11April2020_TESTVBFPlot_wBDT'

# bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/'
# signalLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/'
# dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/'
# bkgLocation = '/afs/cern.ch/work/t/twamorka/Scripts/forH4G/'
# bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'
# signalLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'
# dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'

# bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/11April2020_VBFTraining_LooseWP/VBF_Train_Applied/'
# signalLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/11April2020_VBFTraining_LooseWP/VBF_Train_Applied/'
# dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/11April2020_VBFTraining_LooseWP/VBF_Train_Applied/'

# bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/VBF_Train_Applied/'
# signalLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/VBF_Train_Applied/'
# dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/VBF_Train_Applied/'

#plots to be made
plots = []
# plots.append(['dp_mass_diff','a1_mass-a2_mass','dp_mass_diff',nbin,0,5])
# plots.append(["CTStarCS","CTStarCS","Cos #theta*",nbin,0,1])
# plots.append(["CT_a1Pho1","CT_a1Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1])
# plots.append(["CT_a2Pho1","CT_a2Pho1","Cos #theta_{#gamma a_{2}}",nbin,0,1])
# plots.append(["a1ptoverhmass","(a1_Pt/tp_mass)","a1 (pT)/ h (mass)",nbin,0,1])
# plots.append(["a2ptoverhmass","(a2_Pt/tp_mass)","a1 (pT) / h (mass)",nbin,0,1])
# plots.append(["a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass","#gamma1 (pT) / a1 (mass)",nbin,0,5])
# plots.append(["a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass","#gamma3 (pT) / a2 (mass)",nbin,0,3])
# plots.append(["bdt","bdt","BDT",nbin,-1,1])
# plots.append(["bdtTransformed","bdtTransformed","Transformed MVA",nbin,0,1])
# plots.append(["pairMVAscore","pairMVAscore","pairMVAscore", nbin,-1,1])
# plots.append(["a1_mass","a1_mass","M(a1) [GeV]",nbin,0,100])
# plots.append(["a2_mass","a2_mass","M(a2) [GeV]",nbin,0,100])
# plots.append(["AvgAMass","(a1_mass+a2_mass)/2","Avg a mass [GeV]",nbin,0,100])
# plots.append(["a1_a2_DR","a1_a2_DR","#Delta R (a1,a2)",nbin,0,7])
# plots.append(["a1_DR","a1_DR","#Delta R (#gamma1, #gamma2)",nbin,0,7])
# plots.append(["a2_DR","a2_DR","#Delta R (#gamma3, #gamma4)",nbin,0,7])
# plots.append(["a1_Pt","a1_Pt","a1 (pT) [GeV]",nbin,0,200])
# plots.append(["a2_Pt","a2_Pt","a2 (pT) [GeV]",nbin,0,200])
# plots.append(["a1_Energy","a1_Energy","a1 (Energy) [GeV]",nbin,0,60])
# plots.append(["a2_Energy","a2_Energy","a2 (Energy) [GeV]",nbin,0,60])
# plots.append(["tp_mass","tp_mass","Higgs Mass [GeV]",nbin,110,180])
# plots.append(["tp_pt","tp_pt","Higgs pT [GeV]",nbin,0,200])
# plots.append(["tp_eta","tp_eta","Higgs #eta",nbin,-4,4])
plots.append(["pho1_MVA","pho1_MVA","#gamma1 MVA",nbin,-1,1])
plots.append(["pho2_MVA","pho2_MVA","#gamma2 MVA",nbin,-1,1])
plots.append(["pho3_MVA","pho3_MVA","#gamma3 MVA",nbin,-1,1])
plots.append(["pho4_MVA","pho4_MVA","#gamma4 MVA",nbin,-1,1])
# plots.append(["pho1_pt","pho1_pt","#gamma1 pT [GeV]",nbin,30,100])
# plots.append(["pho2_pt","pho2_pt","#gamma2 pT [GeV]",nbin,18,100])
# plots.append(["pho3_pt","pho3_pt","#gamma3 pT [GeV]",nbin,15,100])
# plots.append(["pho4_pt","pho4_pt","#gamma4 pT [GeV]",nbin,15,70])
# plots.append(["pho1_eta","pho1_eta","#gamma1 #eta",nbin,-2.5,2.5])
# plots.append(["pho2_eta","pho2_eta","#gamma2 #eta",nbin,-2.5,2.5])
# plots.append(["pho3_eta","pho3_eta","#gamma3 #eta",nbin,-2.5,2.5])
# plots.append(["pho4_eta","pho4_eta","#gamma4 #eta",nbin,-2.5,2.5])


#cuts to be used to make plots
Cut = "1>0"
Cut_Signal = "1>0"
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
