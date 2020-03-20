import ROOT
import argparse
parser =  argparse.ArgumentParser(description='cat MVA')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)

args = parser.parse_args()
mass = args.mass

bkg_file = ROOT.TChain()
#bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(mass)+'/treesForTraining/DiPho40to80_skim_datdrivenbkg.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
#bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(mass)+'/treesForTraining/DiPho80toInf_skim_datdrivenbkg.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')
#bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(mass)+'/treesForTraining/data_all_skim_datdrivenbkg.root/Data_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/treesForTraining/DiPho40to80_skim_datdrivenbkg.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/treesForTraining/DiPho80toInf_skim_datdrivenbkg.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/treesForTraining/data_all_skim_datdrivenbkg.root/Data_13TeV_4photons')

print 'Background events: ', bkg_file.GetEntries()

sig_file = ROOT.TChain()
#sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(mass)+'/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

print 'Signal events: ', sig_file.GetEntries()

# f_out =  ROOT.TFile('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/CatMVAWeights/LearningOutput_BDT_H4G_Ma'+str(mass)+'.root','RECREATE')
# f_out = ROOT.TFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/CatMVAWeights_20Jan2020/LearningOutput_BDT_H4G_Ma'+str(mass)+'_20Jan2020.root','RECREATE')
f_out = ROOT.TFile('_13Jan2020_test.root','RECREATE')


# f_out = ROOT.TFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim_Dec30/CatWeights/LearningOutput_BDT_H4G_Ma'+str(mass)+'_2Jan2020_check.root','RECREATE')
ROOT.TMVA.Tools.Instance()
factory = ROOT.TMVA.Factory("TMVAClassification", f_out,"AnalysisType=Classification")

# mvaVars = [
# 'a1_PtOverMass',
# 'a2_PtOverMass',
# 'a1_Pt/tp_mass',
# #'a1_mass',
# #'a2_mass',
# # 'a2_Pt/tp_mass',
# 'pairMVAscore',
# 'CTStarCS',
# 'CT_a1Pho1',
# 'CT_a2Pho1',
# 'a1_a2_DR'
# #'a1_Pho1PtOvera1Mass',
# #'a2_Pho1PtOvera2Mass'
# ]
mvaVars = [
'CTStarCS',
'CT_a1Pho1',
'CT_a2Pho1',
'a1_Pt/tp_mass',
# 'a2_Pt/tp_mass',
'a1_Pt/a1_mass',
# 'a2_Pt/a2_mass',
'a1_a2_DR',
'a1_Pho1PtOvera1Mass',
# 'a1_Pho2PtOvera1Mass',
'a2_Pho1PtOvera2Mass'
#'pairMVAscore',
# 'a2_Pho2PtOvera2Mass',
#'rho'
# 'a1_mass',
# 'a2_mass'
]

dataloader = ROOT.TMVA.DataLoader("dataset")

for x in mvaVars:
    dataloader.AddVariable(x,"F")

dataloader.AddSignalTree(sig_file)
dataloader.AddBackgroundTree(bkg_file)

#sigCut = ROOT.TCut('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 110 && tp_mass < 180 ')

#bkgCut = ROOT.TCut(' pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && !((tp_mass > 115 && tp_mass < 135))')

sigCut = ROOT.TCut('(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9)')
bkgCut = ROOT.TCut('(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && !((tp_mass > 115 && tp_mass < 135)))')
# sigCut = ROOT.TCut('(pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9)')
# bkgCut = ROOT.TCut('!(tp_mass > 115 && tp_mass < 135)')
# sigCut = ROOT.TCut('pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9')
# bkgCut = ROOT.TCut('!((tp_mass > 115 && tp_mass < 135))')
#bkgCut = ROOT.TCut('1>0')
#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
#factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
#method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")
#method = factory.BookMethod(ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")
dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=200")#:nCuts=200")
# method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625:nCuts=200")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

f_out.Close()

c1 = factory.GetROCCurve(dataloader)
#c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/CatMVAWeights/ROC_'+str(mass)+'.pdf')
# c1.SaveAs('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/CatMVAWeights_20Jan2020/ROC_20Jan2020_'+str(mass)+'.pdf')
