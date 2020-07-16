import ROOT
import argparse
parser =  argparse.ArgumentParser(description='cat MVA')
# parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)
parser.add_argument('-o', '--output', dest='output', required=True, type=str)
parser.add_argument('-oD', '--outputDir', dest='outputDir', required=True, type=str)
parser.add_argument('-WP','--WP',dest='WP',required = True, type=str)


args = parser.parse_args()
# mass = args.mass
output = args.output
outputDir = args.outputDir
WP = args.WP

## Files used for VBF related training
bkg_file = ROOT.TChain()
bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/data_mix.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/5May2020_m15_BDTPairing/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/data_CR.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/DiPho40to80.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/DiPho80toInf.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/5May2020_m15_BDTPairing/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/data_all.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/data_mix.root/Data_13TeV_4photons')

# bkg_file.AddFile('/eos/user/t/twamorka/1May2020_BDTPairing_withoutdeltaMVar_m60/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/wVBFWeightApplied/data_CR.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/wVBFWeightApplied/DiPho40to80.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/wVBFWeightApplied/DiPho80toInf.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_55/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_50/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_45/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_40/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_35/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_30/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_25/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_20/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_15/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')

# bkg_file.AddFile('/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_15/data_mix_reweight_phoMVAvars.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_60/data_mix_all_skim.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/Input_Ntuple/data_mix_reweight_phoMVAVars_withSel.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/16April2020_PhotonIDPlusAPt_reweight_mix_vLoose/data_mix_16April2020_phoMVAplusaptvars_reweight.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/data_CR_preselapplied.root/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/DiPho80toInf_skim_preselapplied.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/DiPho40to80_skim_preselapplied.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/afs/cern.ch/work/t/twamorka/Scripts/forH4G/test_addweight_loosesel_phomvavars_15bins.root')

sig_file = ROOT.TChain()
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_60.root/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_55.root/SUSYGluGluToHToAA_AToGG_M_55_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_50.root/SUSYGluGluToHToAA_AToGG_M_50_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_45.root/SUSYGluGluToHToAA_AToGG_M_45_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_40.root/SUSYGluGluToHToAA_AToGG_M_40_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_35.root/SUSYGluGluToHToAA_AToGG_M_35_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_30.root/SUSYGluGluToHToAA_AToGG_M_30_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_25.root/SUSYGluGluToHToAA_AToGG_M_25_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_20.root/SUSYGluGluToHToAA_AToGG_M_20_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/VBF_Gamma34_Loose/signal_m_15.root/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

# sig_file.AddFile('/eos/user/t/twamorka/5May2020_m15_BDTPairing/signal_m_15.root/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_60.root/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_55.root/SUSYGluGluToHToAA_AToGG_M_55_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_50.root/SUSYGluGluToHToAA_AToGG_M_50_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_45.root/SUSYGluGluToHToAA_AToGG_M_45_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_40.root/SUSYGluGluToHToAA_AToGG_M_40_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_35.root/SUSYGluGluToHToAA_AToGG_M_35_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_30.root/SUSYGluGluToHToAA_AToGG_M_30_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_25.root/SUSYGluGluToHToAA_AToGG_M_25_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_20.root/SUSYGluGluToHToAA_AToGG_M_20_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/2May2020_CommonBDTPairing/signal_m_15.root/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_60.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_55.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_55_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_50.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_50_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_45.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_45_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_40.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_40_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_35.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_35_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_30.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_30_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_25.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_25_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_20.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_20_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/28May_2016Ntuples_ZeroVtx/hadd/signal_m_15.root/h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

# sig_file.AddFile('/eos/user/t/twamorka/1May2020_BDTPairing_withoutdeltaMVar_m60/signal_m_60.root/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/wVBFWeightApplied/signal_m_60.root/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_60/signal_m_60.root/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_55/signal_m_55.root/SUSYGluGluToHToAA_AToGG_M_55_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_50/signal_m_50.root/SUSYGluGluToHToAA_AToGG_M_50_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_45/signal_m_45.root/SUSYGluGluToHToAA_AToGG_M_45_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_40/signal_m_40.root/SUSYGluGluToHToAA_AToGG_M_40_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_35/signal_m_35.root/SUSYGluGluToHToAA_AToGG_M_35_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_30/signal_m_30.root/SUSYGluGluToHToAA_AToGG_M_30_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_25/signal_m_25.root/SUSYGluGluToHToAA_AToGG_M_25_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_20/signal_m_20.root/SUSYGluGluToHToAA_AToGG_M_20_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/26April2020_Ntuples_CommonBDTPairing/m_15/signal_m_15.root/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

