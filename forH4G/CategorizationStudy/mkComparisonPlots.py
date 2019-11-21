import ROOT
from ROOT import *
from mkComparisonPlotsTools import *

gROOT.SetBatch(1)
gStyle.SetOptStat(0)

outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/MVACatStudy/'

bkg_file  = TChain('h4gCandidateDumper/trees/Data_13TeV_4photons')
bkg_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/data_2016.root')

print "Number of bkg events (from data)", bkg_file.GetEntries()

sig_file = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
sig_file.AddFile('/eos/user/t/twamorka/Ntuples_ScalesnSmearings/2016/signal_m_60.root')

print "Number of signal events", sig_file.GetEntries()

for var in Vars:
    h1 = TH1F('h1', var[2], var[3], var[4], var[5])
    h2 = TH1F('h2', var[2], var[3], var[4], var[5])

    bkg_file.Draw(var[0] +'>> h1 ',TCut(Cut_CR))
    sig_file.Draw(var[0] +'>> h2 ',TCut(Cut_Sig))

    h1.SetLineColor(kBlue-8)
    h1.SetFillColorAlpha(kBlue-8, 0.35)
    h2.SetLineColor(kSpring+4)
    h2.SetFillColorAlpha(kSpring+4, 0.35)
    h1.Scale(1./h1.Integral())
    h2.Scale(1./h2.Integral())

    max1  =  h1.GetMaximum()
    max2  =  h2.GetMaximum()
    maxy  =  max(max1,max2)

    h1.SetMaximum(maxy*1.2)

    c0 = TCanvas('', '', 800, 600)
    h1.Draw("hist same")
    h2.Draw("hist same")
    leg = TLegend(0.6, 0.7, 0.89, 0.89)

    leg.AddEntry(h1, 'Background','lf')
    leg.AddEntry(h2, 'Signal','lf')

    leg.Draw("same")
    c0.SaveAs(outputLoc+var[1]+".pdf")
    c0.SaveAs(outputLoc+var[1]+".png")
