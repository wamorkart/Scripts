import ROOT
from ROOT import *
from mkComparisonPlotsTools import *
import argparse

parser =  argparse.ArgumentParser(description='MVA Categorization')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)

opt = parser.parse_args()
mass = opt.mass

gROOT.SetBatch(1)
gStyle.SetOptStat(0)

# outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/MVACatStudy/DataCR/'
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/8Jan2020_MVACatInputVars/'


# bkg_file  = TChain('h4gCandidateDumper/trees/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/data_2016.root')

bkg_file_DiPho  = TChain()
bkg_file_DiPho.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/DiPho40to80_skim.root/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
bkg_file_DiPho.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/DiPho80toInf_skim.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

# bkg_file_DiPho.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim_Dec30/m_'+str(mass)+'/CatMVAApplied/DiPho80toInf_m_'+str(mass)+'_skim.root/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

# bkg_file_DiPho.AddFile('/eos/user/t/twamorka/Dec_2019/m_60/hadd/DiPho40to80.root/h4gCandidateDumper/trees/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
# bkg_file_DiPho.AddFile('/eos/user/t/twamorka/Dec_2019/m_60/hadd/DiPho80toInf.root/h4gCandidateDumper/trees/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

# bkg_file_Data = TChain()
# bkg_file_Data.AddFile('/eos/user/t/twamorka/Dec_2019/m_60/hadd/data_2016.root/h4gCandidateDumper/trees/Data_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/DiPho40to80.root/h4gCandidateDumper/trees/DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons')
# bkg_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/DiPho80toInf.root/h4gCandidateDumper/trees/DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons')

# print "Number of bkg events (from data)", bkg_file.GetEntries()

sig_file = TChain('SUSYGluGluToHToAA_AToGG_M_'+str(mass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# sig_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/signal_m_'+str(mass)+'.root')
# sig_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/signal_m_'+str(mass)+'.root')
# sig_file.AddFile('/eos/user/t/twamorka/Dec_2019/m_60/hadd/signal_m_'+str(mass)+'.root')
# sig_file.AddFile('/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/Skim_Dec30/m_'+str(mass)+'/signal_m_'+str(mass)+'_skim.root')
sig_file.AddFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/signal_m_'+str(mass)+'_skim.root')
print "Number of signal events", sig_file.GetEntries()
print "Number of background events", bkg_file_DiPho.GetEntries()

for var in Vars:
    h1 = TH1F('h1', var[2], var[3], var[4], var[5])
    h2 = TH1F('h2', var[2], var[3], var[4], var[5])
    h_tot_bkg = TH1F('h_tot_bkg', var[2], var[3], var[4], var[5])

    h_sig = TH1F('h_sig', var[2], var[3], var[4], var[5])

    bkg_file_DiPho.Draw(var[0] +'>> h1 ',TCut(Cut_SR))
    # bkg_file_Data.Draw(var[0] +'>> h2 ',TCut(Cut_CR))

    h_tot_bkg = h1.Clone()
    # h_tot_bkg.Add(h2)
    sig_file.Draw(var[0] +'>> h_sig ',TCut(Cut_Sig))

    h_tot_bkg.SetLineColor(kBlue-8)
    h_tot_bkg.SetFillColorAlpha(kBlue-8, 0.35)
    h_sig.SetLineColor(kSpring+4)
    h_sig.SetFillColorAlpha(kSpring+4, 0.35)
    h_tot_bkg.Scale(1./h_tot_bkg.Integral())
    h_sig.Scale(1./h_sig.Integral())

    max1  =  h_sig.GetMaximum()
    max2  =  h_tot_bkg.GetMaximum()
    maxy  =  max(max1,max2)

    h_tot_bkg.SetMaximum(maxy*1.2)

    c0 = TCanvas('', '', 800, 600)
    h_tot_bkg.Draw("hist same")
    h_sig.Draw("hist same")
    leg = TLegend(0.6, 0.7, 0.89, 0.89)

    leg.AddEntry(h_tot_bkg, 'DiPho+Jets','lf')
    leg.AddEntry(h_sig, 'Signal m(a) = '+str(mass)+' GeV','lf')

    leg.Draw("same")
    c0.SaveAs(outputLoc+var[1]+"_"+str(mass)+".pdf")
    c0.SaveAs(outputLoc+var[1]+"_"+str(mass)+".png")
