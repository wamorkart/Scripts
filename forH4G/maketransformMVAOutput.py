import ROOT
from array import array

year = '2018'

f = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
ch = ROOT.TChain('')
if (year == '2016'):
    ch.Add(f+"signal_m_60_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_45_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_45_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_35_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_35_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_25_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_25_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_15_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_15_TuneCUETP8M1_13TeV_pythia8_13TeV_H4GTag_0")
elif (year == '2017'):
    ch.Add(f+"signal_m_60_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_45_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_45_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_35_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_35_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_25_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_25_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_15_"+year+".root/tagsDumper/trees/SUSYGluGluToHToAA_AToGG_M_15_TuneCP5_13TeV_pythia8_13TeV_H4GTag_0")
else:
    ch.Add(f+"signal_m_60_"+year+".root/tagsDumper/trees/HAHMHToAA_AToGG_MA_60GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_45_"+year+".root/tagsDumper/trees/HAHMHToAA_AToGG_MA_45GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_35_"+year+".root/tagsDumper/trees/HAHMHToAA_AToGG_MA_35GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_25_"+year+".root/tagsDumper/trees/HAHMHToAA_AToGG_MA_25GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0")
    ch.Add(f+"signal_m_15_"+year+".root/tagsDumper/trees/HAHMHToAA_AToGG_MA_15GeV_TuneCP5_PSweights_13TeV_madgraph_pythia8_13TeV_H4GTag_0")
print (ch.GetEntries())


f_out = ROOT.TFile.Open(f+"cumulativeTransformation_"+year+".root","recreate")

output = '/eos/user/t/twamorka/www/H4G_Training_CombinedMass_PerYear/'

nbins = 100000
xlow = -1.
xup = 1.

Cut = 'weight*(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180)'

histoMVA = ROOT.TH1F("histoMVA","histoMVA",nbins,xlow,xup)
ch.Draw("bdt>>histoMVA",ROOT.TCut(Cut))

cumulativeHisto = histoMVA.GetCumulative()
cumulativeHisto.Scale(1./histoMVA.Integral())
cumulativeGraph = ROOT.TGraph(cumulativeHisto)
cumulativeGraph.SetTitle("cumulativeGraph")
cumulativeGraph.SetName("cumulativeGraph")

evalCumulatives = ROOT.TH1F("eval","eval",nbins,0,1)
x , y = array( 'd' ), array( 'd' )
step = (xup-xlow)/nbins
for i in range(1,nbins):
    xvalue = ROOT.TH1.GetRandom(histoMVA)
    evalCumulatives.Fill(cumulativeGraph.Eval(xvalue))
evalCumulatives.Sumw2()
evalCumulatives.Scale(1./evalCumulatives.Integral())
evalCumulatives.GetYaxis().SetRangeUser(0,2./evalCumulatives.GetNbinsX())

c = ROOT.TCanvas()
histoMVA.SetLineColor(ROOT.kRed)
histoMVA.Draw()

formats = [".png",".pdf"]

for format in formats:
    c.SaveAs(output+"_"+year+"MVAHist_func"+format)

cumulativeGraph.Draw("AP")
for format in formats:
    c.SaveAs(output+"_"+year+"cumulative"+format)

evalCumulatives.Draw("EP")
for format in formats:
    c.SaveAs(output+"_"+year+"evalx"+format)

cumulativeGraph.Write()
f_out.Write()
f_out.Close()
