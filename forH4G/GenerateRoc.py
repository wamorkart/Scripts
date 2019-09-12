from ROOT import *
from array import array

import argparse
parser =  argparse.ArgumentParser(description='Add Classification BDT weights')
parser.add_argument('-s', '--signal', dest='sig', required=True, type=str)
parser.add_argument('-sT','--signal Tree',dest='sT',required=True,type=str)
parser.add_argument('-b', '--background', dest='bac', required=True, type=str)
parser.add_argument('-bT','--background Tree',dest='bT',required=True,type=str)
parser.add_argument('-v', '--var', dest='var', required=True, type=str)
parser.add_argument('-c', '--cut', dest='cut', required=True, type=str)
parser.add_argument('-o', '--output', dest='out', required=True, type=str)

opt = parser.parse_args()

f_sig = TFile(opt.sig)
f_bac = TFile(opt.bac)

t_sig = f_sig.Get("h4gCandidateDumper/trees/"+str(opt.sT))
t_bac = f_bac.Get("h4gCandidateDumper/trees/"+str(opt.bT))

print t_sig.GetEntries()
print t_bac.GetEntries()
var_n = opt.var.split(',')[0]
var_b = opt.var.split(',')[1]
var_min = opt.var.split(',')[2]
var_max = opt.var.split(',')[3]

var_step = (float(var_max) - float(var_min))/float(var_b)
print var_step
eff_sig = TH1F("eff_sig", ";"+var_n+";Signal Efficiency", int(var_b), float(var_min), float(var_max))
rej_bac = TH1F("rej_bac", ";"+var_n+";Background Rejection (1-Eff)", int(var_b), float(var_min), float(var_max))
ROC = TGraph()
ROC.SetName("ROC")

h_sig = TH1F("h_sig", ";"+var_n+";",int(var_b), float(var_min), float(var_max))
h_bac = TH1F("h_bac", ";"+var_n+";",int(var_b), float(var_min), float(var_max))

t_sig.Draw(var_n+">>h_sig", opt.cut, "goff")
t_bac.Draw(var_n+">>h_bac", opt.cut, "goff")

h_sig.Sumw2()
tot_sig = h_sig.Integral()
print tot_sig
h_sig.Scale(1./tot_sig)

h_bac.Sumw2()
tot_bac = h_bac.Integral()
print tot_bac
h_bac.Scale(1./tot_bac)

for x in range(0, int(var_b)):
    print '#bin',x
    sEff = h_sig.Integral(x+1, int(var_b)+1)
    bRej = h_bac.Integral(1, x+1)
    eff_sig.SetBinContent(x+1, sEff)
    rej_bac.SetBinContent(x+1, bRej)
    ROC.SetPoint(x, sEff, bRej)

def myROC(x,par=0):
    return ROC.Eval(x[0])

myROCTF1 = TF1("myROCTF1", myROC, 0, 1, 0)

outfile = TFile(opt.out, "RECREATE")
eff_sig.Write()
rej_bac.Write()
ROC.Write()
h_sig.Write()
h_bac.Write()
myROCTF1.Write()
outfile.Close()
