import ROOT
from array import array
from array import array
import argparse

parser =  argparse.ArgumentParser(description='Apply Pairing BDT')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)
parser.add_argument('-i', '--infile', dest='infile', required=True, type=str)
parser.add_argument('-iD', '--inDir', dest='inDir', required=True, type=str)
parser.add_argument('-t', '--intree', dest='intree', required=True, type=str)
parser.add_argument('-oD', '--outDir', dest='outDir', required=True, type=str)
opt = parser.parse_args()
Mass = opt.mass
inFile = opt.infile
inDir = opt.inDir
inTree = opt.intree
outDir = opt.outDir
print "Mass: ", Mass
print "inFile: ", str(inDir)+str(inFile)
print "inTree: ",inTree
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

def MakePairing(Phos):
      minDM = 1000000
      P1 = 0
      iP1 = -99
      P2 = 0
      iP2 = -99
      P3 = 0
      iP3 = -99
      P4 = 0
      iP4 = -99
      Dipho1 = 0
      Dipho2 = 0
      for i1,p1 in enumerate(Phos):
         for i2,p2 in enumerate(Phos):
            if i2 <= i1: continue
            for i3,p3 in enumerate(Phos):
               if i3 == i2 or i3 == i1: continue
               for i4,p4 in enumerate(Phos):
                  if i4 <= i3: continue
                  if i4==i1 or i4==i2: continue
                  dipho1 = p1+p2
                  dipho2 = p3+p4
                  #Mass = dipho.M()
                  deltaM = abs(dipho1.M() - dipho2.M())
                  if deltaM < minDM:
                     minDM = deltaM
                     P1 = p1
                     iP1 = i1
                     P2 = p2
                     iP2 = i2
                     P3 = p3
                     iP3 = i3
                     P4 = p4
                     iP4 = i4
                     Dipho1 = dipho1 if ((p1 + p2).Pt() > (p3 + p4).Pt()) else dipho2
                     Dipho2 = dipho2 if ((p1 + p2).Pt() > (p3 + p4).Pt()) else dipho1
                     # Dipho1 = dipho1 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho2
                     # Dipho2 = dipho2 if ((p1.Pt() + p2.Pt()) > (p3.Pt() + p4.Pt())) else dipho1
      arr = [[Dipho1, P1, iP1, P2, iP2], [Dipho2, P3, iP3, P4, iP4]]
      return arr
#infilename = '/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/signal_m_'+str(Mass)+'.root'
infilename = str(inDir)+str(inFile)+'.root'
# infilename = '/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/'+str(inFile)+'.root'
print "Input file: ", infilename
infile = ROOT.TFile(infilename)
intree = infile.Get("photonCollTree")
intree2 = infile.Get("h4gCandidateDumper/trees/"+str(inTree))
outfile = ROOT.TFile(str(outDir)+str(inFile)+"_skim.root", "RECREATE")
outtree = intree2.CloneTree(0)
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



eventsToRun = intree.GetEntries()

for evt in range(0,eventsToRun):
    if evt%1000 == 0: print "## Analyzing event ", evt
    intree.GetEntry(evt)
    Phos = []
    Phos_id = []
    diphoton_pairing_indices_tmp = []
    diphoton_pairing_index = [[],[],[]]
    dipair_index_map = [[],[]]
    diphoton_pairing_indices = []
    mvaVal = []

    for p in range(0,int(intree.nphotons) ):
        p4 = ROOT.TLorentzVector(0,0,0,0)
        p4.SetPtEtaPhiM( intree.v_pho_pt[p], intree.v_pho_eta[p], intree.v_pho_phi[p], 0 )
        Phos.append(p4)
        Phos_id.append(p)
    Phos.sort(key=lambda x: x.Pt(), reverse=True)
    pairedDiphos = MakePairing(Phos)
    PP1 = pairedDiphos[0][0]
    PP2 = pairedDiphos[1][0]

    a1_iPho1[0] = pairedDiphos[0][2]
    a1_iPho2[0] = pairedDiphos[0][4]
    a2_iPho1[0] = pairedDiphos[1][2]
    a2_iPho2[0] = pairedDiphos[1][4]

    a1_mass[0] = PP1.M()
    a2_mass[0] = PP2.M()
    avg_a_mass[0] = (PP1.M()+PP2.M())/2
    a1_Pt[0] = PP1.Pt()
    a2_Pt[0] = PP2.Pt()
    # print a1.M(), " ", a2.M()
    # print a1.Pt()," ", a2.Pt()
    a1_Eta[0] = PP1.Eta()
    a2_Eta[0] = PP2.Eta()
    a1_Phi[0] = PP1.Phi()
    a2_Phi[0] = PP2.Phi()
    a1_Energy[0] = PP1.E()
    a2_Energy[0] = PP2.E()
    a1_DR[0] = pairedDiphos[0][1].DeltaR(pairedDiphos[0][3])
    a2_DR[0] = pairedDiphos[1][1].DeltaR(pairedDiphos[1][3])
    a1_a2_DR[0] = PP1.DeltaR(PP2)

    a1_PtOverMass[0] = PP1.Pt()/PP1.M()
    a2_PtOverMass[0] = PP2.Pt()/PP2.M()
    a1_Pho1PtOvera1Mass[0] = pairedDiphos[0][1].Pt()/PP1.M()
    a1_Pho2PtOvera1Mass[0] = pairedDiphos[0][3].Pt()/PP1.M()
    a2_Pho1PtOvera2Mass[0] = pairedDiphos[1][1].Pt()/PP2.M()
    a2_Pho2PtOvera2Mass[0] = pairedDiphos[1][3].Pt()/PP2.M()
    CTStarCS[0] =  abs(getCosThetaStar_CS())
    CT_a1Pho1[0] = abs(CosThetaAngles()[0])
    CT_a2Pho1[0] = abs(CosThetaAngles()[1])

    intree2.GetEntry(evt)
    outtree.Fill()
outfile.cd()
outtree.Write()
outfile.Close()
