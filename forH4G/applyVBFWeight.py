import ROOT
from array import array

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
f.close()
# print run

# print list[0][3]
inputFile = '/eos/user/t/twamorka/Quaruntuples_11032020/hadd/BDTPairing/data_all_slim_forVBF_presel.root'
itree = ROOT.TChain("Data_13TeV_4photons")
itree.AddFile(inputFile)

outfile = ROOT.TFile("TEST_VBF.root", "RECREATE")
outtree = itree.CloneTree(0)
weight_VBF = array('f',[0])

_weight_VBF = outtree.Branch('weight_VBF',weight_VBF,'weight_VBF/F')

eventsToRun =  itree.GetEntries()
list_tree = []
for ievt in range(eventsToRun):
    itree.GetEntry(ievt)
    list_tree.append([float(itree.run), float(itree.lumi), float(itree.event)])


weight_vbf = []
for val in range(len(list_tree)):
    print list_tree[val], "  ", list.index(list_tree[val]), "  ", list[list.index(list_tree[val])], weight[list.index(list_tree[val])]
    weight_vbf.append(weight[list.index(list_tree[val])])

for ievt2 in range(eventsToRun):
    itree.GetEntry(ievt2)
    weight_VBF[0] = weight_vbf[ievt2]

    outtree.Fill()
outfile.cd()
outtree.Write()
outfile.Close()
    # weight_vbf.append(weight[list.index(list_tree[val])])
