##################################################
##################################################
## Configuration parameters to run MakeStack.py ##
##################################################
##################################################
doSignalOnly = True
doBlind = True
doSignalRegion = False

isPhoCR = False
# addHiggs = False
hideData = False
#addbbH = True
#dyjets = False

#do pile up reweighting
doPUweight = False

year = ""

doSignal = False

#Luminosity to normalize backgrounds
lumi = 35.87
signalFactor = 1
#List of datasets to be used (cross section information defined there)
# data_file = open("datasets/Datasets_2016_flashgg.json")
# data_file = open("datasets/Datasets_2016_flashgg_removeOverlap.json")
# data_file = open("datasets/Datasets_2016_flashgg_2Photons.json")
# data_file = open("datasets/Datasets_2016_flashgg_4Gamma_Jan19.json")
# data_file = open("datasets/HToAATo4Gamma_2016Analysis.json")
# data_file = open("datasets/HToAATo4Gamma_2016Analysis_DataDriven.json")
# data_file = open('datasets/Datasets_2016_flashgg_25Feb2019.json')
data_file = open('datasets/Datasets_2016_flashgg_25Feb2019_2Photons.json')
#number of bins in histograms
nbin = 30

#plots will be saved in dirName
prefix = ""
# dirSuffix = "_Nov21_flashgg_wTriggerMC_OverlapRemoval_Plots/"
#dirSuffix = "_2Photons_Test_withoutOverlapRemoval_ExtraScale/"
# dirSuffix = "_Dec4/"
# dirSuffix = "_Feb5/"
# dirSuffix = "_Test_Feb11_DataDriven_Test2"
# dirSuffix = "_Feb2019_NoCut"
# dirSuffix = "_Feb2019_KinematicCut_andMVACut2"
# dirSuffix = "_Feb2019_DataDriven_KinematicCut"
dirSuffix = "_25Feb2019_Inclusive_2Photons"
# dirPrefix = "/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg/H4GFlash/Plotter"
dirPrefix = "/afs/cern.ch/work/t/twamorka/Scripts/Plotter"
dirName = dirPrefix + dirSuffix

#Location of root files for each invidivual samples. Name of the root files is defined in datasets/datasets.json
# bkgLocation = '/eos/cms/store/user/twamorka/MC_2016_WithoutTrigger/flashgg_H4G_Bkg_2016/'
# signalLocation = '/eos/cms/store/user/twamorka/MC_2016_WithoutTrigger/flashgg_H4G_Signal_2016/'

# bkgLocation = '/eos/cms/store/user/torimoto/physics/4gamma/MC_2016_WithTrigger/flashgg_H4G_Bkg_2016/'
# signalLocation = '/eos/cms/store/user/torimoto/physics/4gamma/MC_2016_WithTrigger/flashgg_H4G_Signal_2016/'
#
# dataLocation = '/eos/cms/store/user/twamorka/flashgg_H4G_Data_2016/'
# bkgLocation = '/eos/cms/store/user/twamorka/Jan19_H4G_Bkg16/'
# signalLocation = '/eos/cms/store/user/twamorka/Jan19_H4G_Signal16/'
# dataLocation = '/eos/cms/store/user/twamorka/Jan19_H4G_Data16/'
# bkgLocation = '/eos/cms/store/user/torimoto/physics/4gamma/HToAATo4Gamma_2016Analysis/'
# signalLocation = '/eos/cms/store/user/torimoto/physics/4gamma/HToAATo4Gamma_2016Analysis/'
# dataLocation = '/eos/cms/store/user/torimoto/physics/4gamma/HToAATo4Gamma_2016Analysis/'
bkgLocation = '/eos/cms/store/user/twamorka/NTuples_17Feb2019/Background/'
signalLocation = '/eos/cms/store/user/twamorka/NTuples_17Feb2019/Signal/'
dataLocation = '/eos/cms/store/user/twamorka/NTuples_17Feb2019/Data/'

