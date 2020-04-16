import ROOT
from array import array
from array import array
import argparse
import operator

parser =  argparse.ArgumentParser(description='Apply Pairing BDT')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)
parser.add_argument('-i', '--infile', dest='infile', required=True, type=str)
parser.add_argument('-iD', '--inDir', dest='inDir', required=True, type=str)
parser.add_argument('-t', '--intree', dest='intree', required=True, type=str)
parser.add_argument('-w', '--weight', dest='weight', required=True, type=str)
parser.add_argument('-oD', '--outDir', dest='outDir', required=True, type=str)
opt = parser.parse_args()
Mass = opt.mass
inFile = opt.infile
inDir = opt.inDir
inTree = opt.intree
weight = opt.weight
outDir = opt.outDir
print "Mass: ", Mass
print "inFile: ", str(inDir)+str(inFile)
print "inTree: ",inTree
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
reader.BookMVA("BDT",str(weight))

infilename = str(inDir)+str(inFile)+'.root'
print "Input file: ", infilename
infile = ROOT.TFile(infilename)
intree = infile.Get("photonCollTree")
intree2 = infile.Get("h4gCandidateDumper/trees/"+str(inTree))
# intree = infile.Get("h4gCandidateDumper/trees/"+str(inTree))
outfile = ROOT.TFile(str(outDir)+str(inFile)+"_skim.root", "RECREATE")
print "Output file: ", outfile
# outfile = ROOT.TFile(str(outDir)+"signal_m_"+str(Mass)+"_skim.root", "RECREATE")
outtree = intree2.CloneTree(0)
# outtree = ROOT.TTree(str(inTree),str(inTree))
# outtree = intree.CloneTree(0)
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



eventsToRun = intree.GetEntries()

