#!/usr/bin/python
import numpy as n
import ROOT
# from ROOT import *
import sys, getopt
from array import array
from H4GSkimTools import *
from optparse import OptionParser
import operator
import argparse

if __name__ == '__main__':


  # parser = OptionParser()
  parser = argparse.ArgumentParser(description='Mixing with BDT pairing')
  parser.add_argument(   "-i", "--inputFile",   dest="inputFile",    default="input.root",       type=str,  help="Input file" )
  parser.add_argument(   "-o", "--outputFile",  dest="outputFile",   default="output.root",      type=str,  help="Output file")
  parser.add_argument(   "-t", "--tree",  dest="tree",   default="tree",      type=str,  help="tree")
  parser.add_argument(   "-w", "--weight", dest="weight", default="", type=str, help="weight")
  parser.add_argument(   "-m", "--Mass", dest="Mass", default="", type=str, help="mass")
  # parser.add_argument(   "-i1", "--i1",  dest="i1",   default=0,      type=int,  help="p1")
  # parser.add_argument(   "-i2", "--i2",  dest="i2",   default=0,      type=int,  help="p2")
  # parser.add_argument(   "-i3", "--i3",  dest="i3",   default=0,      type=int,  help="p3")
  # parser.add_argument(   "-i4", "--i4",  dest="i4",   default=0,      type=int,  help="p4")


  #/afs/cern.ch/user/a/amassiro/public/H4G/signal_m_50.root

  # (options, args) = parser.parse_args()
  options = parser.parse_args()

  # itree = ROOT.TChain("SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons")
  itree = ROOT.TChain(str(options.tree))
  itree.AddFile(options.inputFile)

  print "Total number of events to be analyzed:", itree.GetEntries()

  outRoot = ROOT.TFile(options.outputFile, "RECREATE")
  # outtree = itree.CloneTree(0)
  outtree = ROOT.TTree(options.tree,options.tree)

  def getCosThetaStar_CS():
      h_lor = a1 + a2
      h = ROOT.TLorentzVector(0,0,0,0)
      h.SetPxPyPzE(h_lor.Px(),h_lor.Py(),h_lor.Pz(),h_lor.E())
      a1_lor = a1
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
      Boosted_a1.SetPxPyPzE(a1.Px(),a1.Py(),a1.Pz(),a1.E())
      BoostedLeadingPhoton_a1 = ROOT.TLorentzVector(0,0,0,0)
      BoostedLeadingPhoton_a1.SetPxPyPzE(a1_pho1.Px(),a1_pho1.Py(),a1_pho1.Pz(),a1_pho1.E())
      helicityThetas.append( helicityCosTheta(Boosted_a1, BoostedLeadingPhoton_a1))

      Boosted_a2 = ROOT.TLorentzVector(0,0,0,0)
      Boosted_a2.SetPxPyPzE(a2.Px(),a2.Py(),a2.Pz(),a2.E())
      BoostedLeadingPhoton_a2 = ROOT.TLorentzVector(0,0,0,0)
      BoostedLeadingPhoton_a2.SetPxPyPzE(a2_pho1.Px(),a2_pho1.Py(),a2_pho1.Pz(),a2_pho1.E())
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


  reader = ROOT.TMVA.Reader()
  a1_E = array('f', [0])
  a1_pt = array('f', [0])
  a1_eta = array('f', [0])
  a1_dr = array('f', [0])
  dM1_gen1 = array('f', [0])
  a2_E = array('f', [0])
  a2_pt = array('f', [0])
  a2_eta = array('f', [0])
  a2_dr = array('f', [0])
  dM2_gen1 = array('f', [0])
  aPair_dr = array('f', [0])

  reader.AddVariable('dipho1_energy',a1_E)
  reader.AddVariable('dipho1_pt',a1_pt)
  reader.AddVariable('dipho1_eta',a1_eta)
  reader.AddVariable('dipho1_dR',a1_dr)
  reader.AddVariable('deltaM1_gen1',dM1_gen1)
  reader.AddVariable('dipho2_energy',a2_E)
  reader.AddVariable('dipho2_pt',a2_pt)
  reader.AddVariable('dipho2_eta',a2_eta)
  reader.AddVariable('dipho2_dR',a2_dr)
  reader.AddVariable('deltaM2_gen1',dM2_gen1)
  reader.AddVariable('dipair_dR',aPair_dr)

  # print "Weight file: ", str(weight)+str(Mass)+".weights.xml"
  # reader.BookMVA("BDT",str(weight)+str(Mass)+".weights.xml")
  reader.BookMVA("BDT",str(options.weight))

  pho1_pt = array('f', [0])
  pho2_pt = array('f', [0])
  pho3_pt = array('f', [0])
  pho4_pt = array('f', [0])
  pho1_eta = array('f', [0])
  pho2_eta = array('f', [0])
  pho3_eta = array('f', [0])
  pho4_eta = array('f', [0])
  pho1_electronveto = array('f',[0])
  pho2_electronveto = array('f',[0])
  pho3_electronveto = array('f',[0])
  pho4_electronveto = array('f',[0])
  pho1_MVA = array('f', [0])
  pho2_MVA = array('f', [0])
  pho3_MVA = array('f', [0])
  pho4_MVA = array('f', [0])
  pho_minMVA = array('f', [0])
  pho_maxMVA = array('f', [0])
  pho12_DR = array('f', [0])
  pho13_DR = array('f', [0])
  pho14_DR = array('f', [0])
  pho23_DR = array('f', [0])
  pho24_DR = array('f', [0])
  pho34_DR = array('f', [0])
  pho12_M = array('f', [0])
  pho13_M = array('f', [0])
  pho14_M = array('f', [0])
  pho23_M = array('f', [0])
  pho24_M = array('f', [0])
  isPresel = array('i',[0])
  pho34_M = array('f', [0])
  pairMVAscore = array('f',[0])
  a1_mass = array('f',[0])
  a2_mass = array('f',[0])
  avg_a_mass = array('f',[0])
  a1_Pt = array('f',[0])
  a2_Pt = array('f',[0])
  a1_Eta = array('f',[0])
  a2_Eta = array('f',[0])
  a1_Phi = array('f',[0])
  a2_Phi = array('f',[0])
  a1_Energy = array('f',[0])
  a2_Energy = array('f',[0])
  a1_DR = array('f',[0])
  a2_DR = array('f',[0])
  a1_a2_DR = array('f',[0])
  a1_iPho1 = array('f',[0])
  a1_iPho2 = array('f',[0])
  a2_iPho1 = array('f',[0])
  a2_iPho2 = array('f',[0])
  a1_PtOverMass = array('f',[0])
  a2_PtOverMass = array('f',[0])
  a1_Pho1PtOvera1Mass = array('f',[0])
  a1_Pho2PtOvera1Mass = array('f',[0])
  a2_Pho1PtOvera2Mass = array('f',[0])
  a2_Pho2PtOvera2Mass = array('f',[0])
  CTStarCS = array('f',[0])
  CT_a1Pho1 = array('f',[0])
  CT_a2Pho1 = array('f',[0])
  tp_mass  = array('f',[0])
  tp_pt  = array('f',[0])
  tp_eta = array('f',[0])
  tp_phi  = array('f',[0])

  _pho1_pt = outtree.Branch('pho1_pt',pho1_pt,'pho1_pt/F')
  _pho2_pt = outtree.Branch('pho2_pt',pho2_pt,'pho2_pt/F')
  _pho3_pt = outtree.Branch('pho3_pt',pho3_pt,'pho3_pt/F')
  _pho4_pt = outtree.Branch('pho4_pt',pho4_pt,'pho4_pt/F')
  _pho1_eta = outtree.Branch('pho1_eta',pho1_eta,'pho1_eta/F')
  _pho2_eta = outtree.Branch('pho2_eta',pho2_eta,'pho2_eta/F')
  _pho3_eta = outtree.Branch('pho3_eta',pho3_eta,'pho3_eta/F')
  _pho4_eta = outtree.Branch('pho4_eta',pho4_eta,'pho4_eta/F')
  _pho1_electronveto = outtree.Branch('pho1_electronveto',pho1_electronveto,'pho1_electronveto/F')
  _pho2_electronveto = outtree.Branch('pho2_electronveto',pho2_electronveto,'pho2_electronveto/F')
  _pho3_electronveto = outtree.Branch('pho3_electronveto',pho3_electronveto,'pho3_electronveto/F')
  _pho4_electronveto = outtree.Branch('pho4_electronveto',pho4_electronveto,'pho4_electronveto/F')
  _pho1_MVA = outtree.Branch('pho1_MVA',pho1_MVA,'pho1_MVA/F')
  _pho2_MVA = outtree.Branch('pho2_MVA',pho2_MVA,'pho2_MVA/F')
  _pho3_MVA = outtree.Branch('pho3_MVA',pho3_MVA,'pho3_MVA/F')
  _pho4_MVA = outtree.Branch('pho4_MVA',pho4_MVA,'pho4_MVA/F')
  _pho_minMVA = outtree.Branch('pho_minMVA',pho_minMVA,'pho_minMVA/F')
  _pho_maxMVA = outtree.Branch('pho_maxMVA',pho_maxMVA,'pho_maxMVA/F')
  _pho12_DR = outtree.Branch('pho12_DR',pho12_DR,'pho12_DR/F')
  _pho13_DR = outtree.Branch('pho13_DR',pho13_DR,'pho13_DR/F')
  _pho14_DR = outtree.Branch('pho14_DR',pho14_DR,'pho14_DR/F')
  _pho23_DR = outtree.Branch('pho23_DR',pho23_DR,'pho23_DR/F')
  _pho24_DR = outtree.Branch('pho24_DR',pho24_DR,'pho24_DR/F')
  _pho34_DR = outtree.Branch('pho34_DR',pho34_DR,'pho34_DR/F')
  _pho12_M = outtree.Branch('pho12_M',pho12_M,'pho12_M/F')
  _pho13_M = outtree.Branch('pho13_M',pho13_M,'pho13_M/F')
  _pho14_M = outtree.Branch('pho14_M',pho14_M,'pho14_M/F')
  _pho23_M = outtree.Branch('pho23_M',pho23_M,'pho23_M/F')
  _pho24_M = outtree.Branch('pho24_M',pho24_M,'pho24_M/F')
  _pho34_M = outtree.Branch('pho34_M',pho34_M,'pho34_M/F')
  _isPresel = outtree.Branch('isPresel',isPresel,'isPresel/I')
  _pairMVAscore = outtree.Branch('pairMVAscore',pairMVAscore,'pairMVAscore/F')
  _a1_mass = outtree.Branch('a1_mass',a1_mass,'a1_mass/F')
  _a2_mass = outtree.Branch('a2_mass',a2_mass,'a2_mass/F')
  _avg_a_mass = outtree.Branch('avg_a_mass',avg_a_mass,'avg_a_mass/F')
  _a1_Pt = outtree.Branch('a1_Pt',a1_Pt,'a1_Pt/F')
  _a2_Pt = outtree.Branch('a2_Pt',a2_Pt,'a2_Pt/F')
  _a1_Eta = outtree.Branch('a1_Eta',a1_Eta,'a1_Eta/F')
  _a2_Eta = outtree.Branch('a2_Eta',a2_Eta,'a2_Eta/F')
  _a1_Phi = outtree.Branch('a1_Phi',a1_Phi,'a1_Phi/F')
  _a2_Phi = outtree.Branch('a2_Phi',a2_Phi,'a2_Phi/F')
  _a1_Energy = outtree.Branch('a1_Energy',a1_Energy,'a1_Energy/F')
  _a2_Energy = outtree.Branch('a2_Energy',a2_Energy,'a2_Energy/F')
  _a1_DR = outtree.Branch('a1_DR',a1_DR,'a1_DR/F')
  _a2_DR = outtree.Branch('a2_DR',a2_DR,'a2_DR/F')
  _a1_a2_DR = outtree.Branch('a1_a2_DR',a1_a2_DR,'a1_a2_DR/F')
  _a1_iPho1 = outtree.Branch('a1_iPho1',a1_iPho1,'a1_iPho1/F')
  _a1_iPho2 = outtree.Branch('a1_iPho2',a1_iPho2,'a1_iPho2/F')
  _a2_iPho1 = outtree.Branch('a2_iPho1',a2_iPho1,'a2_iPho1/F')
  _a2_iPho2 = outtree.Branch('a2_iPho2',a2_iPho2,'a2_iPho2/F')
  _a1_PtOverMass = outtree.Branch('a1_PtOverMass',a1_PtOverMass,'a1_PtOverMass/F')
  _a2_PtOverMass = outtree.Branch('a2_PtOverMass',a2_PtOverMass,'a2_PtOverMass/F')
  _CTStarCS = outtree.Branch('CTStarCS',CTStarCS,'CTStarCS/F')
  _CT_a1Pho1 = outtree.Branch('CT_a1Pho1',CT_a1Pho1,'CT_a1Pho1/F')
  _CT_a2Pho1 = outtree.Branch('CT_a2Pho1',CT_a2Pho1,'CT_a2Pho1/F')
  _a1_Pho1PtOvera1Mass = outtree.Branch('a1_Pho1PtOvera1Mass',a1_Pho1PtOvera1Mass,'a1_Pho1PtOvera1Mass/F')
  _a1_Pho2PtOvera1Mass = outtree.Branch('a1_Pho2PtOvera1Mass',a1_Pho2PtOvera1Mass,'a1_Pho2PtOvera1Mass/F')
  _a2_Pho1PtOvera2Mass = outtree.Branch('a2_Pho1PtOvera2Mass',a2_Pho1PtOvera2Mass,'a2_Pho1PtOvera2Mass/F')
  _a2_Pho2PtOvera2Mass = outtree.Branch('a2_Pho2PtOvera2Mass',a2_Pho2PtOvera2Mass,'a2_Pho2PtOvera2Mass/F')
  _tp_mass = outtree.Branch('tp_mass',tp_mass,'tp_mass/F')
  _tp_pt = outtree.Branch('tp_pt',tp_pt,'tp_pt/F')
  _tp_eta = outtree.Branch('tp_eta',tp_eta,'tp_eta/F')
  _tp_phi = outtree.Branch('tp_phi',tp_phi,'tp_phi/F')

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
        itree.GetEntry(evt+20)
        # print "evt1: ", evt
      # itree.GetEntry(evt+(options.i1))
      # print "evt1: ", evt+options.i1

    ObjList = [key.GetName() for key in  itree.GetListOfBranches()]
    for branch in ObjList:
      nameToSearch1 = "pho" + str(int(dp1_p1i)+1) + "_"
      if branch.startswith(nameToSearch1) :
        getattr(treeSkimmer, branch)[0] = getattr(itree, branch)


    if evt == eventsToRun :
      itree.GetEntry(0)
    else :
        itree.GetEntry(evt+21)
        # print "evt2: ", evt+1
      # itree.GetEntry(evt+options.i2)
      # print "evt2: ", evt+options.i2

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
        itree.GetEntry(evt+22)
        # print "evt2: ", evt+2
      # itree.GetEntry(evt+options.i3)
      # print "evt3: ", evt+options.i3

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
      itree.GetEntry(evt+23)
      # print "evt3: ", evt+3
      # itree.GetEntry(evt+options.i4)
      # print "evt4: ", evt+options.i4
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
    diphoton_pairing_indices_tmp = []
    diphoton_pairing_index = [[],[],[]]
    dipair_index_map = [[],[]]
    diphoton_pairing_indices = []
    mvaVal = []



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

    # isPresel_res =  Pho12_presel or Pho13_presel or Pho14_presel or Pho23_presel or Pho24_presel or Pho34_presel
    isPresel[0] = Pho12_presel or Pho13_presel or Pho14_presel or Pho23_presel or Pho24_presel or Pho34_presel
    # print "pt ", sPhos[0].Pt()
    # print sPhos[1].Pt()
    # print sPhos[2].Pt()
    # print sPhos[3].Pt()
    # print sPhos_mva[0], "  ", sPhos_mva[1], "  ", sPhos_mva[2], "  ", sPhos_mva[3]

    pho1_pt[0] = sPhos[0].Pt()
    pho2_pt[0] = sPhos[1].Pt()
    pho3_pt[0] = sPhos[2].Pt()
    pho4_pt[0] = sPhos[3].Pt()
    pho1_eta[0] = sPhos[0].Eta()
    pho2_eta[0] = sPhos[1].Eta()
    pho3_eta[0] = sPhos[2].Eta()
    pho4_eta[0] = sPhos[3].Eta()
    pho1_electronveto[0] = sPhos_EV[0]
    pho2_electronveto[0] = sPhos_EV[1]
    pho3_electronveto[0] = sPhos_EV[2]
    pho4_electronveto[0] = sPhos_EV[3]
    pho1_MVA[0] = sPhos_mva[0]
    pho2_MVA[0] = sPhos_mva[1]
    pho3_MVA[0] = sPhos_mva[2]
    pho4_MVA[0] = sPhos_mva[3]
    pho_minMVA[0] = min(sPhos_mva)
    pho_maxMVA[0] = max(sPhos_mva)
    pho12_DR[0] = sPhos[0].DeltaR(sPhos[1])
    pho13_DR[0] = sPhos[0].DeltaR(sPhos[2])
    pho14_DR[0] = sPhos[0].DeltaR(sPhos[3])
    pho23_DR[0] = sPhos[1].DeltaR(sPhos[2])
    pho24_DR[0] = sPhos[1].DeltaR(sPhos[3])
    pho34_DR[0] = sPhos[2].DeltaR(sPhos[3])
    pho12_M[0] = (sPhos[0]+sPhos[1]).M()
    pho13_M[0] = (sPhos[0]+sPhos[2]).M()
    pho14_M[0] = (sPhos[0]+sPhos[3]).M()
    pho23_M[0] = (sPhos[1]+sPhos[2]).M()
    pho24_M[0] = (sPhos[1]+sPhos[3]).M()
    pho34_M[0] = (sPhos[2]+sPhos[3]).M()
    # isPresel[0] = isPresel_res

    for i1 in range(0,len(sPhos)):
        pho1 = sPhos[i1]
        for i2 in range(0,len(sPhos)):
            if (i2<=i1): continue
            pho2 = sPhos[i2]
            for i3 in range(0,len(sPhos)):
                if (i3<=i2): continue
                if (i3==i1): continue
                pho3 = sPhos[i3]
                for i4 in range(0,len(sPhos)):
                    if (i4<=i3): continue
                    if (i4 == i1 or i4 == i2): continue
                    pho4 = sPhos[i4]
                    # print i1, i2, i3, i4

                    dipho1 = pho1 + pho2
                    dipho1_energy = dipho1.E()
                    dipho1_pt = dipho1.Pt()
                    dipho1_eta = dipho1.Eta()
                    dipho1_Phi = dipho1.Phi()
                    dipho1_dR = pho1.DeltaR(pho2)
                    dipho1_mass = dipho1.M()
                    deltaM1_gen1 = abs(dipho1.M()-float(options.Mass))
                    deltaM1_gen2 = abs(dipho1.M()-float(options.Mass))

                    dipho2 = pho3 + pho4
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho3.DeltaR(pho4)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-float(options.Mass))
                    deltaM2_gen2 = abs(dipho2.M()-float(options.Mass))

                    dipair_dR = dipho1.DeltaR(dipho2)

                    a1_E[0] = dipho1_energy
                    a1_pt[0] = dipho1_pt
                    a1_eta[0] = dipho1_eta
                    a1_dr[0] = dipho1_dR
                    dM1_gen1[0] = deltaM1_gen1
                    a2_E[0] = dipho2_energy
                    a2_pt[0] = dipho2_pt
                    a2_eta[0] = dipho2_eta
                    a2_dr[0] = dipho2_dR
                    dM2_gen1[0] = deltaM2_gen1
                    aPair_dr[0] = dipair_dR

                    mva_value = reader.EvaluateMVA( "BDT" )
                    mvaVal.append(mva_value)
                    dipair_index_map[0].append([i1,i2,i3,i4])
                    dipair_index_map[1].append(mva_value)

                    dipho1 = pho1 + pho3
                    dipho1_energy = dipho1.E()
                    dipho1_pt = dipho1.Pt()
                    dipho1_eta = dipho1.Eta()
                    dipho1_Phi = dipho1.Phi()
                    dipho1_dR = pho1.DeltaR(pho3)
                    dipho1_mass = dipho1.M()
                    deltaM1_gen1 = abs(dipho1.M()-float(options.Mass))
                    deltaM1_gen2 = abs(dipho1.M()-float(options.Mass))

                    dipho2 = pho2 + pho4
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho2.DeltaR(pho4)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-float(options.Mass))
                    deltaM2_gen2 = abs(dipho2.M()-float(options.Mass))

                    dipair_dR = dipho1.DeltaR(dipho2)

                    a1_E[0] = dipho1_energy
                    a1_pt[0] = dipho1_pt
                    a1_eta[0] = dipho1_eta
                    a1_dr[0] = dipho1_dR
                    dM1_gen1[0] = deltaM1_gen1
                    a2_E[0] = dipho2_energy
                    a2_pt[0] = dipho2_pt
                    a2_eta[0] = dipho2_eta
                    a2_dr[0] = dipho2_dR
                    dM2_gen1[0] = deltaM2_gen1
                    aPair_dr[0] = dipair_dR
                    mva_value = reader.EvaluateMVA( "BDT" )
                    mvaVal.append(mva_value)
                    dipair_index_map[0].append([i1,i3,i2,i4])
                    dipair_index_map[1].append(mva_value)

                    dipho1 = pho1 + pho4
                    dipho1_energy = dipho1.E()
                    dipho1_pt = dipho1.Pt()
                    dipho1_eta = dipho1.Eta()
                    dipho1_Phi = dipho1.Phi()
                    dipho1_dR = pho1.DeltaR(pho4)
                    dipho1_mass = dipho1.M()
                    deltaM1_gen1 = abs(dipho1.M()-float(options.Mass))
                    deltaM1_gen2 = abs(dipho1.M()-float(options.Mass))

                    dipho2 = pho2 + pho3
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho2.DeltaR(pho3)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-float(options.Mass))
                    deltaM2_gen2 = abs(dipho2.M()-float(options.Mass))

                    dipair_dR = dipho1.DeltaR(dipho2)

                    a1_E[0] = dipho1_energy
                    a1_pt[0] = dipho1_pt
                    a1_eta[0] = dipho1_eta
                    a1_dr[0] = dipho1_dR
                    dM1_gen1[0] = deltaM1_gen1
                    a2_E[0] = dipho2_energy
                    a2_pt[0] = dipho2_pt
                    a2_eta[0] = dipho2_eta
                    a2_dr[0] = dipho2_dR
                    dM2_gen1[0] = deltaM2_gen1
                    aPair_dr[0] = dipair_dR
                    mva_value = reader.EvaluateMVA( "BDT" )
                    # print "mva 3 ", mva_value
                    mvaVal.append(mva_value)
                    dipair_index_map[0].append([i1,i4,i2,i3])
                    dipair_index_map[1].append(mva_value)

    indexlist = dipair_index_map[0]
    mvalist = dipair_index_map[1]
    # print mvalist

    pairMVAscore[0] = max(mvalist)

    sPhos.sort(key=lambda x: x.Pt(), reverse=True)
    Pho1 = sPhos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][0]]
    Pho2 = sPhos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][1]]
    Pho3 = sPhos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][2]]
    Pho4 = sPhos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][3]]

    if (Pho1.Pt() > Pho2.Pt()):
        a1_pho1 = Pho1
        a1_pho2 = Pho2
        a1_ipho1 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][0]
        a1_ipho2 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][1]
    else:
        a1_pho1 = Pho2
        a1_pho2 = Pho1
        a1_ipho1 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][1]
        a1_ipho2 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][0]
    if (Pho3.Pt() > Pho4.Pt()):
        a2_pho1 = Pho3
        a2_pho2 = Pho4
        a2_ipho1 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][2]
        a2_ipho2 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][3]
    else:
        a2_pho1 = Pho4
        a2_pho2 = Pho3
        a2_ipho1 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][3]
        a2_ipho2 = indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][2]

    a1_temp = Pho1 + Pho2
    a2_temp = Pho3 + Pho4
    if (a1_temp.Pt() > a2_temp.Pt()):
             a1 = a1_temp
             a2 = a2_temp
    elif (a1_temp.Pt() < a2_temp.Pt()):
             a1 = a2_temp
             a2 = a1_temp

    a1_mass[0] = a1.M()
    a2_mass[0] = a2.M()
    avg_a_mass[0] = (a1.M()+a2.M())/2
    a1_Pt[0] = a1.Pt()
    a2_Pt[0] = a2.Pt()
    # print a1.M(), " ", a2.M()
    # print a1.Pt()," ", a2.Pt()
    a1_Eta[0] = a1.Eta()
    a2_Eta[0] = a2.Eta()
    a1_Phi[0] = a1.Phi()
    a2_Phi[0] = a2.Phi()
    a1_Energy[0] = a1.E()
    a2_Energy[0] = a2.E()
    a1_DR[0] = a1_pho1.DeltaR(a1_pho2)
    a2_DR[0] = a2_pho1.DeltaR(a2_pho2)
    a1_a2_DR[0] = a1.DeltaR(a2)
    a1_iPho1[0] = float(a1_ipho1)
    a1_iPho2[0] = float(a1_ipho2)
    a2_iPho1[0] = float(a2_ipho1)
    a2_iPho2[0] = float(a2_ipho2)
    a1_PtOverMass[0] = a1.Pt()/a1.M()
    a2_PtOverMass[0] = a2.Pt()/a2.M()
    a1_Pho1PtOvera1Mass[0] = a1_pho1.Pt()/a1.M()
    a1_Pho2PtOvera1Mass[0] = a1_pho2.Pt()/a1.M()
    a2_Pho1PtOvera2Mass[0] = a2_pho1.Pt()/a2.M()
    a2_Pho2PtOvera2Mass[0] = a2_pho2.Pt()/a2.M()
    CTStarCS[0] =  abs(getCosThetaStar_CS())
    CT_a1Pho1[0] = abs(CosThetaAngles()[0])
    CT_a2Pho1[0] = abs(CosThetaAngles()[1])

    Pgggg = sPhos[0] + sPhos[1] + sPhos[2] + sPhos[3]
    tp_mass[0] = Pgggg.M()
    tp_pt[0] = Pgggg.Pt()
    tp_eta[0] = Pgggg.Eta()
    tp_phi[0] = Pgggg.Phi()


    if (isPresel[0] == 1):
        outtree.Fill()

  outRoot.cd()
  outtree.Write()
  outRoot.Close()
