import ROOT
from array import array
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

reader.BookMVA("BDT","/eos/user/t/twamorka/TMVAClassification_BDT_H4GPairing_M60_2016.weights.xml")


infilename = '/eos/user/t/twamorka/test.root'
infile = ROOT.TFile(infilename)
intree = infile.Get("photonCollTree")
intree2 = infile.Get("h4gCandidateDumper/trees/_13TeV_4photons")
outfile = ROOT.TFile("TEST.root", "RECREATE")
outtree = intree2.CloneTree(0)
pairMVAscore = array('f',[0])
a1_mass = array('f',[0])
a2_mass = array('f',[0])
a1_pt = array('f',[0])
a2_pt = array('f',[0])

_pairMVAscore = outtree.Branch('pairMVAscore',pairMVAscore,'pairMVAscore/F')
_a1_mass = outtree.Branch('a1_mass',a1_mass,'a1_mass/F')
_a2_mass = outtree.Branch('a2_mass',a2_mass,'a2_mass/F')
_a1_pt = outtree.Branch('a1_pt',a1_pt,'a1_pt/F')
_a2_pt = outtree.Branch('a2_pt',a2_pt,'a2_pt/F')

eventsToRun = intree.GetEntries()

for evt in range(0,eventsToRun):
    print "Event# ", evt
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
                    print i1, i2, i3, i4
                    dipho1 = pho1 + pho2
                    dipho1_energy = dipho1.E()
                    dipho1_pt = dipho1.Pt()
                    dipho1_eta = dipho1.Eta()
                    dipho1_Phi = dipho1.Phi()
                    dipho1_dR = pho1.DeltaR(pho2)
                    dipho1_mass = dipho1.M()
                    deltaM1_gen1 = abs(dipho1.M()-60)
                    deltaM1_gen2 = abs(dipho1.M()-60)

                    dipho2 = pho3 + pho4
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho3.DeltaR(pho4)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-60)
                    deltaM2_gen2 = abs(dipho2.M()-60)

                    dipair_dR = dipho1.DeltaR(dipho2)
#                     print dipho1_energy, "  ", dipho2_energy
#                     print dipho1_pt, "  ", dipho2_pt
#                     print dipho1_eta, "  ", dipho2_eta
#                     print dipho1_dR, "  ", dipho2_dR
#                     print deltaM1_gen1, " ",deltaM2_gen1
#                     print dipair_dR
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
                    print "mva 1 ", mva_value
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
                    deltaM1_gen1 = abs(dipho1.M()-60)
                    deltaM1_gen2 = abs(dipho1.M()-60)

                    dipho2 = pho2 + pho4
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho2.DeltaR(pho4)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-60)
                    deltaM2_gen2 = abs(dipho2.M()-60)

                    dipair_dR = dipho1.DeltaR(dipho2)

#                     print dipho1_energy, "  ", dipho2_energy
#                     print dipho1_pt, "  ", dipho2_pt
#                     print dipho1_eta, "  ", dipho2_eta
#                     print dipho1_dR, "  ", dipho2_dR
#                     print deltaM1_gen1, " ",deltaM2_gen1
#                     print dipair_dR
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
                    print "mva 2 ", mva_value
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
                    deltaM1_gen1 = abs(dipho1.M()-60)
                    deltaM1_gen2 = abs(dipho1.M()-60)

                    dipho2 = pho2 + pho3
                    dipho2_energy = dipho2.E()
                    dipho2_pt = dipho2.Pt()
                    dipho2_eta = dipho2.Eta()
                    dipho2_Phi = dipho2.Phi()
                    dipho2_dR = pho2.DeltaR(pho3)
                    dipho2_mass = dipho2.M()
                    deltaM2_gen1 = abs(dipho2.M()-60)
                    deltaM2_gen2 = abs(dipho2.M()-60)

                    dipair_dR = dipho1.DeltaR(dipho2)

#                     print dipho1_energy, "  ", dipho2_energy
#                     print dipho1_pt, "  ", dipho2_pt
#                     print dipho1_eta, "  ", dipho2_eta
#                     print dipho1_dR, "  ", dipho2_dR
#                     print deltaM1_gen1, " ",deltaM2_gen1
#                     print dipair_dR
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
                    print "mva 3 ", mva_value
                    mvaVal.append(mva_value)
                    dipair_index_map[0].append([i1,i4,i2,i3])
                    dipair_index_map[1].append(mva_value)
