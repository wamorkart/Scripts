import ROOT
from ROOT import *

bkg_file = TChain('h4gCandidateDumper/trees/Data_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/data_2016.root')


sig_file = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/signal_m_60.root')

f_out = TFile('LearningOutput_BDT_H4G_Ma60.root','RECREATE')

# Create the TMVA factory
ROOT.TMVA.Tools.Instance()
factory = ROOT.TMVA.Factory("TMVAClassification", f_out,"AnalysisType=Classification")


mvaVars = [
'absCosThetaStar_CS',
'absCosTheta_pho_a1',
'absCosTheta_pho_a2',
'dp1_pt/tp_mass',
'dp2_pt/tp_mass',
'dp1_PtoverMass',
'dp2_PtoverMass'
]
dataloader = ROOT.TMVA.DataLoader("dataset")

# for x in mvaVars:
#     factory.AddVariable(x,'F')

for x in mvaVars:
    dataloader.AddVariable(x,'F')

# Link the signal and background to the root_data ntuple
# factory.AddSignalTree(bkg_file)
# factory.AddBackgroundTree(sig_file)

dataloader.AddSignalTree(sig_file)
dataloader.AddBackgroundTree(bkg_file)

sigCut = TCut('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6')

bkgCut = TCut('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && (pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA < -0.6 && pho4_MVA < -0.6) || (pho1_MVA > -0.9 && pho3_MVA > -0.6 && pho2_MVA < -0.9 && pho4_MVA < -0.6) || (pho1_MVA > -0.9 && pho4_MVA > -0.6 && pho2_MVA < -0.9 && pho3_MVA < -0.6) || (pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho1_MVA < -0.9 && pho4_MVA < -0.6) || (pho2_MVA > -0.9 && pho4_MVA > -0.6 && pho1_MVA < -0.9 && pho3_MVA < -0.6) || (pho3_MVA > -0.6 && pho4_MVA > -0.6 && pho1_MVA < -0.9 && pho2_MVA < -0.9) && !((tp_mass > 115 && tp_mass < 135))')

# Prepare the training/testing signal/background
# factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")

# dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")

# method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")
method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")#:nCuts=200")

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

f_out.Close()

c1 = factory.GetROCCurve(dataloader)
c1.SaveAs('ROC.pdf')

TMVA.TMVAGui('LearningOutput_BDT_H4G_Ma60.root')
gApplication.Run()