# sig_file.AddFile('/eos/user/t/twamorka/16April2020_Ntuples_BDTPairing/m_15/signal_m_15.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/Input_Ntuple/signal_m_60_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/1April2020_CatTrainign/12April2020_VBFTraining_withsamplewithoutBlindCut/signal_m_60_skim_preselapplied.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# # bkg_file = ROOT.TChain()
# # bkg_file.AddFile('/eos/user/t/twamorka/31March2020_MixedData/data_mix_add.root/Data_13TeV_4photons')
# # bkg_file.AddFile('/afs/cern.ch/work/t/twamorka/Scripts/forH4G/test_mix_30March_2.root/Data_13TeV_4photons')
# # bkg_file.AddFile('/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/SameBranchName/data_mix_MVATrain_presel.root/Data_13TeV_4photons')
# #bkg_file.AddFile('/eos/user/t/twamorka/Quaruntuples_11032020/hadd/OldPairing/Mixed/sameBranchName/data_mixed_presel.root/Data_13TeV_4photons')
# print 'Background events: ', bkg_file.GetEntries()
#
# sig_file = ROOT.TChain()
# sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# # sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
#
# print 'Signal events: ', sig_file.GetEntries()

f_out = ROOT.TFile(outputDir+output+'.root','RECREATE')

ROOT.TMVA.Tools.Instance()
factory = ROOT.TMVA.Factory("TMVAClassification", f_out,"AnalysisType=Classification")

mvaVars = [
# 'CTStarCS',
# 'CT_a1Pho1',
# 'CT_a2Pho1',
# 'a1_Pt/tp_mass',
# 'a2_Pt/tp_mass',
# 'a1_Pho1PtOvera1Mass',
# 'a2_Pho1PtOvera2Mass',
'pho1_MVA',
'pho2_MVA',
'pho3_MVA',
'pho4_MVA',
#'pairMVAscore'
# 'pho1_pt',
# 'pho2_pt',
# 'pho3_pt',
# 'pho4_pt',
# 'pho1_eta',
# 'pho2_eta',
# 'pho3_eta',
# 'pho4_eta',
# 'tp_pt',
# 'tp_eta'
]

dataloader = ROOT.TMVA.DataLoader("dataset")

for x in mvaVars:
    #factory.AddVariable(x,"F")
    dataloader.AddVariable(x,"F")

#factory.AddSignalTree(sig_file)
#factory.AddBackgroundTree(bkg_file)
dataloader.AddSignalTree(sig_file)
dataloader.AddBackgroundTree(bkg_file)

if (WP == 'veryLoose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9)'
elif (WP == 'Loose'):
    Cut_MVA = 'pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.75 && pho4_MVA > -0.75)'
elif (WP == 'Medium'):
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.75 && pho4_MVA > -0.75)'
else:
    Cut_MVA = 'pho1_MVA > -0.2 && pho2_MVA > -0.4 && pho3_MVA > -0.5 && pho4_MVA > -0.5)'

Cut_Signal = '(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180  &&'
# Cut_Background = '(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && !((tp_mass > 115 && tp_mass < 135)) && '
# Cut_Background_weight = '(mix_weight)*'

# Cut_Signal = 'weight_VBF'
# Cut_Background = '(weight_VBF)*(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && !((tp_mass > 115 && tp_mass < 135)) &&'

# Cut_Signal = '(1>0 &&'
# Cut_Background = '(mix_weight)*(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && !(tp_mass > 115 && tp_mass < 135)  &&  '
Cut_Background = '(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass <180 && !(tp_mass > 115 && tp_mass < 135)   &&'
# Cut_Background = '(mix_weight)*(!(tp_mass > 115 && tp_mass < 135) &&'
#
Cut_add = 'pho1_MVA > -999. && pho2_MVA > -999. && pho3_MVA > -999. && pho4_MVA > -999)'
sigCut = ROOT.TCut(Cut_Signal+Cut_add)
bkgCut = ROOT.TCut(Cut_Background+Cut_add)

# sigCut = ROOT.TCut(Cut_Signal)
# bkgCut = ROOT.TCut(Cut_Background)


print "S Cut: ", sigCut
print "B Cut: ", bkgCut

# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=200")#:nCuts=200")

dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=750:MinNodeSize=3%:MaxDepth=5:BoostType=AdaBoost:AdaBoostBeta=0.1:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")#:nCuts=200")

# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
# method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")
# method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=500:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")

# factory.OptimizeAllMethods("SigEffAt001","Scan");
# factory.OptimizeAllMethods("ROCIntegral","FitGA");

#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
#method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")

#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
#method = factory.BookMethod( dataloader, ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")
#method = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")
# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=200")#:nCuts=200")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

# f_out.Close()

# c1 = factory.GetROCCurve(dataloader)
#c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/CatMVAWeights/ROC_'+str(mass)+'.pdf')
# c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/CatMVAWeights_20Jan2020/ROC_20Jan2020_'+str(mass)+'.pdf')
