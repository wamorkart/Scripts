#!/usr/bin/python
import numpy as n
from ROOT import *
import sys, getopt
from array import array

from genAnalyzer_tools import *

def main(argv):
   inputfiles = '/afs/cern.ch/work/t/twamorka/ThesisAnalysis/CMSSW_10_5_0/src/flashgg/output.root'
   outputfile = 'test.root'
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputFiles=","outputFile="])
   except getopt.GetoptError:
      print 'H4GTreeAnalyzer.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile1,inputfile2,inputfile3...> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--inputFiles"):
         inputfiles = arg
      elif opt in ("-o", "--outputFile"):
         outputfile = arg

   listOfFiles = inputfiles.split(",")
   print "Number of input files: ", len(listOfFiles)

   tree = TChain("FlashggH4GCandidate/genTree")
   for f in listOfFiles:
       print "\t Adding file:", f
       tree.AddFile(f)
   print "Total number of events to be analyzed:", tree.GetEntries()

   outRoot = TFile(outputfile, "RECREATE")

   GenMaker = GenTools()
   outTree = GenMaker.MakeGenTree()

   evtCounter = 0
   GenMaker.totevs[0] = tree.GetEntries()
   #Tree Loop:
   print tree.GetEntries()
   for evt in range(0, tree.GetEntries()):
       if evt%1000 == 0: print "## Analyzing event ", evt
       tree.GetEntry(evt)
       Genphos = []
       number = 0
       for g in range(0,tree.genPhoton_p4.size()):       ## loop over GEN photons
           P4 = TLorentzVector(0,0,0,0)
           P4.SetPtEtaPhiE( tree.genPhoton_p4[g].pt(), tree.genPhoton_p4[g].eta(), tree.genPhoton_p4[g].phi(), tree.genPhoton_p4[g].e())
           Genphos.append(P4)
           minDR = 999

       Photon1 = TLorentzVector(0,0,0,0)
       Photon2 = TLorentzVector(0,0,0,0)
       Photon3 = TLorentzVector(0,0,0,0)
       Photon4 = TLorentzVector(0,0,0,0)

       Photon1 = Genphos[0] # photons 1,2 come from a1; 3,4 come from a2
       Photon2 = Genphos[1]
       Photon3 = Genphos[2]
       Photon4 = Genphos[3]

       GenMaker.gen12_mass[0] = (Photon1+Photon2).M()
       GenMaker.gen13_mass[0] = (Photon1+Photon3).M()
       GenMaker.gen14_mass[0] = (Photon1+Photon4).M()
       GenMaker.gen23_mass[0] = (Photon2+Photon3).M()
       GenMaker.gen24_mass[0] = (Photon2+Photon4).M()
       GenMaker.gen34_mass[0] = (Photon3+Photon4).M()

       GenMaker.gen12dr[0] = Photon1.DeltaR(Photon2)
       GenMaker.gen13dr[0] = Photon1.DeltaR(Photon3)
       GenMaker.gen14dr[0] = Photon1.DeltaR(Photon4)
       GenMaker.gen23dr[0] = Photon2.DeltaR(Photon3)
       GenMaker.gen24dr[0] = Photon2.DeltaR(Photon4)
       GenMaker.gen34dr[0] = Photon3.DeltaR(Photon4)

       GenMaker.gen_mindr[0] = min(Photon1.DeltaR(Photon2),Photon1.DeltaR(Photon3),Photon1.DeltaR(Photon4),Photon2.DeltaR(Photon3),Photon2.DeltaR(Photon4),Photon3.DeltaR(Photon4))
       GenMaker.gen_maxdr[0] = max(Photon1.DeltaR(Photon2),Photon1.DeltaR(Photon3),Photon1.DeltaR(Photon4),Photon2.DeltaR(Photon3),Photon2.DeltaR(Photon4),Photon3.DeltaR(Photon4))

       GenMaker.tp_mass[0] = (Photon1+Photon2+Photon3+Photon4).M()

       Genphos.sort(key=lambda x: x.Pt(), reverse=True) # now sort in pt order and save kinematics

       gen1 = Genphos[0]
       gen2 = Genphos[1]
       gen3 = Genphos[2]
       gen4 = Genphos[3]

       GenMaker.gen1_pt[0] = gen1.Pt()
       GenMaker.gen2_pt[0] = gen2.Pt()
       GenMaker.gen3_pt[0] = gen3.Pt()
       GenMaker.gen4_pt[0] = gen4.Pt()
       GenMaker.gen1_eta[0] = gen1.Eta()
       GenMaker.gen2_eta[0] = gen2.Eta()
       GenMaker.gen3_eta[0] = gen3.Eta()
       GenMaker.gen4_eta[0] = gen4.Eta()
       GenMaker.gen1_phi[0] = gen1.Phi()
       GenMaker.gen2_phi[0] = gen2.Phi()
       GenMaker.gen3_phi[0] = gen3.Phi()
       GenMaker.gen4_phi[0] = gen4.Phi()
       GenMaker.gen1_energy[0] = gen1.Energy()
       GenMaker.gen2_energy[0] = gen2.Energy()
       GenMaker.gen3_energy[0] = gen3.Energy()
       GenMaker.gen4_energy[0] = gen4.Energy()


       outTree.Fill()

   evtCounter += 1

   outRoot.cd()
   outTree.Write()

   outRoot.Close()


if __name__ == "__main__":
   main(sys.argv[1:])
