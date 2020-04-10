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

# if (year=='2016'):
#    if doDataDriven == True:
#       data_file = open('datasets/Datasets_2016_flashgg_December2019_DataDriven.json')
#    else: data_file = open('datasets/Datasets_2016_flashgg_December2019.json')
# elif (year=='2017'):
#     print "2017"
#data_file = open('datasets/Datasets_2017_flashgg_January2020.json')
# data_file = open('datasets/Datasets_2016_flashgg_December2019_DataDriven.json')
# data_file = open('datasets/Datasets_2016_flashgg_December2019.json')
# data_file = open('datasets/Datasets_2016_flashgg_December2019_DataDriven_TightMVA.json')
data_file = open('datasets/Datasets_Mix_test.json')
# data_file = open('datasets/HToAATo4Gamma_2016Analysis_VBF_DataDriven.json')
# data_file = open('datasets/Datasets_2016_flashgg_March2020_4Photons.json')
#number of bins in histograms
nbin = 20

#plots will be saved in dirName
prefix = ""

dirName = '8April2020_onlyKin_vLoose_bdtTransform/'
#dirName = '/eos/user/t/twamorka/www/H4Gamma/3April2020_DataMixing_vLoose/'
# dirName = '/eos/user/t/twamorka/www/H4Gamma/7April2020_vLoose_PhoVarsPlusHiggsVars/'
# dirName = '27March_StackPlots_Tight'
# dirName = "25March_Gamma34_medium_VBFStrategy_wCatMVA"

# bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/vLoose_AnglesKinPlusPhotonID/'
# # bkgLocation = '/eos/user/t/twamorka/8April2020_mixing/'
# signalLocation ='/eos/user/t/twamorka/1April2020_CatTrainign/vLoose_AnglesKinPlusPhotonID/'
# dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/vLoose_AnglesKinPlusPhotonID/'


bkgLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'
signalLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'
dataLocation = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/'
# bkgLocation = '/eos/user/t/twamorka/31March2020_MixedData/'
# bkgLocation = '/eos/user/t/twamorka/forBadder_forMVAOptimization/'
# signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/'
# dataLocation = '/eos/user/t/twamorka/forBadder_forMVAOptimization/'

# bkgLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/25March2020_VBFCR_CatTrainApplied/Gamma34_Medium/'
# signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/25March2020_VBFCR_CatTrainApplied/Gamma34_Medium/'
# dataLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/25March2020_VBFCR_CatTrainApplied/Gamma34_Medium/'
# bkgLocation = "/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/"
# signalLocation = "/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/catMVA_Tight_woMVA/"
# dataLocation = "/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/catMVA_Tight_woMVA/"


# dirName = "22March_catMVA_Tight_woMVA"
# bkgLocation = "/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/catMVA_Tight_woMVA/"
# signalLocation = "/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/catMVA_Tight_woMVA/"
# dataLocation = "/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/catMVA_Tight_woMVA/"

#bkgLocation = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/OldPairing/Mixed/'
#signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'
#dataLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'
# bkgLocation = '/afs/cern.ch/work/t/twamorka/Scripts/forH4G/Skimmer/'
# signalLocation = '/afs/cern.ch/work/t/twamorka/Scripts/forH4G/Skimmer/'
# dataLocation = '/afs/cern.ch/work/t/twamorka/Scripts/forH4G/Skimmer/'
# bkgLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'
# signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'
# dataLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'
# bkgLocation = '/eos/user/t/twamorka/6Mar2020_CheckMixing_Data/hadd/'
# dataLocation = '/eos/user/t/twamorka/6Mar2020_CheckMixing_Data/hadd/'
# bkgLocation = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/Mixed/'
# dataLocation = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/BDTPairing/'
# # bkgLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_6Feb2020_OnlyMC_NoPreselection/'
# signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_6Feb2020_OnlyMC_NoPreselection/'
# dataLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_6Feb2020_OnlyMC_NoPreselection/'
# bkgLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_15/wCatMVA/'
# signalLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_15/wCatMVA/'
# dataLocation = '/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_15/wCatMVA/'

