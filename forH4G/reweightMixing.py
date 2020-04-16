import ROOT
import itertools
from array import array

def findVal(trre,var):
   val = -999.
   if(var=="CTStarCS"): val = trre.CTStarCS
   elif(var=="CT_a1Pho1"): val = trre.CT_a1Pho1
   elif(var=="CT_a2Pho1"): val = trre.CT_a2Pho1
   elif(var=="a1_PtOverMass"): val = trre.a1_PtOverMass
   elif(var=="a2_PtOverMass"): val = trre.a2_PtOverMass
   elif(var=="a1_Pho1PtOvera1Mass"): val = trre.a1_Pho1PtOvera1Mass
   elif(var=="a2_Pho1PtOvera2Mass"): val = trre.a2_Pho1PtOvera2Mass
   elif(var=="bdt"): val = trre.bdt
   elif(var=="bdtTransformed"): val = trre.bdtTransformed
   elif(var=="a1_a2_DR"): val = trre.a1_a2_DR
   elif(var=="a1_DR"): val = trre.a1_DR
   elif(var=="a2_DR"): val = trre.a2_DR
   elif(var=="a1_Pt"): val = trre.a1_Pt
   elif(var=="a2_Pt"): val = trre.a2_Pt
   elif(var=="a1_Energy"): val = trre.a1_Energy
   elif(var=="a2_Energy"): val = trre.a2_Energy
   elif(var=="tp_pt"): val = trre.tp_pt
   elif(var=="tp_eta"): val = trre.tp_eta
   elif(var=="pho1_MVA"): val = trre.pho1_MVA
   elif(var=="pho2_MVA"): val = trre.pho2_MVA
   elif(var=="pho3_MVA"): val = trre.pho3_MVA
   elif(var=="pho4_MVA"): val = trre.pho4_MVA
   elif(var=="pho1_pt"): val = trre.pho1_pt
   elif(var=="pho2_pt"): val = trre.pho2_pt
   elif(var=="pho3_pt"): val = trre.pho3_pt
   elif(var=="pho4_pt"): val = trre.pho4_pt
   elif(var=="pho1_eta"): val = trre.pho1_eta
   elif(var=="pho2_eta"): val = trre.pho2_eta
   elif(var=="pho3_eta"): val = trre.pho3_eta
   elif(var=="pho4_eta"): val = trre.pho4_eta
   else: print "findVal ---> WARNING MISSING VAR: ",var

   return val

