import ROOT
from ROOT import *
from configs import *
from array import array
from MyCMSStyle import *

gROOT.ProcessLine("gErrorIgnoreLevel = 5000;")

legendSize = 0.03
markerStyles = [ 24, 25, 26, 27, 28, 30, 32 ]
markerStylesFull = [ 20, 21, 22, 33, 34, 29, 23 ]
axes = {}

grs = TMultiGraph()
# grs = []
effs = {}
print weight
# for st in steps:
#     effs[st] = []
#     axes[st] = []
weightedCut = ""
if weight=='1':
   weightedCut = "weight"
elif weight=='0':
   weightedCut = "1>0"

thisweightedCut = TCut(weightedCut)
print weightedCut

for cut in cuts:
    effs[cut] = []
    axes[cut] = []

for n,i in enumerate(xaxis):
    print "analyzing file:", inFolder+files[n][0]
    ch = TChain('h4gCandidateDumper/trees/'+str(files[n][1]))
    ch.Add(inFolder+files[n][0])
    # print ch.GetEntries()
    hist_tot = TH1F('hist_tot','hist_tot',100,0,10000)
    ch.Draw('tp_mass >> hist_tot',thisweightedCut)
    totalEvs = hist_tot.Integral()
    # print totalEvs
    hist = TH1F('hist','hist',100,0,10000)
    for cut in cuts:
        ch.Draw('tp_mass >> hist',thisweightedCut*TCut(cut))
        nBins = hist.GetSize()-2
        yield_err = ROOT.Double(0)
        integral = hist.IntegralAndError(0,nBins+1,yield_err,"")
        effs[cut].append(100*float(integral)/float(totalEvs))
        axes[cut].append(int(i))
        # print float(integral)/float(totalEvs)

leg = TLegend(0.1,0.7,0.48,0.9)
leg.SetFillColor(kWhite)
leg.SetHeader(header)
Header = leg.GetListOfPrimitives().First()
Header.SetTextSize(.035)
leg.SetLineWidth(0)
# leg.SetNColumns(3)
leg.SetFillStyle(0)
leg.SetTextSize(legendSize)
for n, i in enumerate(cuts):
    print axes[i], "  ", effs[i]
    gr = TGraph(len(axes[i]), array('d', axes[i]), array('d', effs[i]))
    gr.SetLineColor(TColor.GetColor(colors[n]))
    gr.SetMarkerColor(TColor.GetColor(colors[n]))
    gr.SetMarkerStyle(markerStylesFull[n])
    gr.SetMarkerSize(1.5)
    grs.Add(gr)
    # print stepLegs[n]
    leg.AddEntry(gr, stepLegs[n], "p")
c0 = TCanvas("c", "c", 800, 750)
SetPadStyle(c0)
c0.SetGridy()
c0.SetGridx()
#
grs.SetTitle(";m_{a} GeV;Eficiency(%)")
grs.SetMaximum(150)
grs.SetMinimum(0)

grs.Draw("AP ")
leg.Draw("same")

c0.SaveAs(outLoc+outputName)