print "eventsToRun", eventsToRun
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
    # print intree.nphotons
    # for p in range(0,int(intree.nphotons) ):
    # order_photons = {
         # 1: intree.pho1_pt,
         # 2: intree.pho2_pt,
         # 3: intree.pho3_pt,
         # 4: intree.pho4_pt
         # }
    # sorted_order_photons = sorted(order_photons.items(), key=operator.itemgetter(1))
    # sorted_order_photons.reverse()   # from high to low
    #
    # for iphoton in sorted_order_photons:
    #     p4 = ROOT.TLorentzVector(0,0,0,0)
    #     name_pt  = "pho" + str( int(iphoton [0] ) ) + "_pt"
    #     name_eta = "pho" + str( int(iphoton [0] ) ) + "_eta"
    #     name_phi = "pho" + str( int(iphoton [0] ) ) + "_phi"
    #     p4.SetPtEtaPhiM( getattr(intree, name_pt),  getattr(intree, name_eta),    getattr(intree, name_phi) , 0 )
    #     Phos.append(p4)
    if (int(intree.nphotons == 2)):
        # print int(intree.nphotons)
        for p in range(0,int(intree.nphotons)):
            p4 = ROOT.TLorentzVector(0,0,0,0)
            p4.SetPtEtaPhiM( intree.v_pho_pt[p], intree.v_pho_eta[p], intree.v_pho_phi[p], 0 )
            # print intree.v_pho_pt[p]
            Phos.append(p4)
            Phos_id.append(p)
    elif (int(intree.nphotons == 3)):
        # print int(intree.nphotons)
        for p in range(0,int(intree.nphotons)):
            p4 = ROOT.TLorentzVector(0,0,0,0)
            p4.SetPtEtaPhiM( intree.v_pho_pt[p], intree.v_pho_eta[p], intree.v_pho_phi[p], 0 )
            # print intree.v_pho_pt[p]
            Phos.append(p4)
            Phos_id.append(p)
    else:
        # print "here"
        # print int(intree.nphotons)
        for p in range(0,int(intree.nphotons)):
            p4 = ROOT.TLorentzVector(0,0,0,0)
            p4.SetPtEtaPhiM( intree.v_pho_pt[p], intree.v_pho_eta[p], intree.v_pho_phi[p], 0 )
            # print intree.v_pho_pt[p]
            Phos.append(p4)
            Phos_id.append(p)
    # print "HERE 1 "
    # print len(Phos)
    # print Phos[0].Pt()
    # print Phos[1].Pt()
    # print Phos[2].Pt()
    # print Phos[3].Pt()
    # print intree2.dp1_mass_prime
    if (len(Phos) > 3):
       print "four photon case"
       print Phos[0].Pt()
       print Phos[1].Pt()
       print Phos[2].Pt()
       print Phos[3].Pt()
       for i1 in range(0,len(Phos)):
           pho1 = Phos[i1]
           for i2 in range(0,len(Phos)):
               if (i2<=i1): continue
               pho2 = Phos[i2]
               for i3 in range(0,len(Phos)):
                   if (i3<=i2): continue
                   if (i3==i1): continue
                   pho3 = Phos[i3]
                   for i4 in range(0,len(Phos)):
                       if (i4<=i3): continue
                       if (i4 == i1 or i4 == i2): continue
                       pho4 = Phos[i4]
                       # print i1, i2, i3, i4

                       dipho1 = pho1 + pho2
                       dipho1_energy = dipho1.E()
                       dipho1_pt = dipho1.Pt()
                       dipho1_eta = dipho1.Eta()
                       dipho1_Phi = dipho1.Phi()
                       dipho1_dR = pho1.DeltaR(pho2)
                       dipho1_mass = dipho1.M()
                       deltaM1_gen1 = abs(dipho1.M()-float(Mass))
                       deltaM1_gen2 = abs(dipho1.M()-float(Mass))

                       dipho2 = pho3 + pho4
                       dipho2_energy = dipho2.E()
                       dipho2_pt = dipho2.Pt()
                       dipho2_eta = dipho2.Eta()
                       dipho2_Phi = dipho2.Phi()
                       dipho2_dR = pho3.DeltaR(pho4)
                       dipho2_mass = dipho2.M()
                       deltaM2_gen1 = abs(dipho2.M()-float(Mass))
                       deltaM2_gen2 = abs(dipho2.M()-float(Mass))

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
                       deltaM1_gen1 = abs(dipho1.M()-float(Mass))
                       deltaM1_gen2 = abs(dipho1.M()-float(Mass))

                       dipho2 = pho2 + pho4
                       dipho2_energy = dipho2.E()
                       dipho2_pt = dipho2.Pt()
                       dipho2_eta = dipho2.Eta()
                       dipho2_Phi = dipho2.Phi()
                       dipho2_dR = pho2.DeltaR(pho4)
                       dipho2_mass = dipho2.M()
                       deltaM2_gen1 = abs(dipho2.M()-float(Mass))
                       deltaM2_gen2 = abs(dipho2.M()-float(Mass))

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
                       deltaM1_gen1 = abs(dipho1.M()-float(Mass))
                       deltaM1_gen2 = abs(dipho1.M()-float(Mass))

                       dipho2 = pho2 + pho3
                       dipho2_energy = dipho2.E()
                       dipho2_pt = dipho2.Pt()
                       dipho2_eta = dipho2.Eta()
                       dipho2_Phi = dipho2.Phi()
                       dipho2_dR = pho2.DeltaR(pho3)
                       dipho2_mass = dipho2.M()
                       deltaM2_gen1 = abs(dipho2.M()-float(Mass))
                       deltaM2_gen2 = abs(dipho2.M()-float(Mass))

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

       Phos.sort(key=lambda x: x.Pt(), reverse=True)
       Pho1 = Phos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][0]]
       Pho2 = Phos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][1]]
       Pho3 = Phos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][2]]
       Pho4 = Phos[indexlist[max(xrange(len(mvalist)), key=mvalist.__getitem__)][3]]


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

       intree2.GetEntry(evt)
       # intree.GetEntry(evt)
       outtree.Fill()
outfile.cd()
outtree.Write()
outfile.Close()