#plots to be made
plots = []
# plots.append(["nvtx", "nvtx", "Number of vertices", 100, 0, 100])
# plots.append(["n_pho", "n_pho", "Number of #gamma's", 30, 3, 10])
plots.append(["pho1_pt", "pho1_pt", "#gamma_{1} P_{T} [GeV]", nbin, 0, 500])
plots.append(["pho2_pt", "pho2_pt", "#gamma_{2} P_{T} [GeV]", nbin, 0, 500])
# plots.append(["pho3_pt", "pho3_pt", "#gamma_{3} P_{T} [GeV]", nbin, 0, 100])
# plots.append(["pho4_pt", "pho4_pt", "#gamma_{4} P_{T} [GeV]", nbin, 0, 100])
# plots.append(["pho1_eta", "pho1_eta", "#gamma_{1} #eta", 30, -3.0, 3.0])
# plots.append(["pho2_eta", "pho2_eta", "#gamma_{2} #eta", 30, -3.0, 3.0])
# plots.append(["pho3_eta", "pho3_eta", "#gamma_{3} #eta", 30, -3.0, 3.0])
# plots.append(["pho4_eta", "pho4_eta", "#gamma_{4} #eta", 30, -3.0, 3.0])
# plots.append(["pho1_MVA", "pho1_MVA", "#gamma_{1} MVA", 30, -1.2, 1.2])
# plots.append(["pho2_MVA", "pho2_MVA", "#gamma_{2} MVA", 30, -1.2, 1.2])
# plots.append(["pho3_MVA", "pho3_MVA", "#gamma_{3} MVA", 30, -1.2, 1.2])
# plots.append(["pho4_MVA", "pho4_MVA", "#gamma_{4} MVA", 30, -1.2, 1.2])
# plots.append(["min pho_MVA","min(pho1_MVA, pho2_MVA, pho3_MVA, pho4_MVA)", 30, 1.5, 1.5])
# plots.append(["pho1_EGMVA", "pho1_EGMVA", "#gamma_{1} MVA", 30, -1.5, 1.5])
# plots.append(["pho2_EGMVA", "pho2_EGMVA", "#gamma_{2} MVA", 30, -1.5, 1.5])
# plots.append(["pho3_EGMVA", "pho3_EGMVA", "#gamma_{3} MVA", 30, -1.5, 1.5])
# plots.append(["pho4_EGMVA", "pho4_EGMVA", "#gamma_{4} MVA", 30, -1.5, 1.5])
#
# plots.append(["pho12_dR", "pho12_dR", "#Delta R #gamma_{12}", 30, 0, 5.0])
# plots.append(["pho13_dR", "pho13_dR", "#Delta R #gamma_{13}", 30, 0, 5.0])
# plots.append(["pho14_dR", "pho14_dR", "#Delta R #gamma_{14}", 30, 0, 5.0])
# plots.append(["pho23_dR", "pho23_dR", "#Delta R #gamma_{23}", 30, 0, 5.0])
# plots.append(["pho24_dR", "pho24_dR", "#Delta R #gamma_{24}", 30, 0, 5.0])
# plots.append(["pho34_dR", "pho34_dR", "#Delta R #gamma_{34}", 30, 0, 5.0])
# plots.append(["pho12_m", "pho12_m", "Mass #gamma_{12} [GeV]", 30, 0, 100])
# plots.append(["pho13_m", "pho13_m", "Mass #gamma_{13} [GeV]", 30, 0, 100])
# plots.append(["pho14_m", "pho14_m", "Mass #gamma_{14} [GeV]", 30, 0, 100])
# plots.append(["pho23_m", "pho23_m", "Mass #gamma_{23} [GeV]", 30, 0, 100])
# plots.append(["pho24_m", "pho24_m", "Mass #gamma_{24} [GeV]", 30, 0, 100])
# plots.append(["pho34_m", "pho34_m", "Mass #gamma_{34} [GeV]", 30, 0, 100])
# # #
# plots.append(["dp1_mass", "dp1_mass", "DiPhoton_{1} Mass [GeV]", 30, 0, 300])
# plots.append(["dp2_mass", "dp2_mass", "DiPhoton_{2} Mass [GeV]", 30, 0, 300])
# plots.append(["avg_dp_mass", "avg_dp_mass", "Avg. DiPhoton Mass [GeV]", 30, 0, 300])
# plots.append(["dp1_dr", "dp1_dr", "#Delta R DiPhoton_{1}", 30, 0, 5.0])
# plots.append(["dp2_dr", "dp2_dr", "#Delta R DiPhoton_{2}", 30, 0, 5.0])
# #
# plots.append(["absDiPhotonMassDifference", "abs(dp1_mass-dp2_mass)", "|DiPhoton_{1} Mass - DiPhoton_{2} Mass| [GeV]", 30, 0, 10])
# plots.append(["AverageDiPhotonMass", "(dp1_mass+dp2_mass)/2", "Avg. DiPhoton Mass [GeV]", 30, 0, 100])
# plots.append(["dp1_dr", "dp1_dr", "#Delta R DiPhoton_{1}", 30, 0, 5.0])
# plots.append(["dp2_dr", "dp2_dr", "#Delta R DiPhoton_{2}", 30, 0, 5.0])
# plots.append(["dp1_PtoverMass", "dp1_PtoverMass", "DiPhoton_{1} P_{T}/Mass", 30, 0, 10])
# plots.append(["dp2_PtoverMass", "dp2_PtoverMass", "DiPhoton_{2} P_{T}/Mass", 30, 0, 10])
# # #
# plots.append(["tp_pt", "tp_pt", "TetraPhoton P_{T} [GeV]", 30, 0, 400])
# plots.append(["tp_eta", "tp_eta", "TetraPhoton #eta", 30, -3.0, 3.0])
# plots.append(["tp_mass", "tp_mass", "TetraPhoton Mass [GeV]", 100, 100, 180])
# plots.append(["DiPhoPt_Over_Tpmass", "dp1_pt/tp_mass", "dp1_pt/tp_mass", 30, 0, 1.0])
# plots.append(["Higgs Mass Difference", "abs(tp_mass - 125)", "|(tp_mass-125)| [GeV]", 30, 0, 10])
# plots.append(["absCosThetaStar_CS", "absCosThetaStar_CS", "Cos #theta^{*}", 30, 0, 1])
# plots.append(["absCosTheta_pho_a1", "absCosTheta_pho_a1", "Cos #theta^{*}", 30, 0, 1])
# plots.append(["absCosTheta_pho_a2", "absCosTheta_pho_a2", "Cos #theta^{*}", 30, 0, 1])






#cuts to be used to make plots
Cut = "1>0"
Cut_Signal = ""