#plots to be made
plots = []
plots.append(["CTStarCS","CTStarCS","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CTStarCS","CTStarCS"])
plots.append(["CT_a1Pho1","CT_a1Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CT_a1Pho1","CT_a1Pho1"])
plots.append(["CT_a2Pho1","CT_a2Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CT_a2Pho1","CT_a2Pho1"])
plots.append(["a1ptoverhmass","(a1_Pt/tp_mass)","Cos #theta_{#gamma a_{1}}",nbin,0,1,"(a1_Pt/tp_mass)","(a1_pt/tp_mass)"])
plots.append(["a2ptoverhmass","(a2_Pt/tp_mass)","Cos #theta_{#gamma a_{1}}",nbin,0,1,"(a2_Pt/tp_mass)","(a1_pt/tp_mass)"])
plots.append(["a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass","Cos #theta_{#gamma a_{1}}",nbin,0,5,"a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass"])
plots.append(["a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass","Cos #theta_{#gamma a_{1}}",nbin,0,3,"a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass"])
plots.append(["bdt","bdt","Cos #theta_{#gamma a_{1}}",nbin,-1,1,"bdt","bdt"])
plots.append(["bdtTransformed","bdtTransformed","Cos #theta_{#gamma a_{1}}",nbin,0,1,"bdtTransformed","bdtTransformed"])
plots.append(["CTStarCS","CTStarCS","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CTStarCS_mix","CTStarCS_mix"])
plots.append(["CT_a1Pho1","CT_a1Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CT_a1Pho1_mix","CT_a1Pho1_mix"])
plots.append(["CT_a2Pho1","CT_a2Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1,"CT_a2Pho1_mix","CT_a2Pho1_mix"])
plots.append(["a1_a2_DR","a1_a2_DR","Cos #theta_{#gamma a_{1}}",nbin,0,7,"a1_a2_DR","a1_a2_DR"])
plots.append(["a1_DR","a1_DR","Cos #theta_{#gamma a_{1}}",nbin,0,7,"a1_DR","a1_DR"])
plots.append(["a2_DR","a2_DR","Cos #theta_{#gamma a_{1}}",nbin,0,7,"a2_DR","a2_DR"])
plots.append(["a1_Pt","a1_Pt","Cos #theta_{#gamma a_{1}}",nbin,0,200,"a1_Pt","a1_Pt"])
plots.append(["a2_Pt","a2_Pt","Cos #theta_{#gamma a_{1}}",nbin,0,200,"a2_Pt","a2_Pt"])
plots.append(["a1_Energy","a1_Energy","Cos #theta_{#gamma a_{1}}",nbin,0,60,"a1_Energy","a1_Energy"])
plots.append(["a2_Energy","a2_Energy","Cos #theta_{#gamma a_{1}}",nbin,0,60,"a2_Energy","a2_Energy"])
plots.append(["tp_pt","tp_pt","Cos #theta_{#gamma a_{1}}",nbin,0,200,"tp_pt","tp_pt"])
plots.append(["tp_eta","tp_eta","Cos #theta_{#gamma a_{1}}",nbin,-4,4,"tp_eta","tp_eta"])
# plots.append(["a1_PtOverMass","a1_PtOverMass","Cos #theta_{#gamma a_{1}}",nbin,0,5,"a1_PtOverMass","a1_PtOverMass"])
# plots.append(["a2_PtOverMass","a2_PtOverMass","Cos #theta_{#gamma a_{2}}",nbin,0,5,"a2_PtOverMass","a2_PtOverMass"])
#plots.append(["a1ptoverhmass","(a1_Pt/tp_mass)","Cos #theta_{#gamma a_{1}}",nbin,0,1,"(a1_Pt_mix/tp_mass_mix)","(a1_pt_mix/tp_mass_mix)"])
#plots.append(["a2ptoverhmass","(a2_Pt/tp_mass)","Cos #theta_{#gamma a_{1}}",nbin,0,1,"(a2_Pt_mix/tp_mass_mix)","(a2_pt_mix/tp_mass_mix)"])
#plots.append(["a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass","Cos #theta_{#gamma a_{1}}",nbin,0,5,"a1_Pho1PtOvera1Mass_mix","a1_Pho1PtOvera1Mass_mix"])
#plots.append(["a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass","Cos #theta_{#gamma a_{1}}",nbin,0,3,"a2_Pho1PtOvera2Mass_mix","a2_Pho1PtOvera2Mass_mix"])
plots.append(["pho1_MVA","pho1_MVA","Cos #theta_{#gamma a_{1}}",nbin,-1,1,"pho1_MVA","pho1_MVA"])
plots.append(["pho2_MVA","pho2_MVA","Cos #theta_{#gamma a_{1}}",nbin,-1,1,"pho2_MVA","pho2_MVA"])
plots.append(["pho3_MVA","pho3_MVA","Cos #theta_{#gamma a_{1}}",nbin,-1,1,"pho3_MVA","pho3_MVA"])
plots.append(["pho4_MVA","pho4_MVA","Cos #theta_{#gamma a_{1}}",nbin,-1,1,"pho4_MVA","pho4_MVA"])
# plots.append(["cat_MVA_value","cat_MVA_value","Cos #theta_{#gamma a_{1}}",nbin,-0.5,0.7,"cat_MVA_value","cat_MVA_value"])
# plots.append(["a1ptovermass","(dp1_pt/dp1_mass)","Cos #theta_{#gamma a_{1}}",nbin,0,3,"a1ptovermassmix","(a1_pt_mix/a1_mass_mix)"])
# #
# plots.append(["tp_mass","tp_mass","Cos #theta_{#gamma a_{1}}",nbin,110,180,"tp_mass_mix","tp_mass_mix"])

plots.append(["pho1_pt","pho1_pt","Cos #theta_{#gamma a_{1}}",nbin,30,100,"pho1_pt","pho1_pt"])
plots.append(["pho2_pt","pho2_pt","Cos #theta_{#gamma a_{1}}",nbin,18,100,"pho2_pt","pho2_pt"])
plots.append(["pho3_pt","pho3_pt","Cos #theta_{#gamma a_{1}}",nbin,15,100,"pho3_pt","pho3_pt"])
plots.append(["pho4_pt","pho4_pt","Cos #theta_{#gamma a_{1}}",nbin,15,70,"pho4_pt","pho4_pt"])
plots.append(["pho1_eta","pho1_eta","Cos #theta_{#gamma a_{1}}",nbin,-2.5,2.5,"pho1_eta","pho1_eta"])
plots.append(["pho2_eta","pho2_eta","Cos #theta_{#gamma a_{1}}",nbin,-2.5,2.5,"pho2_eta","pho2_eta"])
plots.append(["pho3_eta","pho3_eta","Cos #theta_{#gamma a_{1}}",nbin,-2.5,2.5,"pho3_eta","pho3_eta"])
plots.append(["pho4_eta","pho4_eta","Cos #theta_{#gamma a_{1}}",nbin,-2.5,2.5,"pho4_eta","pho4_eta"])

# plots.append(["phoptsumoverhmass","(pho4_pt+pho3_pt+pho2_pt+pho1_pt)/tp_mass","Cos #theta_{#gamma a_{1}}",nbin,0,5,"phoptsumoverhmass","(pho4_pt_mix+pho3_pt_mix+pho2_pt_mix+pho1_pt_mix)/tp_mass_mix"])

# plots.append(["nvtx", "nvtx", "Number of vertices", 100, 0, 100])
# plots.append(["npho", "npho", "Number of #gamma's", 30, 3, 10])
# plots.append(["pho1_pt", "pho1_pt", "#gamma_{1} P_{T} [GeV]", nbin, 30, 100])
# plots.append(["pho2_pt", "pho2_pt", "#gamma_{2} P_{T} [GeV]", nbin, 18, 100])
# plots.append(["pho3_pt", "pho3_pt", "#gamma_{3} P_{T} [GeV]", nbin, 10, 50])
# plots.append(["pho4_pt", "pho4_pt", "#gamma_{4} P_{T} [GeV]", nbin, 10, 50])
# plots.append(["pho1_eta", "pho1_eta", "#gamma_{1} #eta", nbin, -2.5, 2.5])
# plots.append(["pho2_eta", "pho2_eta", "#gamma_{2} #eta", nbin, -2.5, 2.5])
# plots.append(["pho3_eta", "pho3_eta", "#gamma_{3} #eta", nbin, -2.5, 2.5])
# plots.append(["pho4_eta", "pho4_eta", "#gamma_{4} #eta", nbin, -2.5, 2.5])
# plots.append(["pho1_MVA", "pho1_MVA", "#gamma_{1} MVA", nbin, -1.01, 1.01])
# plots.append(["pho2_MVA", "pho2_MVA", "#gamma_{2} MVA", nbin, -1.01, 1.01])
# plots.append(["pho3_MVA", "pho3_MVA", "#gamma_{3} MVA", nbin, -1.01, 1.01])
# plots.append(["pho4_MVA", "pho4_MVA", "#gamma_{4} MVA", nbin, -1.01, 1.01])
# plots.append(["a1_mass", "a1_mass", "a_{1} Mass [GeV]", nbin, 0, 100])
# plots.append(["a2_mass", "a2_mass", "a_{2} Mass [GeV]", nbin, 0, 100])
# plots.append(["avg_a_mass", "avg_a_mass", "Avg a Mass [GeV]", nbin, 0, 100])
# # plots.append(["a1_Pt", "a1_Pt", "a_{1} P_{T} [GeV]", nbin, 0, 100])
# # plots.append(["a2_Pt", "a2_Pt", "a_{2} P_{T} [GeV]", nbin, 0, 100])
# # plots.append(["a1_DR", "a1_DR", "a_{1} #Delta R", nbin, 0, 5])
# # plots.append(["a2_DR", "a2_DR", "a_{2} #Delta R", nbin, 0, 5])
# plots.append(["a1_a2_DR", "a1_a2_DR", "#Delta R (a_{1},a_{2})", nbin, 0, 5])
# plots.append(["a1_PtOverMass","a1_PtOverMass","a_{1} P_{T}/a_{1} Mass",nbin,0,7])
# plots.append(["a2_PtOverMass","a2_PtOverMass","a_{2} P_{T}/a_{2} Mass",nbin,0,7])
# plots.append(["a1_Ptovertp_mass","a1_Pt/tp_mass","a_{1} P_{T}/H Mass",nbin,0,2])
# plots.append(["a2_Ptovertp_mass","a2_Pt/tp_mass","a_{2} P_{T}/H Mass",nbin,0,2])
# # plots.append(["pairMVAscore","pairMVAscore","Pair MVA score",nbin,-1.1,1.1])
# plots.append(["CTStarCS","CTStarCS","Cos #theta^{*}",nbin,0,1])
# plots.append(["CT_a1Pho1","CT_a1Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1])
# plots.append(["CT_a2Pho1","CT_a2Pho1","Cos #theta_{#gamma a_{2}}",nbin,0,1])
# plots.append(["a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass","#gamma_{1} P_{T}/a_{1} Mass",nbin,0,9])
# plots.append(["a1_Pho2PtOvera1Mass","a1_Pho2PtOvera1Mass","#gamma_{2} P_{T}/a_{1} Mass",nbin,0,2.5])
# plots.append(["a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass","#gamma_{3} P_{T}/a_{2} Mass",nbin,0,2.5])
# plots.append(["a2_Pho2PtOvera2Mass","a2_Pho2PtOvera2Mass","#gamma_{4} P_{T}/a_{2} Mass",nbin,0,2.5])
# plots.append(["cat_MVA_value","cat_MVA_value","Cat MVA score",nbin,-0.6,0.4])
# plots.append(["MVAOutputTransformed","MVAOutputTransformed","MVAOutputTransformed",nbin,0,1])
# # plots.append(["min(pho1_MVA, pho2_MVA, pho3_MVA, pho4_MVA)","min(pho1_MVA, pho2_MVA, pho3_MVA, pho4_MVA)", 30, 1.5, 1.5])
# plots.append(["pho1_EGMVA", "pho1_EGMVA", "#gamma_{1} MVA", nbin, -1.01, 1.01])
# plots.append(["pho2_EGMVA", "pho2_EGMVA", "#gamma_{2} MVA", nbin, -1.01, 1.01])
# plots.append(["pho3_EGMVA", "pho3_EGMVA", "#gamma_{3} MVA", nbin, -1.01, 1.01])
# plots.append(["pho4_EGMVA", "pho4_EGMVA", "#gamma_{4} MVA", nbin, -1.01, 1.01])
# #
# plots.append(["pho12_dR", "pho12_dR", "#Delta R #gamma_{12}", nbin, 0, 5.0])
# plots.append(["pho13_dR", "pho13_dR", "#Delta R #gamma_{13}", nbin, 0, 5.0])
# plots.append(["pho14_dR", "pho14_dR", "#Delta R #gamma_{14}", nbin, 0, 5.0])
# plots.append(["pho23_dR", "pho23_dR", "#Delta R #gamma_{23}", nbin, 0, 5.0])
# plots.append(["pho24_dR", "pho24_dR", "#Delta R #gamma_{24}", nbin, 0, 5.03])
# plots.append(["pho34_dR", "pho34_dR", "#Delta R #gamma_{34}", nbin, 0, 5.0])
# plots.append(["pho12_m", "pho12_m", "Mass #gamma_{12} [GeV]", nbin, 0, 100])
# plots.append(["pho13_m", "pho13_m", "Mass #gamma_{13} [GeV]", nbin, 0, 100])
# plots.append(["pho14_m", "pho14_m", "Mass #gamma_{14} [GeV]", nbin, 0, 100])
# plots.append(["pho23_m", "pho23_m", "Mass #gamma_{23} [GeV]", nbin, 0, 100])
# plots.append(["pho24_m", "pho24_m", "Mass #gamma_{24} [GeV]", nbin, 0, 100])
# plots.append(["pho34_m", "pho34_m", "Mass #gamma_{34} [GeV]", nbin, 0, 100])
# #
#plots.append(["dp1_mass_prime", "dp1_mass_prime", "a_{1} Mass [GeV]", nbin, 0, 100])
# plots.append(["dp2_mass", "dp2_mass  ", "a_{2} Mass [GeV]", nbin, 0, 100])
# plots.append(["avg_dp_mass", "avg_dp_mass", "Avg. DiPhoton Mass [GeV]", nbin, 0, 100])
# plots.append(["dp1_dr", "dp1_dr", "#Delta R b/w #gamma's a_{1}", nbin, 0, 5.0])
# plots.append(["dp2_dr", "dp2_dr", "#Delta R b/w #gamma's a_{2}", nbin, 0, 5.0])
# plots.append(["dp1_pt", "dp1_pt", "a_{1} P_{T} [GeV]", nbin, 0, 100])
# plots.append(["dp2_pt", "dp2_pt  ","a_{2} P_{T} [GeV]", nbin, 0, 100])
# plots.append(["dp1_eta", "dp1_eta", "a_{1} #eta", nbin, -3.5, 3.5])
# plots.append(["dp2_eta", "dp2_eta  ","a_{2} #eta", nbin, -3.5, 3.5])
# plots.append(["dp12_dr", "dp12_dr", "#Delta R b/w a_{1} a_{2}",nbin,0,5])
# plots.append(["dp1_PtoverMass", "dp1_PtoverMass", "a_{1} P_{T}/a_{1} Mass", nbin, 0, 10])
# plots.append(["dp2_PtoverMass", "dp2_PtoverMass", "a_{2} P_{T}/a_{1} Mass", nbin, 0, 10])
# plots.append(["absCosThetaStar_CS", "absCosThetaStar_CS", "Cos #theta^{*}", nbin, 0, 1])
# plots.append(["absCosTheta_pho_a1", "absCosTheta_pho_a1", "Cos #theta_{#gamma a_{1}}", nbin, 0, 1])
# plots.append(["absCosTheta_pho_a2", "absCosTheta_pho_a2", "Cos #theta_{#gamma a_{2}}", nbin, 0, 1])
# plots.append(["diphoPair_MVA", "diphoPair_MVA", "DiPhoton Pairing MVA", nbin, -1.1, 1.1])
# plots.append(["absDiPhotonMassDifference", "abs(dp1_mass-dp2_mass)", "|a_{1} Mass - a_{2} Mass| [GeV]", 30, 0, 10])
# #
# plots.append(["tp_pt", "tp_pt", "Higgs P_{T} [GeV]", nbin, 0, 400])
# plots.append(["tp_eta", "tp_eta", "Higgs #eta", nbin, -3.0, 3.0])
# plots.append(["tp_mass", "tp_mass", "Higgs Mass [GeV]", nbin, 110, 180])
# plots.append(["tp_PtoverMass","tp_PtoverMass","Higgs P_{T}/Higgs Mass",nbin,0,10])
# plots.append(["DiPho1Pt_Over_Tpmass", "dp1_pt/tp_mass", "a_{1} P_{T}/Higgs Mass", nbin, 0, 0.6])
# plots.append(["DiPho2Pt_Over_Tpmass", "dp2_pt/tp_mass", "a_{2} P_{T}/Higgs Mass", nbin, 0, 0.6])
# plots.append(["a1ptovermass", "dp1_pt/dp1_mass", "a_{1} P_{T}/a_{1} Mass", nbin, 0, 7])
# plots.append(["a2ptovermass", "dp2_pt/dp2_mass", "a_{2} P_{T}/a_{2} Mass", nbin, 0, 7])
# plots.append(["(DiPhoPtSum)_Over_2Tpmass", "dp1_pt+dp2_pt/(tp_mass)", "a_{1} P_{T} + a_{2} P_{T}/2*(Higgs Mass)", nbin, 0, 100])
#plots.append(["Cat. MVA2", "cat_MVA_value", "Cat. MVA2", nbin, -0.6,0.6])
# plots.append(["Cat. MVA Old Method", "cat_MVA_value_oldmethod", "Cat. MVA Old Method", nbin, -1.01,1.01])



#cuts to be used to make plots
Cut = "1>0"
Cut_Signal = "1>0"
