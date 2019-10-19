import ROOT
from ROOT import *
import math
from array import array

import argparse
parser =  argparse.ArgumentParser(description='Photon ID MVA Optimizer')
parser.add_argument('-s', '--signal', dest='sig', required=True, type=str)
parser.add_argument('-b', '--background', dest='bac', required=True, type=str)
parser.add_argument('-v', '--var', dest='var', required=True, type=str)
parser.add_argument('-c', '--cut', dest='cut', required=True, type=str)
parser.add_argument('-o', '--outputLoc', dest='outputLoc', required=True, type=str)

opt = parser.parse_args()
sigMass = opt.sig
bkg = opt.bac
var = opt.var
cut = opt.cut
outputLoc = opt.outputLoc

print "here"
print opt.cut
f_sig = TFile('/eos/user/t/twamorka/newCatalog_fixVtx_3Oct2019/hadd_Tree/signal_m_'+str(sigMass)+'.root')
t_sig = f_sig.Get('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(sigMass)+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')

bkgFiles = []
if bkg == 'QCD':
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/QCD30to40.root','QCD_Pt_30to40_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8_13TeV_4photons','QCD 30to40'])
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/QCD30toInf.root','QCD_Pt_30toInf_DoubleEMEnriched_MGG_40to80_TuneCUETP8M1_13TeV_Pythia8_13TeV_4photons','QCD 30toInf'])
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/QCD40toInf.root','QCD_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8_13TeV_4photons','QCD 40toInf'])

elif bkg == 'GJet':
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/GJet20toInf.root','GJet_Pt_20toInf_DoubleEMEnriched_MGG_40to80_TuneCUETP8M1_13TeV_Pythia8_13TeV_4photons','GJet 20toInf'])
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/GJet40toInf.root','GJet_Pt_40toInf_DoubleEMEnriched_MGG_80toInf_TuneCUETP8M1_13TeV_Pythia8_13TeV_4photons','GJet 40toInf'])

elif bkg == 'DiPho':
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/DiPho40to80.root','DiPhotonJetsBox_M40_80_Sherpa_13TeV_4photons','DiPho 40to80'])
   bkgFiles.append(['/eos/user/t/twamorka/2016Ntuples/DiPho80toInf.root','DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa_13TeV_4photons','DiPho 80toInf'])



Cut_Cat = []
i = -0.9
while i<1:
    # print i
    Cut_Cat.append(['pho1_MVA > '+str(i)+' && pho2_MVA >'+str(i)+'&&'+cut, 'pho1_MVA > '+str(i)+' && pho2_MVA >'+str(i)+' && pho3_MVA >' + str(i) +' && pho4_MVA >'+str(i)+'&&'+cut,'pho1_MVA > -0.9 && pho2_MVA > -0.9'+' && pho3_MVA >'+str(i)+' && pho4_MVA >'+str(i)+'&&'+cut] )
    i += 0.1

t_bkg = TChain()
for file in bkgFiles:
    t_bkg.Add(str(file[0])+'/h4gCandidateDumper/trees/'+str(file[1]))

print t_bkg.GetEntries()


t_sig.Draw(var + '>> h_sig')
t_bkg.Draw(var + '>> h_bkg')
tot_sig =  h_sig.Integral()
tot_bkg = h_bkg.Integral()
hists = []
graphs  = TMultiGraph()
sigEff_Cat0, bkgEff_Cat0 = array( 'd' ), array( 'd' )
sigEff_Cat1, bkgEff_Cat1 = array( 'd' ), array( 'd' )
sigEff_Cat2, bkgEff_Cat2 = array( 'd' ), array( 'd' )
for cut in Cut_Cat:
    t_sig.Draw(var + '>> h0_sig',TCut(cut[0]))
    t_bkg.Draw(var + '>> h0_bkg',TCut(cut[0]))
    sigEff_Cat0.append(h0_sig.Integral()/tot_sig)
    bkgEff_Cat0.append(1-(h0_bkg.Integral()/tot_bkg))

    t_sig.Draw(var + '>> h1_sig',TCut(cut[1]))
    t_bkg.Draw(var + '>> h1_bkg',TCut(cut[1]))
    sigEff_Cat1.append(h1_sig.Integral()/tot_sig)
    bkgEff_Cat1.append(1-(h1_bkg.Integral()/tot_bkg))

    t_sig.Draw(var + '>> h2_sig',TCut(cut[2]))
    t_bkg.Draw(var + '>> h2_bkg',TCut(cut[2]))
    sigEff_Cat2.append(h2_sig.Integral()/tot_sig)
    bkgEff_Cat2.append(1-(h2_bkg.Integral()/tot_bkg))


gr1 = TGraph(len(sigEff_Cat0),sigEff_Cat0,bkgEff_Cat0)
gr1.SetMarkerColor(kBlack)
gr1.SetMarkerStyle(20)
gr1.SetMarkerSize(1.5)

gr2 = TGraph(len(sigEff_Cat1),sigEff_Cat1,bkgEff_Cat1)
gr2.SetMarkerColor(kRed)
gr2.SetMarkerStyle(20)
gr2.SetMarkerSize(1.5)

gr3 = TGraph(len(sigEff_Cat2),sigEff_Cat2,bkgEff_Cat2)
gr3.SetMarkerColor(kGreen)
gr3.SetMarkerStyle(20)
gr3.SetMarkerSize(1.5)


c0 = TCanvas("c", "c", 800, 750)
c0.SetGridy()
c0.SetGridx()
leg = TLegend(0.152882, 0.167143, 0.442356, 0.357143)
leg.SetBorderSize(0)
leg.SetTextSize(0.04)
leg.SetFillColor(kWhite)
leg.SetFillStyle(0)
graphs.Add(gr1)
graphs.Add(gr2)
graphs.Add(gr3)
leg.AddEntry(gr1,"Cut 1","lp")
leg.AddEntry(gr2,"Cut 2","lp")
leg.AddEntry(gr3,"Cut 3","lp")
graphs.SetTitle(";Signal Efficiency; 1- Background Efficiency")
graphs.Draw("AP")
leg.Draw("same")
c0.SaveAs(outputLoc+'Eff_'+str(bkg)+'_'+str(opt.cut)+'.pdf')
c0.SaveAs(outputLoc+'Eff_'+str(bkg)+'_'+str(opt.cut)+'.png')
