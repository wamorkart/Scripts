import ROOT
from array import array

from optparse import OptionParser
parser = OptionParser()
parser.add_option(   "-i", "--inputFile",   dest="inputFile",    default="input.root",       type="string",  help="Input file" )
parser.add_option(   "-t", "--tree",  dest="tree",   default="tree",      type="string",  help="tree")
parser.add_option(   "-s", "--signal",  dest="signal",   default="",      type="string",  help="signal")
parser.add_option(   "-o", "--outputFile",  dest="outputFile",   default="output.root",      type="string",  help="Output file")

(options, args) = parser.parse_args()

file = '/eos/user/t/twamorka/SWAN_projects/vbf-learn/examples/h4g_24March2020_Photon34_Loose.txt'

f=open(file,"r")
lines=f.readlines()

run = []
lumi = []
event = []
weight = []
list = []
for x in lines:
    run.append(float(x.split(' ')[0]))
    lumi.append(float(x.split(' ')[1]))
    event.append(float(x.split(' ')[2]))
    weight.append(float(x.split(' ')[3]))
    list.append([float(x.split(' ')[0]), float(x.split(' ')[1]),float(x.split(' ')[2])])

    # print float(x.split(' ')[3])
f.close()
# print run

# print list[0][3]
inputFile = options.inputFile
itree = ROOT.TChain(options.tree)
itree.AddFile(inputFile)
outfile = ROOT.TFile(options.outputFile,'recreate')
# inputFile = '/eos/user/t/twamorka/21March2020_Mixing/hadd/OldPairing/data_all_skim_small_forVBF_Loose.root'
# inputFile = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/BDTPairing/data_all_slim_forVBF.root'
# inputFile = '/eos/user/t/twamorka/1April2020_CatTrainign/8April2020_onlyKin_vLoose/data_all_skim.root'
# inputFile = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/BDTPairing/data_all_slim_forVBF_presel.root'
# itree = ROOT.TChain("Data_13TeV_4photons")
# inputFile = '/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/signal_m_60_skim.root'
# itree = ROOT.TChain('SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
# itree.AddFile(inputFile)
# outfile = ROOT.TFile('test_vbf_11apr2020.root','recreate')
# outfile = ROOT.TFile("/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/data_VBF_Gamma12_Medium.root", "RECREATE")
# outfile = ROOT.TFile('/eos/user/t/twamorka/Jan2020/2016Samples/OldDiphoPairing/wCatMVA_20Jan2020/m_60/signal_m_60_skim_VBFWeight.root','RECREATE')
outtree = itree.CloneTree(0)
weight_VBF = array('f',[0])

_weight_VBF = outtree.Branch('weight_VBF',weight_VBF,'weight_VBF/F')

eventsToRun =  itree.GetEntries()

if (options.signal == 'signal' or options.signal == 'dipho' or options.signal == 'data'):
    print "NOT CR"
    for ievt in range(eventsToRun):
        itree.GetEntry(ievt)
        weight_VBF[0] = 1.0
        outtree.Fill()
else:
    print "Doing CR"
    list_tree = []
    for ievt in range(eventsToRun):
        itree.GetEntry(ievt)
        list_tree.append([float(itree.run), float(itree.lumi), float(itree.event)])
    weight_vbf = []
    for val in range(len(list_tree)):
    # print list_tree[val], "  ", list.index(list_tree[val]), "  ", list[list.index(list_tree[val])], weight[list.index(list_tree[val])]
        weight_vbf.append(weight[list.index(list_tree[val])])
    # print weight[list.index(list_tree[val])]

    for ievt2 in range(eventsToRun):
        itree.GetEntry(ievt2)
        weight_VBF[0] = weight_vbf[ievt2]
        outtree.Fill()
outfile.cd()
outtree.Write()
outfile.Close()
    # weight_vbf.append(weight[list.index(list_tree[val])])
