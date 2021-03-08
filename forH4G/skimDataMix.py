from ROOT import *
from array import array
import argparse

gROOT.SetBatch(kTRUE)

parser =  argparse.ArgumentParser(description='cat MVA')
parser.add_argument('-y', '--year', dest='year', required=True, type=str)
parser.add_argument('-e', '--event', dest='event', required=True, type=str)

args = parser.parse_args()
year = args.year
event_num = args.event
inDir = "/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_22Jan2021/19Feb2021/H4G_PhoMVA_manyKinVars_aMass_fullRun2_DataMix_HighStat_kinWeight_dataSBScaling_MGPodd_bkgOdd_noCorrel/60/"
outDir = "/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_22Jan2021/19Feb2021/H4G_PhoMVA_manyKinVars_aMass_fullRun2_DataMix_HighStat_kinWeight_dataSBScaling_MGPodd_bkgOdd_noCorrel/60/DataMix_Skim/"

infile_data = inDir+"/data_"+year+".root"
tree_data = TChain()
tree_data.Add(infile_data+"/Data_13TeV_H4GTag_0")

sel_SB = "(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180 && !(tp_mass > 115 && tp_mass < 135) && bdt > 0.94)"

h = TH1F('h','h',100,0,100000)
tree_data.Draw("tp_mass >> h",sel_SB)
n_data = h.Integral()

print n_data

infile_bkg = TFile(inDir+"data_mix_"+year+"_even.root")

tree_bkg = infile_bkg.Get("Data_13TeV_H4GTag_0")
nentries_bkg = tree_bkg.GetEntries()

tree_bkg_out = TFile( outDir+"data_mix_"+year+"_"+event_num+".root","RECREATE")
outtree = TTree("Data_13TeV_H4GTag_0","Data_13TeV_H4GTag_0")

tp_mass = array('f',[0])
bdt = array('f',[0])
weight = array('f',[0])
# event = array('f',[0])

_tp_mass = outtree.Branch('tp_mass', tp_mass, 'tp_mass/F')
_bdt = outtree.Branch('bdt', bdt, 'bdt/F')
_weight = outtree.Branch('weight', weight, 'weight/F')
# _event = outtree.Branch('event',event,'event/F')


count = 0
# for i in range(0, nentries_bkg):
for i in range(int(event_num), nentries_bkg):
    if i%1000 == 0: print i
    tree_bkg.GetEntry(i)
    if (tree_bkg.pho1_pt > 30 and tree_bkg.pho2_pt > 18 and tree_bkg.pho3_pt > 15 and tree_bkg.pho4_pt > 15 and abs(tree_bkg.pho1_eta) < 2.5 and abs(tree_bkg.pho2_eta) < 2.5 and abs(tree_bkg.pho3_eta) < 2.5 and abs(tree_bkg.pho4_eta) < 2.5 and (abs(tree_bkg.pho1_eta) < 1.4442 or abs(tree_bkg.pho1_eta) > 1.566) and (abs(tree_bkg.pho2_eta) < 1.4442 or abs(tree_bkg.pho2_eta) > 1.566) and (abs(tree_bkg.pho3_eta) < 1.4442 or abs(tree_bkg.pho3_eta) > 1.566) and (abs(tree_bkg.pho4_eta) < 1.4442 or abs(tree_bkg.pho4_eta) > 1.566) and tree_bkg.pho1_electronveto==1 and tree_bkg.pho2_electronveto==1 and tree_bkg.pho3_electronveto==1 and tree_bkg.pho4_electronveto==1 and tree_bkg.tp_mass > 110 and tree_bkg.tp_mass < 180 and tree_bkg.bdt > 0.94):
        if (not(tree_bkg.tp_mass > 115 and tree_bkg.tp_mass < 135) ):
            count +=1

        tp_mass[0] = tree_bkg.tp_mass
        bdt[0] = tree_bkg.bdt
        weight[0] = tree_bkg.weight
        # event[0] = tree_bkg.event

        outtree.Fill()

    # print count
    if (count > n_data-1):
        break
        # print tree.weight
tree_bkg_out.cd()
outtree.Write()


tree_bkg_out.Write()
# print count
