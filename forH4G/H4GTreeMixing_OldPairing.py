#!/usr/bin/python
import numpy as n
import ROOT
# from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *
from optparse import OptionParser
import operator

if __name__ == '__main__':


  parser = OptionParser()
  parser.add_option(   "-i", "--inputFile",   dest="inputFile",    default="input.root",       type="string",  help="Input file" )
  parser.add_option(   "-o", "--outputFile",  dest="outputFile",   default="output.root",      type="string",  help="Output file")
  parser.add_option(   "-t", "--tree",  dest="tree",   default="tree",      type="string",  help="tree")
  #/afs/cern.ch/user/a/amassiro/public/H4G/signal_m_50.root

  (options, args) = parser.parse_args()

  # itree = ROOT.TChain("SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons")
  itree = ROOT.TChain(str(options.tree))
  itree.AddFile(options.inputFile)

  print "Total number of events to be analyzed:", itree.GetEntries()

  outRoot = ROOT.TFile(options.outputFile, "RECREATE")
  outtree = itree.CloneTree(0)
  # outtree = ROOT.TTree("H4GMix","H4GMix")

  def getCosThetaStar_CS():
      h_lor = PP1 + PP2
      h = ROOT.TLorentzVector(0,0,0,0)
      h.SetPxPyPzE(h_lor.Px(),h_lor.Py(),h_lor.Pz(),h_lor.E())
      a1_lor = PP1
      a_1 = ROOT.TLorentzVector(0,0,0,0)
      a_1.SetPxPyPzE(a1_lor.Px(),a1_lor.Py(),a1_lor.Pz(),a1_lor.E())
      a_1.Boost(-h.BoostVector())
      return a_1.CosTheta()

  def helicityCosTheta( Booster,  Boosted):
      BoostVector = Booster.BoostVector()
      Boosted.Boost( -BoostVector.x(), -BoostVector.y(), -BoostVector.z() );
      return Boosted.CosTheta()

  def CosThetaAngles():
      helicityThetas = []
      Boosted_a1 = ROOT.TLorentzVector(0,0,0,0)
      Boosted_a1.SetPxPyPzE(PP1.Px(),PP1.Py(),PP1.Pz(),PP1.E())
      BoostedLeadingPhoton_a1 = ROOT.TLorentzVector(0,0,0,0)
      BoostedLeadingPhoton_a1.SetPxPyPzE(pairedDiphos[0][1].Px(),pairedDiphos[0][1].Py(),pairedDiphos[0][1].Pz(),pairedDiphos[0][1].E())
      helicityThetas.append( helicityCosTheta(Boosted_a1, BoostedLeadingPhoton_a1))

      Boosted_a2 = ROOT.TLorentzVector(0,0,0,0)
      Boosted_a2.SetPxPyPzE(PP2.Px(),PP2.Py(),PP2.Pz(),PP2.E())
      BoostedLeadingPhoton_a2 = ROOT.TLorentzVector(0,0,0,0)
      BoostedLeadingPhoton_a2.SetPxPyPzE(pairedDiphos[1][1].Px(),pairedDiphos[1][1].Py(),pairedDiphos[1][1].Pz(),pairedDiphos[1][1].E())
      helicityThetas.append( helicityCosTheta(Boosted_a2, BoostedLeadingPhoton_a2))
      return helicityThetas

  def Preselection(Pho1_vec,Pho2_vec):
        isPreselected = False
        if (
        (Pho1_vec[1] > 0.8 or Pho1_vec[2] < 20 or (Pho1_vec[2]/Pho1_vec[0].Pt()) < 0.3 )
        and (Pho2_vec[1] > 0.8 or Pho2_vec[2] < 20 or (Pho2_vec[2]/Pho2_vec[0].Pt() < 0.3))
        and (Pho1_vec[3] < 0.08 and Pho2_vec[3] < 0.08)
        and ( ((abs(Pho1_vec[4]) < 1.4442 and Pho1_vec[3] < 0.07)or (abs(Pho1_vec[4]) > 1.566 and Pho1_vec[3] < 0.035)) and ((abs(Pho2_vec[4]) < 1.4442 and  Pho2_vec[3] < 0.07)or(abs(Pho2_vec[4]) > 1.566 and Pho2_vec[3] < 0.035) ) )
        and ( ((abs(Pho1_vec[4]) < 1.4442) or (abs(Pho1_vec[4]) > 1.566)) and ((abs(Pho2_vec[4]) < 1.4442 )or(abs(Pho2_vec[4]) > 1.566 ) ) )
        and (Pho1_vec[0].Pt()> 30.0 and Pho2_vec[0].Pt()> 18.0)
        and (abs(Pho1_vec[4]) < 2.5 and abs(Pho2_vec[4]) < 2.5)
        and (abs(Pho1_vec[4]) < 1.4442 or abs(Pho2_vec[4]) > 1.566 )
        and (abs(Pho1_vec[4]) < 1.4442 or abs(Pho2_vec[4]) > 1.566)
        and ( (abs(Pho1_vec[4]) < 1.4442 and abs(Pho2_vec[4]) < 1.4442)
        or (abs(Pho1_vec[4]) < 1.4442 and Pho1_vec[1]>0.85 and abs(Pho2_vec[4]) > 1.566 and Pho2_vec[1]>0.90 )
        or (abs(Pho1_vec[4]) > 1.566 and Pho1_vec[1]>0.90 and abs(Pho2_vec[4]) < 1.4442 and Pho2_vec[1]>0.85 )
        or (abs(Pho1_vec[4]) > 1.566 and Pho1_vec[1]>0.90 and abs(Pho2_vec[4]) > 1.566 and Pho2_vec[1]>0.90 ) )
        and ((Pho1_vec[0]+Pho2_vec[0])).M() > 55
        and (Pho1_vec[0].Pt() > 0.47*Pho1_vec[0].M() and Pho2_vec[0].Pt() > 0.28*Pho2_vec[0].M())
        and (Pho1_vec[5] == 0) and (Pho2_vec[5]==0)
        ):
         isPreselected = True

        return isPreselected

  pho1_pt_mix = array('f', [0])
  pho2_pt_mix = array('f', [0])
  pho3_pt_mix = array('f', [0])
  pho4_pt_mix = array('f', [0])
  pho1_eta_mix = array('f', [0])
  pho2_eta_mix = array('f', [0])
  pho3_eta_mix = array('f', [0])
  pho4_eta_mix = array('f', [0])
  pho1_electronveto_mix = array('f',[0])
  pho2_electronveto_mix = array('f',[0])
  pho3_electronveto_mix = array('f',[0])
  pho4_electronveto_mix = array('f',[0])
  pho1_MVA_mix = array('f', [0])
  pho2_MVA_mix = array('f', [0])
  pho3_MVA_mix = array('f', [0])
  pho4_MVA_mix = array('f', [0])
  pho_minMVA_mix = array('f', [0])
  pho_maxMVA_mix = array('f', [0])
  pho12_DR_mix = array('f', [0])
  pho13_DR_mix = array('f', [0])
  pho14_DR_mix = array('f', [0])
  pho23_DR_mix = array('f', [0])
  pho24_DR_mix = array('f', [0])
  pho34_DR_mix = array('f', [0])
  pho12_M_mix = array('f', [0])
  pho13_M_mix = array('f', [0])
  pho14_M_mix = array('f', [0])
  pho23_M_mix = array('f', [0])
  pho24_M_mix = array('f', [0])
  isPresel = array('i',[0])
  pho34_M_mix = array('f', [0])
  a1_mass_mix = array('f',[0])
  a2_mass_mix = array('f',[0])
  avg_a_mass_mix = array('f',[0])
  a1_Pt_mix = array('f',[0])
  a2_Pt_mix = array('f',[0])
  a1_Eta_mix = array('f',[0])
  a2_Eta_mix = array('f',[0])
  a1_Phi_mix = array('f',[0])
  a2_Phi_mix = array('f',[0])
  a1_Energy_mix = array('f',[0])
  a2_Energy_mix = array('f',[0])
  a1_DR_mix = array('f',[0])
  a2_DR_mix = array('f',[0])
  a1_a2_DR_mix = array('f',[0])
  a1_iPho1_mix = array('f',[0])
  a1_iPho2_mix = array('f',[0])
  a2_iPho1_mix = array('f',[0])
  a2_iPho2_mix = array('f',[0])
  a1_PtOverMass_mix = array('f',[0])
  a2_PtOverMass_mix = array('f',[0])
  a1_Pho1PtOvera1Mass_mix = array('f',[0])
  a1_Pho2PtOvera1Mass_mix = array('f',[0])
  a2_Pho1PtOvera2Mass_mix = array('f',[0])
  a2_Pho2PtOvera2Mass_mix = array('f',[0])
  CTStarCS_mix = array('f',[0])
  CT_a1Pho1_mix = array('f',[0])
  CT_a2Pho1_mix = array('f',[0])
  tp_mass_mix  = array('f',[0])
  tp_pt_mix  = array('f',[0])
  tp_eta_mix = array('f',[0])
  tp_phi_mix  = array('f',[0])

  _pho1_pt_mix = outtree.Branch('pho1_pt_mix',pho1_pt_mix,'pho1_pt_mix/F')
  _pho2_pt_mix = outtree.Branch('pho2_pt_mix',pho2_pt_mix,'pho2_pt_mix/F')
  _pho3_pt_mix = outtree.Branch('pho3_pt_mix',pho3_pt_mix,'pho3_pt_mix/F')
  _pho4_pt_mix = outtree.Branch('pho4_pt_mix',pho4_pt_mix,'pho4_pt_mix/F')
  _pho1_eta_mix = outtree.Branch('pho1_eta_mix',pho1_eta_mix,'pho1_eta_mix/F')
  _pho2_eta_mix = outtree.Branch('pho2_eta_mix',pho2_eta_mix,'pho2_eta_mix/F')
  _pho3_eta_mix = outtree.Branch('pho3_eta_mix',pho3_eta_mix,'pho3_eta_mix/F')
  _pho4_eta_mix = outtree.Branch('pho4_eta_mix',pho4_eta_mix,'pho4_eta_mix/F')
  _pho1_electronveto_mix = outtree.Branch('pho1_electronveto_mix',pho1_electronveto_mix,'pho1_electronveto_mix/F')
  _pho2_electronveto_mix = outtree.Branch('pho2_electronveto_mix',pho2_electronveto_mix,'pho2_electronveto_mix/F')
  _pho3_electronveto_mix = outtree.Branch('pho3_electronveto_mix',pho3_electronveto_mix,'pho3_electronveto_mix/F')
  _pho4_electronveto_mix = outtree.Branch('pho4_electronveto_mix',pho4_electronveto_mix,'pho4_electronveto_mix/F')
  _pho1_MVA_mix = outtree.Branch('pho1_MVA_mix',pho1_MVA_mix,'pho1_MVA_mix/F')
  _pho2_MVA_mix = outtree.Branch('pho2_MVA_mix',pho2_MVA_mix,'pho2_MVA_mix/F')
  _pho3_MVA_mix = outtree.Branch('pho3_MVA_mix',pho3_MVA_mix,'pho3_MVA_mix/F')
  _pho4_MVA_mix = outtree.Branch('pho4_MVA_mix',pho4_MVA_mix,'pho4_MVA_mix/F')
  _pho_minMVA_mix = outtree.Branch('pho_minMVA_mix',pho_minMVA_mix,'pho_minMVA_mix/F')
  _pho_maxMVA_mix = outtree.Branch('pho_maxMVA_mix',pho_maxMVA_mix,'pho_maxMVA_mix/F')
  _pho12_DR_mix = outtree.Branch('pho12_DR_mix',pho12_DR_mix,'pho12_DR_mix/F')
  _pho13_DR_mix = outtree.Branch('pho13_DR_mix',pho13_DR_mix,'pho13_DR_mix/F')
  _pho14_DR_mix = outtree.Branch('pho14_DR_mix',pho14_DR_mix,'pho14_DR_mix/F')
  _pho23_DR_mix = outtree.Branch('pho23_DR_mix',pho23_DR_mix,'pho23_DR_mix/F')
  _pho24_DR_mix = outtree.Branch('pho24_DR_mix',pho24_DR_mix,'pho24_DR_mix/F')
  _pho34_DR_mix = outtree.Branch('pho34_DR_mix',pho34_DR_mix,'pho34_DR_mix/F')
  _pho12_M_mix = outtree.Branch('pho12_M_mix',pho12_M_mix,'pho12_M_mix/F')
  _pho13_M_mix = outtree.Branch('pho13_M_mix',pho13_M_mix,'pho13_M_mix/F')
  _pho14_M_mix = outtree.Branch('pho14_M_mix',pho14_M_mix,'pho14_M_mix/F')
  _pho23_M_mix = outtree.Branch('pho23_M_mix',pho23_M_mix,'pho23_M_mix/F')
  _pho24_M_mix = outtree.Branch('pho24_M_mix',pho24_M_mix,'pho24_M_mix/F')
  _pho34_M_mix = outtree.Branch('pho34_M_mix',pho34_M_mix,'pho34_M_mix/F')
  _isPresel = outtree.Branch('isPresel',isPresel,'isPresel/I')
  _a1_mass_mix = outtree.Branch('a1_mass_mix',a1_mass_mix,'a1_mass_mix/F')
  _a2_mass_mix = outtree.Branch('a2_mass_mix',a2_mass_mix,'a2_mass_mix/F')
  _avg_a_mass_mix = outtree.Branch('avg_a_mass_mix',avg_a_mass_mix,'avg_a_mass_mix/F')
  _a1_Pt_mix = outtree.Branch('a1_Pt_mix',a1_Pt_mix,'a1_Pt_mix/F')
  _a2_Pt_mix = outtree.Branch('a2_Pt_mix',a2_Pt_mix,'a2_Pt_mix/F')
  _a1_Eta_mix = outtree.Branch('a1_Eta_mix',a1_Eta_mix,'a1_Eta_mix/F')
  _a2_Eta_mix = outtree.Branch('a2_Eta_mix',a2_Eta_mix,'a2_Eta_mix/F')
  _a1_Phi_mix = outtree.Branch('a1_Phi_mix',a1_Phi_mix,'a1_Phi_mix/F')
  _a2_Phi_mix = outtree.Branch('a2_Phi_mix',a2_Phi_mix,'a2_Phi_mix/F')
  _a1_Energy_mix = outtree.Branch('a1_Energy_mix',a1_Energy_mix,'a1_Energy_mix/F')
  _a2_Energy_mix = outtree.Branch('a2_Energy_mix',a2_Energy_mix,'a2_Energy_mix/F')
  _a1_DR_mix = outtree.Branch('a1_DR_mix',a1_DR_mix,'a1_DR_mix/F')
  _a2_DR_mix = outtree.Branch('a2_DR_mix',a2_DR_mix,'a2_DR_mix/F')
  _a1_a2_DR_mix = outtree.Branch('a1_a2_DR_mix',a1_a2_DR_mix,'a1_a2_DR_mix/F')
  _a1_iPho1_mix = outtree.Branch('a1_iPho1_mix',a1_iPho1_mix,'a1_iPho1_mix/F')
  _a1_iPho2_mix = outtree.Branch('a1_iPho2_mix',a1_iPho2_mix,'a1_iPho2_mix/F')
  _a2_iPho1_mix = outtree.Branch('a2_iPho1_mix',a2_iPho1_mix,'a2_iPho1_mix/F')
  _a2_iPho2_mix = outtree.Branch('a2_iPho2_mix',a2_iPho2_mix,'a2_iPho2_mix/F')
  _a1_PtOverMass_mix = outtree.Branch('a1_PtOverMass_mix',a1_PtOverMass_mix,'a1_PtOverMass_mix/F')
  _a2_PtOverMass_mix = outtree.Branch('a2_PtOverMass_mix',a2_PtOverMass_mix,'a2_PtOverMass_mix/F')
  _CTStarCS_mix = outtree.Branch('CTStarCS_mix',CTStarCS_mix,'CTStarCS_mix/F')
  _CT_a1Pho1_mix = outtree.Branch('CT_a1Pho1_mix',CT_a1Pho1_mix,'CT_a1Pho1_mix/F')
  _CT_a2Pho1_mix = outtree.Branch('CT_a2Pho1_mix',CT_a2Pho1_mix,'CT_a2Pho1_mix/F')
  _a1_Pho1PtOvera1Mass_mix = outtree.Branch('a1_Pho1PtOvera1Mass_mix',a1_Pho1PtOvera1Mass_mix,'a1_Pho1PtOvera1Mass_mix/F')
  _a1_Pho2PtOvera1Mass_mix = outtree.Branch('a1_Pho2PtOvera1Mass_mix',a1_Pho2PtOvera1Mass_mix,'a1_Pho2PtOvera1Mass_mix/F')
  _a2_Pho1PtOvera2Mass_mix = outtree.Branch('a2_Pho1PtOvera2Mass_mix',a2_Pho1PtOvera2Mass_mix,'a2_Pho1PtOvera2Mass_mix/F')
  _a2_Pho2PtOvera2Mass_mix = outtree.Branch('a2_Pho2PtOvera2Mass_mix',a2_Pho2PtOvera2Mass_mix,'a2_Pho2PtOvera2Mass_mix/F')
  _tp_mass_mix = outtree.Branch('tp_mass_mix',tp_mass_mix,'tp_mass_mix/F')
  _tp_pt_mix = outtree.Branch('tp_pt_mix',tp_pt_mix,'tp_pt_mix/F')
  _tp_eta_mix = outtree.Branch('tp_eta_mix',tp_eta_mix,'tp_eta_mix/F')
  _tp_phi_mix = outtree.Branch('tp_phi_mix',tp_phi_mix,'tp_phi_mix/F')

  treeSkimmer = SkimmedTreeTools()
  otree = treeSkimmer.MakeSkimmedTree()


  for b in itree.GetListOfBranches():
    b.SetStatus(0)

  otree = itree.CloneTree(0)
  # BUT keep all branches "active" in the old tree
  itree.SetBranchStatus('*'  ,1)


  # prepare for the loop ...
  eventsToRun = itree.GetEntries()

  # print " itree.GetListOfBranches = ", itree.GetListOfBranches

  # and loop
  for evt in range(0, eventsToRun):
  # for evt in range(0,100):

    if evt%1000 == 0: print "## Analyzing event ", evt
    tempPhos = []
    itree.GetEntry(evt)

    # treeSkimmer.FillEvent(itree)

    dp1_p1i = itree.dp1_p1i
    dp1_p2i = itree.dp1_p2i
    dp2_p1i = itree.dp2_p1i
    dp2_p2i = itree.dp2_p2i

    # print "original photon mva "
    # print itree.pho1_MVA, "  ", itree.pho2_MVA, "  ", itree.pho3_MVA, "  ", itree.pho4_MVA
    if evt == eventsToRun :
      itree.GetEntry(0)
    else :
      itree.GetEntry(evt)
      # print "evt", evt

    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]
    for branch in ObjList:
      nameToSearch1 = "pho" + str(int(dp1_p1i)+1) + "_"
      if branch.startswith(nameToSearch1) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)


    if evt == eventsToRun :
      itree.GetEntry(0)
    else :
      itree.GetEntry(evt+1)

    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]
    for branch in ObjList:
      nameToSearch1 = "pho" + str(int(dp1_p2i)+1) + "_"
      if branch.startswith(nameToSearch1) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)


    if evt == eventsToRun :
      itree.GetEntry(1)
    elif evt == (eventsToRun-1) :
      itree.GetEntry(0)
    else :
      itree.GetEntry(evt+2)

    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]
    for branch in ObjList:
      nameToSearch1 = "pho" + str(int(dp2_p1i)+1) + "_"
      if branch.startswith(nameToSearch1) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)


    if evt == eventsToRun :
      itree.GetEntry(2)
    elif evt == (eventsToRun-1) :
      itree.GetEntry(1)
    elif evt == (eventsToRun-2) :
      itree.GetEntry(0)
    else :
      itree.GetEntry(evt+3)

    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]
    for branch in ObjList:
      nameToSearch1 = "pho" + str(int(dp2_p2i)+1) + "_"
      if branch.startswith(nameToSearch1) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)


    order_photons = {
          1: treeSkimmer.pho1_pt,
          2: treeSkimmer.pho2_pt,
          3: treeSkimmer.pho3_pt,
          4: treeSkimmer.pho4_pt
          }
    # print "treeSkimmer.pho1_pt ", treeSkimmer.pho1_pt
    # print "treeSkimmer.pho2_pt ", treeSkimmer.pho2_pt
    # print "treeSkimmer.pho3_pt ", treeSkimmer.pho3_pt
    # print "treeSkimmer.pho4_pt ", treeSkimmer.pho4_pt
    sorted_order_photons = sorted(order_photons.items(), key=operator.itemgetter(1))
    sorted_order_photons.reverse()   # from high to low


    sPhos = []
    sPhos_mva = []
    sPhos_full5x5_r9 = []
    sPhos_chHadIso = []
    sPhos_HoE = []
    sPhos_SCEta = []
    sPhos_PSV = []
    sPhos_EV = []
    pho1_vec = []
    pho2_vec = []
    pho3_vec = []
    pho4_vec = []

    #for iphoton in range(0, 4):  # 4 photons
    for iphoton in sorted_order_photons:
      p4 = ROOT.TLorentzVector(0,0,0,0)
      name_pt  = "pho" + str( int(iphoton [0] ) ) + "_pt"
      name_eta = "pho" + str( int(iphoton [0] ) ) + "_eta"
      name_phi = "pho" + str( int(iphoton [0] ) ) + "_phi"
      name_mva = "pho" + str( int(iphoton [0] ) ) + "_MVA"
      name_full5x5_r9 = "pho" + str( int(iphoton [0] ) ) + "_full5x5_r9"
      name_chHadIso = "pho" + str(int(iphoton [0])) + "_ChHadIso"
      name_HoE = "pho" + str(int(iphoton [0])) + "_HoE"
      name_SCEta = "pho" + str(int(iphoton [0])) + "_SC_eta"
      name_PSV = "pho" + str(int(iphoton [0])) + "_pixelseed"
      name_EV = "pho" + str(int(iphoton [0])) + "_electronveto"

      p4.SetPtEtaPhiM( getattr(treeSkimmer, name_pt),  getattr(treeSkimmer, name_eta),    getattr(treeSkimmer, name_phi) , 0 )
      sPhos.append(p4)
      sPhos_mva.append(getattr(treeSkimmer, name_mva))
      sPhos_full5x5_r9.append(getattr(treeSkimmer, name_full5x5_r9))
      sPhos_chHadIso.append(getattr(treeSkimmer, name_chHadIso))
      sPhos_HoE.append(getattr(treeSkimmer, name_HoE))
      sPhos_SCEta.append(getattr(treeSkimmer, name_SCEta))
      sPhos_PSV.append(getattr(treeSkimmer, name_PSV))
      sPhos_EV.append(getattr(treeSkimmer,name_EV))

    pho1_vec.append(sPhos[0])
    pho1_vec.append(sPhos_full5x5_r9[0])
    pho1_vec.append(sPhos_chHadIso[0])
    pho1_vec.append(sPhos_HoE[0])
    pho1_vec.append(sPhos_SCEta[0])
    pho1_vec.append(sPhos_PSV[0])

    pho2_vec.append(sPhos[1])
    pho2_vec.append(sPhos_full5x5_r9[1])
    pho2_vec.append(sPhos_chHadIso[1])
    pho2_vec.append(sPhos_HoE[1])
    pho2_vec.append(sPhos_SCEta[1])
    pho2_vec.append(sPhos_PSV[1])

    pho3_vec.append(sPhos[2]) ## 0
    pho3_vec.append(sPhos_full5x5_r9[2]) ## 1
    pho3_vec.append(sPhos_chHadIso[2]) ## 2
    pho3_vec.append(sPhos_HoE[2]) ## 3
    pho3_vec.append(sPhos_SCEta[2]) ## 4
    pho3_vec.append(sPhos_PSV[2]) ## 5

    pho4_vec.append(sPhos[3])
    pho4_vec.append(sPhos_full5x5_r9[3])
    pho4_vec.append(sPhos_chHadIso[3])
    pho4_vec.append(sPhos_HoE[3])
    pho4_vec.append(sPhos_SCEta[3])
    pho4_vec.append(sPhos_PSV[3])


    Pho12_presel = Preselection(pho1_vec, pho2_vec)
    Pho13_presel = Preselection(pho1_vec, pho3_vec)
    Pho14_presel = Preselection(pho1_vec, pho4_vec)
    Pho23_presel = Preselection(pho2_vec, pho3_vec)
    Pho24_presel = Preselection(pho2_vec, pho4_vec)
    Pho34_presel = Preselection(pho3_vec, pho4_vec)

    isPresel_res =  Pho12_presel or Pho13_presel or Pho14_presel or Pho23_presel or Pho24_presel or Pho34_presel

    # print "pt ", sPhos[0].Pt()
    # print sPhos[1].Pt()
    # print sPhos[2].Pt()
    # print sPhos[3].Pt()
    # print sPhos_mva[0], "  ", sPhos_mva[1], "  ", sPhos_mva[2], "  ", sPhos_mva[3]

    pho1_pt_mix[0] = sPhos[0].Pt()
    pho2_pt_mix[0] = sPhos[1].Pt()
    pho3_pt_mix[0] = sPhos[2].Pt()
    pho4_pt_mix[0] = sPhos[3].Pt()
    pho1_eta_mix[0] = sPhos[0].Eta()
    pho2_eta_mix[0] = sPhos[1].Eta()
    pho3_eta_mix[0] = sPhos[2].Eta()
    pho4_eta_mix[0] = sPhos[3].Eta()
    pho1_electronveto_mix[0] = sPhos_EV[0]
    pho2_electronveto_mix[0] = sPhos_EV[1]
    pho3_electronveto_mix[0] = sPhos_EV[2]
    pho4_electronveto_mix[0] = sPhos_EV[3]
    pho1_MVA_mix[0] = sPhos_mva[0]
    pho2_MVA_mix[0] = sPhos_mva[1]
    pho3_MVA_mix[0] = sPhos_mva[2]
    pho4_MVA_mix[0] = sPhos_mva[3]
    pho_minMVA_mix[0] = min(sPhos_mva)
    pho_maxMVA_mix[0] = max(sPhos_mva)
    pho12_DR_mix[0] = sPhos[0].DeltaR(sPhos[1])
    pho13_DR_mix[0] = sPhos[0].DeltaR(sPhos[2])
    pho14_DR_mix[0] = sPhos[0].DeltaR(sPhos[3])
    pho23_DR_mix[0] = sPhos[1].DeltaR(sPhos[2])
    pho24_DR_mix[0] = sPhos[1].DeltaR(sPhos[3])
    pho34_DR_mix[0] = sPhos[2].DeltaR(sPhos[3])
    pho12_M_mix[0] = (sPhos[0]+sPhos[1]).M()
    pho13_M_mix[0] = (sPhos[0]+sPhos[2]).M()
    pho14_M_mix[0] = (sPhos[0]+sPhos[3]).M()
    pho23_M_mix[0] = (sPhos[1]+sPhos[2]).M()
    pho24_M_mix[0] = (sPhos[1]+sPhos[3]).M()
    pho34_M_mix[0] = (sPhos[2]+sPhos[3]).M()
    isPresel[0] = isPresel_res


    pairedDiphos = treeSkimmer.MakePairing(sPhos)
    PP1 = pairedDiphos[0][0]
    PP2 = pairedDiphos[1][0]

    a1_iPho1_mix[0] = pairedDiphos[0][2]
    a1_iPho2_mix[0] = pairedDiphos[0][4]
    a2_iPho1_mix[0] = pairedDiphos[1][2]
    a2_iPho2_mix[0] = pairedDiphos[1][4]

    a1_DR_mix[0] = pairedDiphos[0][1].DeltaR(pairedDiphos[0][3])
    a2_DR_mix[0] = pairedDiphos[1][1].DeltaR(pairedDiphos[1][3])

    a1_Pt_mix[0] = PP1.Pt()
    a2_Pt_mix[0] = PP2.Pt()
    a1_Eta_mix[0] = PP1.Eta()
    a2_Eta_mix[0] = PP2.Eta()
    a1_Phi_mix[0] = PP1.Phi()
    a2_Phi_mix[0] = PP2.Phi()
    a1_Energy_mix[0] = PP1.E()
    a2_Energy_mix[0] = PP2.E()

    a1_mass_mix[0] = PP1.M()
    a2_mass_mix[0] = PP2.M()
    avg_a_mass_mix[0] = (PP1.M() + PP2.M())/2

    a1_a2_DR_mix[0] = PP1.DeltaR(PP2)
    a1_PtOverMass_mix[0] = PP1.Pt()/PP1.M()
    a2_PtOverMass_mix[0] = PP2.Pt()/PP2.M()
    a1_Pho1PtOvera1Mass_mix[0] = pairedDiphos[0][1].Pt()/PP1.M()
    a1_Pho2PtOvera1Mass_mix[0] = pairedDiphos[0][3].Pt()/PP1.M()
    a2_Pho1PtOvera2Mass_mix[0] = pairedDiphos[1][1].Pt()/PP2.M()
    a2_Pho2PtOvera2Mass_mix[0] = pairedDiphos[1][3].Pt()/PP2.M()
    CTStarCS_mix[0] = abs(getCosThetaStar_CS())
    CT_a1Pho1_mix[0] = abs(CosThetaAngles()[0])
    CT_a2Pho1_mix[0] = abs(CosThetaAngles()[1])


    Pgggg = sPhos[0] + sPhos[1] + sPhos[2] + sPhos[3]
    tp_mass_mix[0] = Pgggg.M()
    tp_pt_mix[0] = Pgggg.Pt()
    tp_eta_mix[0] = Pgggg.Eta()
    tp_phi_mix[0] = Pgggg.Phi()


    outtree.Fill()

  outRoot.cd()
  outtree.Write()
  outRoot.Close()
