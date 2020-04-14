import ROOT
from array import array

fin_datamix = ROOT.TFile.Open('/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/data_mixing_transformedMVA.root')
tree_datamix = fin_datamix.Get('Data_13TeV_4photons')

fin_data = ROOT.TFile.Open('/eos/user/t/twamorka/1April2020_CatTrainign/vLoose_OnlyPhotonID/data_all.root')
tree_data = fin_data.Get('Data_13TeV_4photons')

Cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180 && !(tp_mass > 115 && tp_mass < 135) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9'


nbins = 30
xlow = 0
xup = 500

histo_higgs_pt_datamix = ROOT.TH1F("histo_higgs_pt_datamix","histo_higgs_pt_datamix",nbins,xlow,xup)
histo_higgs_pt_data = ROOT.TH1F("histo_higgs_pt_data","histo_higgs_pt_data",nbins,xlow,xup)

tree_data.Draw('tp_pt >> histo_higgs_pt_data',ROOT.TCut(Cut))
tree_datamix.Draw('tp_pt >> histo_higgs_pt_datamix',ROOT.TCut(Cut))

# print histo_higgs_pt_datamix.Integral()
histo_higgs_pt_datamix.Scale(465/histo_higgs_pt_datamix.Integral())
histo_ratio = histo_higgs_pt_datamix.Clone("histo_ratio")
histo_ratio.Divide(histo_higgs_pt_data)

# print  histo_higgs_pt_data.Integral()
# print histo_higgs_pt_datamix.Integral()

c = ROOT.TCanvas()
histo_higgs_pt_data.Draw('hist')
c.SaveAs('histo_higgs_pt_data.pdf')

histo_higgs_pt_datamix.Draw('hist')
c.SaveAs('histo_higgs_pt_datamix.pdf')

# for bin in range(0, nbins):
    # print "data: ", histo_higgs_pt_data.GetBinContent(bin+1),"  bkg: ", histo_higgs_pt_datamix.GetBinContent(bin+1), "  ratio: ", histo_ratio.GetBinContent(bin+1)
outfile = ROOT.TFile('test_addweight.root', "RECREATE")
outtree = tree_datamix.CloneTree(0)
mix_weight = array('f', [0])
_mix_weight = outtree.Branch('mix', mix_weight, 'mix_weight/F')

nentries = tree_datamix.GetEntries()
for i in range(0, nentries):
    if i%1000 == 0: print i
    tree_datamix.GetEntry(i)
    print tree_datamix.tp_pt
    nbin = histo_ratio.GetXaxis().FindBin(tree_datamix.tp_pt)
    print "nbin: ", nbin, " weight: ", histo_ratio.GetBinContent(nbin)
    mix_weight[0] = histo_ratio.GetBinContent(nbin)

    outtree.Fill()

outfile.cd()
outtree.Write()
outfile.Close()



histo_ratio.SetLineColor(ROOT.kRed)
histo_ratio.Draw('hist')
c.SaveAs('histo_ratio.pdf')
