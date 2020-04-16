import ROOT
import argparse
parser =  argparse.ArgumentParser(description='cat MVA')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)

args = parser.parse_args()
mass = args.mass

bkg_file = ROOT.TChain()
bkg_file.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim/m_'+str(mass)+'/data_all_m_'+str(mass)+'_skim_datdrivenbkg.root/Data_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim/m_'+str(mass)+'/DiPho40to80_m_'+str(mass)+'_skim_datdrivenbkg.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim/m_'+str(mass)+'/DiPho80toInf_m_'+str(mass)+'_skim_datdrivenbkg.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

print 'Background events: ', bkg_file.GetEntries()

sig_file = ROOT.TChain()
sig_file.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim/m_'+str(mass)+'/signal_m_'+str(mass)+'_skim.root/SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

print 'Signal events: ', sig_file.GetEntries()

f_out = ROOT.TFile('LearningOutput_BDT_H4G_Ma60_1Jan2020_check.root','RECREATE')

# Create the TMVA factory
ROOT.TMVA.Tools.Instance()
factory = ROOT.TMVA.Factory("TMVAClassification", f_out,"AnalysisType=Classification")

mvaVars = [
'a1_PtOverMass',
'a2_PtOverMass',
'a1_Pt/tp_mass',
# 'a2_Pt/tp_mass',
'pairMVAscore',
'CTStarCS',
'CT_a1Pho1',
'CT_a2Pho1',
'a1_a2_DR'
# 'a1_Pho1PtOvera1Mass',
# 'a1_Pho2PtOvera1Mass',
# 'a2_Pho1PtOvera2Mass',
# 'a2_Pho2PtOvera2Mass'
]
dataloader = ROOT.TMVA.DataLoader("dataset")

for x in mvaVars:
    dataloader.AddVariable(x,'F')

dataloader.AddSignalTree(sig_file)
dataloader.AddBackgroundTree(bkg_file)


sigCut = ROOT.TCut('pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && tp_mass > 110 && tp_mass < 180 ')

bkgCut = ROOT.TCut(' pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && !((tp_mass > 115 && tp_mass < 135))')
# Prepare the training/testing signal/background
# factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")

#dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")
dataloader.PrepareTrainingAndTestTree(sigCut,bkgCut,"nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=NumEvents:!V")
# factory.PrepareTrainingAndTestTree(sigCut,bkgCut,"SplitMode=Random:NormMode=NumEvents:!V")

# method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")#:nCuts=200")
# method = factory.BookMethod( ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")#:nCuts=200")
method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "!H:!V:NTrees=850:MinNodeSize=2.5%:MaxDepth=3:BoostType=AdaBoost:AdaBoostBeta=0.5:UseBaggedBoost:BaggedSampleFraction=0.5:SeparationType=GiniIndex:nCuts=20")
#method = factory.BookMethod( dataloader,ROOT.TMVA.Types.kBDT, "BDT", "UseRandomisedTrees=1:NTrees=1000:BoostType=Grad:NegWeightTreatment=IgnoreNegWeightsInTraining:MaxDepth=3:MinNodeSize=3:Shrinkage=0.1625")
factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

# f_out.Close()
#
c1 = factory.GetROCCurve(dataloader)
c1.SaveAs('ROC_Ma60_Data_30Dec2019_check.pdf')
