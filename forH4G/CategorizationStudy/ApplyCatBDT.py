from ROOT import *
from array import array

import argparse
parser =  argparse.ArgumentParser(description='Add Classification BDT weights')
parser.add_argument('-m', '--mass', dest='mass', required=True, type=str)
parser.add_argument('-iD', '--iD', dest='inDir', required=True, type=str)
parser.add_argument('-F', '--file', dest='File', required=True, type=str)
parser.add_argument('-W', '--weight', dest='Weight', required=True, type=str)
# parser.add_argument('-T', '--tree', dest='Tree', required=True, type=str)
parser.add_argument('-O', '--output', dest='Out', required=True, type=str)

opt = parser.parse_args()

reader = TMVA.Reader()

# ctscs = array('f', [0])
# cta1 = array('f', [0])
# cta2 = array('f', [0])
# a1ptohm = array('f',[0])
# a2ptohm = array('f',[0])
# p1ptoa1m = array('f', [0])
# p1ptoa2m = array('f', [0])

p1mva = array('f',[0])
p2mva = array('f',[0])
p3mva = array('f',[0])
p4mva = array('f',[0])
#p1pt = array('f',[0])
#p2pt = array('f',[0])
#p3pt = array('f',[0])
#p4pt = array('f',[0])
#p1eta = array('f',[0])
#p2eta = array('f',[0])
#p3eta = array('f',[0])
#p4eta = array('f',[0])
#tppt = array('f',[0])
#tpeta = array('f',[0])



# reader.AddVariable('CTStarCS',ctscs)
# reader.AddVariable('CT_a1Pho1',cta1)
# reader.AddVariable('CT_a2Pho1',cta2)
# reader.AddVariable('a1_Pt/tp_mass',a1ptohm)
# reader.AddVariable('a2_Pt/tp_mass',a2ptohm)
# reader.AddVariable('a1_Pho1PtOvera1Mass',p1ptoa1m)
# reader.AddVariable('a2_Pho1PtOvera2Mass',p1ptoa2m)

reader.AddVariable('pho1_MVA',p1mva)
reader.AddVariable('pho2_MVA',p2mva)
reader.AddVariable('pho3_MVA',p3mva)
reader.AddVariable('pho4_MVA',p4mva)
#reader.AddVariable('pho1_pt',p1pt)
#reader.AddVariable('pho2_pt',p2pt)
#reader.AddVariable('pho3_pt',p3pt)
#reader.AddVariable('pho4_pt',p4pt)
#reader.AddVariable('pho1_eta',p1eta)
#reader.AddVariable('pho2_eta',p2eta)
#reader.AddVariable('pho3_eta',p3eta)
#reader.AddVariable('pho4_eta',p4eta)
#reader.AddVariable('tp_pt',tppt)
#reader.AddVariable('tp_eta',tpeta)



reader.BookMVA("BDT",opt.Weight)

FilesToRedo = opt.File.split(',')
for f in FilesToRedo:
  print f
  infilename = opt.inDir + f
  # infilename = '/afs/cern.ch/work/t/twamorka/Scripts/forH4G/'+f
  # infilename = '/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/' + f
  # infilename  = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/'+f
  # infilename = '/eos/user/t/twamorka/forBadder_forMVAOptimization/' +f
  # infilename = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/'+f
  # infilename = '/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/'+f
  #infilename = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/'+f
  #infilename = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/'+f
  # infilename = '/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/'+f
  # print '/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(opt.mass)+'/'+f
  # infilename = '/eos/user/t/twamorka/Jan2020/2016Samples/BDTPairing/m_'+str(opt.mass)+'/'+f
  #infilename = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/'+f
  infile = TFile(infilename)
  print "file name:", infile
  tree = ''
  if ('signal' in f):
      tree = 'SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8'
  elif ('DiPho80toInf' in f):
      print "HERE "
      tree = 'DiPhotonJetsBox_MGG_80toInf_13TeV_Sherpa'
  elif ('DiPho40to80' in f):
      tree = 'DiPhotonJetsBox_M40_80_Sherpa'
  else: tree = 'Data'
  intree = infile.Get(tree+'_13TeV_4photons')
  # intree = infile.Get(str(opt.Tree)+"_13TeV_4photons")
  print "tree name: ", intree
  outfile = TFile(opt.Out, "RECREATE")
  # outfile = TFile(opt.Out+f.split("/")[len(f.split("/"))-1], "RECREATE")
  outtree = intree.CloneTree(0)
  bdt = array('f', [0])
  _bdt = outtree.Branch('bdt', bdt, 'bdt/F')
  # cat_MVA_value = array('f', [0])
  # _cat_MVA_value = outtree.Branch('cat_MVA_value', cat_MVA_value, 'cat_MVA_value/F')

  nentries = intree.GetEntries()

  for i in range(0, nentries):
     if i%1000 == 0: print i
     intree.GetEntry(i)
     # ctscs[0] = intree.CTStarCS
     # cta1[0] = intree.CT_a1Pho1
     # cta2[0] = intree.CT_a2Pho1
     # a1ptohm[0] = intree.a1_Pt/intree.tp_mass
     # a2ptohm[0] = intree.a2_Pt/intree.tp_mass
     # p1ptoa1m[0] = intree.a1_Pho1PtOvera1Mass
     # p1ptoa2m[0] = intree.a2_Pho1PtOvera2Mass
     p1mva[0] = float(intree.pho1_MVA)
     p2mva[0] = float(intree.pho2_MVA)
     p3mva[0] = float(intree.pho3_MVA)
     p4mva[0] = float(intree.pho4_MVA)
     #p1pt[0] = float(intree.pho1_pt)
     #p2pt[0] = float(intree.pho2_pt)
     #p3pt[0] = float(intree.pho3_pt)
     #p4pt[0] = float(intree.pho4_pt)
     #p1eta[0] = float(intree.pho1_eta)
     #p2eta[0] = float(intree.pho2_eta)
     #p3eta[0] = float(intree.pho3_eta)
     #p4eta[0] = float(intree.pho4_eta)
     #tppt[0] = float(intree.tp_pt)
     #tpeta[0] = float(intree.tp_eta)



     #a1ptom[0] = intree.a1_Pt/intree.a1_mass
     # a2ptom[0] = intree.a2_Pt/intree.a2_mass
     #a1a2dr[0] = intree.a1_a2_DR
     #p2ptoa1m[0] = intree.a1_Pho2PtOvera1Mass


     # mvas[0] = intree.pairMVAscore
     # rho[0] = intree.rho
     # p2ptoa2m[0] = intree.a2_Pho2PtOvera2Mass
     # a1m[0] = intree.a1_mass
     # a2m[0] = intree.a2_mass
     bdt[0] = reader.EvaluateMVA("BDT")
     # cat_MVA_value[0] = reader.EvaluateMVA("BDT")
     # if (cat_MVA_value[0] == -1):
         # print "-1 value"
     # print cat_MVA_value[0]

     outtree.Fill()

  outfile.cd()
  outtree.Write()
  outfile.Close()