if __name__ == '__main__':

 nbin = 10
 plots = []
 #plots.append(["CTStarCS","CTStarCS","Cos #theta*",nbin,0,1])
 #plots.append(["CT_a1Pho1","CT_a1Pho1","Cos #theta_{#gamma a_{1}}",nbin,0,1])
 #plots.append(["CT_a2Pho1","CT_a2Pho1","Cos #theta_{#gamma a_{2}}",nbin,0,1])
 #plots.append(["a1_PtOverMass","(a1_Pt/tp_mass)","a1 (pT)/ h (mass)",nbin,0,1])
 #plots.append(["a2_PtOverMass","(a2_Pt/tp_mass)","a1 (pT) / h (mass)",nbin,0,1])
 #plots.append(["a1_Pho1PtOvera1Mass","a1_Pho1PtOvera1Mass","#gamma1 (pT) / a1 (mass)",nbin,0,5])
 #plots.append(["a2_Pho1PtOvera2Mass","a2_Pho1PtOvera2Mass","#gamma3 (pT) / a2 (mass)",nbin,0,3])
 #plots.append(["bdt","bdt","BDT",nbin,-1,1])
 #plots.append(["bdtTransformed","bdtTransformed","Transformed MVA",nbin,0,1])
 #plots.append(["a1_a2_DR","a1_a2_DR","#Delta R (a1,a2)",nbin,0,7])
 #plots.append(["a1_DR","a1_DR","#Delta R (#gamma1, #gamma2)",nbin,0,7])
 #plots.append(["a2_DR","a2_DR","#Delta R (#gamma3, #gamma4)",nbin,0,7])
 #plots.append(["a1_Pt","a1_Pt","a1 (pT) [GeV]",nbin,0,200])
 #plots.append(["a2_Pt","a2_Pt","a2 (pT) [GeV]",nbin,0,200])
 #plots.append(["a1_Energy","a1_Energy","a1 (Energy) [GeV]",nbin,0,60])
 #plots.append(["a2_Energy","a2_Energy","a2 (Energy) [GeV]",nbin,0,60])
 #plots.append(["tp_pt","tp_pt","Higgs pT [GeV]",nbin,0,200])
 #plots.append(["tp_eta","tp_eta","Higgs #eta",nbin,-4,4])
 #plots.append(["pho1_MVA","pho1_MVA","#gamma1 MVA",nbin,-1,1])
 #plots.append(["pho2_MVA","pho2_MVA","#gamma2 MVA",nbin,-1,1])
 #plots.append(["pho3_MVA","pho3_MVA","#gamma3 MVA",nbin,-1,1])
 #plots.append(["pho4_MVA","pho4_MVA","#gamma4 MVA",nbin,-1,1])
 plots.append(["pho1_pt","pho1_pt","#gamma1 pT [GeV]",nbin,30,100])
 plots.append(["pho2_pt","pho2_pt","#gamma2 pT [GeV]",nbin,18,100])
 plots.append(["pho3_pt","pho3_pt","#gamma3 pT [GeV]",nbin,15,100])
 plots.append(["pho4_pt","pho4_pt","#gamma4 pT [GeV]",nbin,15,70])
 #plots.append(["pho1_eta","pho1_eta","#gamma1 #eta",nbin,-2.5,2.5])
 #plots.append(["pho2_eta","pho2_eta","#gamma2 #eta",nbin,-2.5,2.5])
 #plots.append(["pho3_eta","pho3_eta","#gamma3 #eta",nbin,-2.5,2.5])
 #plots.append(["pho4_eta","pho4_eta","#gamma4 #eta",nbin,-2.5,2.5])

 fin_datamix = ROOT.TFile.Open('/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/data_mixing_transformedMVA.root')
 tree_datamix = fin_datamix.Get('Data_13TeV_4photons')

 fin_data = ROOT.TFile.Open('/eos/user/t/twamorka/1April2020_CatTrainign/vLoose_OnlyPhotonID/data_all.root')
 tree_data = fin_data.Get('Data_13TeV_4photons')

 Cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_electronveto==1 && pho2_electronveto==1 && pho3_electronveto==1 && pho4_electronveto==1 && tp_mass > 110 && tp_mass < 180 && !(tp_mass > 115 && tp_mass < 135) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9'

 Histos = []
 weight_data = {}
 weight_datamix = {}

 for plot in plots:
    Histos.append(ROOT.TH1F("histo_"+plot[0], plot[2], int(plot[3]), float(plot[4]), float(plot[5])))

 histo_scale_data = ROOT.TH1F("histo_scale_data","",100000,-1.,1.)
 histo_scale_datamix = ROOT.TH1F("histo_scale_datamix","",100000,-1.,1.)
 tree_datamix.Draw('pho1_MVA >> histo_scale_datamix',ROOT.TCut(Cut))
 tree_data.Draw('pho1_MVA >> histo_scale_data',ROOT.TCut(Cut))
 scale = float(histo_scale_data.Integral())/float(histo_scale_datamix.Integral())

 print "Computing occupancies for datamix..."
 nentries = tree_datamix.GetEntries()
 for i in range(0, nentries):
    #if i%1000 == 0: print i
    tree_datamix.GetEntry(i)
    if tree_datamix.pho1_pt > 30 and tree_datamix.pho2_pt > 18 and tree_datamix.pho3_pt > 15 and tree_datamix.pho4_pt > 15 and  abs(tree_datamix.pho1_eta) < 2.5 and abs(tree_datamix.pho2_eta) < 2.5 and abs(tree_datamix.pho3_eta) < 2.5 and abs(tree_datamix.pho4_eta) < 2.5 and (abs(tree_datamix.pho1_eta) < 1.4442 or abs(tree_datamix.pho1_eta) > 1.566) and (abs(tree_datamix.pho2_eta) < 1.4442 or abs(tree_datamix.pho2_eta) > 1.566) and (abs(tree_datamix.pho3_eta) < 1.4442 or abs(tree_datamix.pho3_eta) > 1.566) and (abs(tree_datamix.pho4_eta) < 1.4442 or abs(tree_datamix.pho4_eta) > 1.566) and tree_datamix.pho1_electronveto==1 and tree_datamix.pho2_electronveto==1 and tree_datamix.pho3_electronveto==1 and tree_datamix.pho4_electronveto==1 and tree_datamix.tp_mass > 110 and tree_datamix.tp_mass < 180 and (tree_datamix.tp_mass <= 115 or tree_datamix.tp_mass >= 135) and tree_datamix.pho1_MVA > -0.9 and tree_datamix.pho2_MVA > -0.9 and tree_datamix.pho3_MVA > -0.9 and tree_datamix.pho4_MVA > -0.9:
       iVar=0
       subset = []
       for plot in plots:
          ibin = Histos[iVar].FindBin(findVal(tree_datamix,plot[0]))
          if ibin==0: ibin=1
          if ibin==Histos[iVar].GetNbinsX()+1: ibin=Histos[iVar].GetNbinsX()
          subset.append(ibin)
          iVar+=1
       if tuple(subset) in weight_datamix:
          weight_datamix[tuple(subset)]+=1
       else:
          weight_datamix[tuple(subset)]=1

 print "Computing occupancies for data..."
 nentries = tree_data.GetEntries()
 for i in range(0, nentries):
    #if i%1000 == 0: print i
    tree_data.GetEntry(i)
    if tree_data.pho1_pt > 30 and tree_data.pho2_pt > 18 and tree_data.pho3_pt > 15 and tree_data.pho4_pt > 15 and  abs(tree_data.pho1_eta) < 2.5 and abs(tree_data.pho2_eta) < 2.5 and abs(tree_data.pho3_eta) < 2.5 and abs(tree_data.pho4_eta) < 2.5 and (abs(tree_data.pho1_eta) < 1.4442 or abs(tree_data.pho1_eta) > 1.566) and (abs(tree_data.pho2_eta) < 1.4442 or abs(tree_data.pho2_eta) > 1.566) and (abs(tree_data.pho3_eta) < 1.4442 or abs(tree_data.pho3_eta) > 1.566) and (abs(tree_data.pho4_eta) < 1.4442 or abs(tree_data.pho4_eta) > 1.566) and tree_data.pho1_electronveto==1 and tree_data.pho2_electronveto==1 and tree_data.pho3_electronveto==1 and tree_data.pho4_electronveto==1 and tree_data.tp_mass > 110 and tree_data.tp_mass < 180 and (tree_data.tp_mass <= 115 or tree_data.tp_mass >= 135) and tree_data.pho1_MVA > -0.9 and tree_data.pho2_MVA > -0.9 and tree_data.pho3_MVA > -0.9 and tree_data.pho4_MVA > -0.9:
       iVar=0
       subset = []
       for plot in plots:
          ibin = Histos[iVar].FindBin(findVal(tree_data,plot[0]))
          if ibin==0: ibin=1
          if ibin==Histos[iVar].GetNbinsX()+1: ibin=Histos[iVar].GetNbinsX()
          subset.append(ibin)
          iVar+=1
       if tuple(subset) in weight_data:
          weight_data[tuple(subset)]+=1
       else:
          weight_data[tuple(subset)]=1

 outfile = ROOT.TFile('test_addweight.root', "RECREATE")
 outtree = tree_datamix.CloneTree(0)
 mix_weight = array('f', [0])
 _mix_weight = outtree.Branch('mix_weight', mix_weight, 'mix_weight/F')
 nentries = tree_datamix.GetEntries()
 for i in range(0, nentries):
    #if i%1000 == 0: print i
    tree_datamix.GetEntry(i)
    weight=0.
    if tree_datamix.pho1_pt > 30 and tree_datamix.pho2_pt > 18 and tree_datamix.pho3_pt > 15 and tree_datamix.pho4_pt > 15 and  abs(tree_datamix.pho1_eta) < 2.5 and abs(tree_datamix.pho2_eta) < 2.5 and abs(tree_datamix.pho3_eta) < 2.5 and abs(tree_datamix.pho4_eta) < 2.5 and (abs(tree_datamix.pho1_eta) < 1.4442 or abs(tree_datamix.pho1_eta) > 1.566) and (abs(tree_datamix.pho2_eta) < 1.4442 or abs(tree_datamix.pho2_eta) > 1.566) and (abs(tree_datamix.pho3_eta) < 1.4442 or abs(tree_datamix.pho3_eta) > 1.566) and (abs(tree_datamix.pho4_eta) < 1.4442 or abs(tree_datamix.pho4_eta) > 1.566) and tree_datamix.pho1_electronveto==1 and tree_datamix.pho2_electronveto==1 and tree_datamix.pho3_electronveto==1 and tree_datamix.pho4_electronveto==1 and tree_datamix.tp_mass > 110 and tree_datamix.tp_mass < 180 and (tree_datamix.tp_mass <= 115 or tree_datamix.tp_mass >= 135) and tree_datamix.pho1_MVA > -0.9 and tree_datamix.pho2_MVA > -0.9 and tree_datamix.pho3_MVA > -0.9 and tree_datamix.pho4_MVA > -0.9:
       iVar=0
       subset = []
       for plot in plots:
          ibin = Histos[iVar].FindBin(findVal(tree_datamix,plot[0]))
          if ibin==0: ibin=1
          if ibin==Histos[iVar].GetNbinsX()+1: ibin=Histos[iVar].GetNbinsX()
          subset.append(ibin)
          iVar+=1
       if (tuple(subset) in weight_data) and weight_datamix[tuple(subset)]!=0:
          weight=float(weight_data[tuple(subset)])/float(weight_datamix[tuple(subset)])*1./scale
    mix_weight[0] = weight
    outtree.Fill()

 outfile.cd()
 outtree.Write()
 outfile.Close()
