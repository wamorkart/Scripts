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
effs = {}
for st in steps:
    effs[st] = []
    axes[st] = []

for n,i in enumerate(xaxis):
    print "analyzing file:", inFolder+files[n]
    thisFile =  TFile(inFolder+files[n])
    thisEffHist = thisFile.Get('FlashggH4GCandidate/cutFlow')
    totalEvs = 1
    if thisEffHist != None:
      totalEvs = thisEffHist.GetBinContent(1)
      for st in steps:
          effs[st].append(100*float(thisEffHist.GetBinContent(st+2)/float(totalEvs)))
          axes[st].append(int(i))


leg = TLegend(0.1,0.7,0.48,0.9)
leg.SetFillColor(kWhite)
leg.SetHeader(header)
Header = leg.GetListOfPrimitives().First()
Header.SetTextSize(.035)
leg.SetLineWidth(0)
# leg.SetNColumns(3)
leg.SetFillStyle(0)
leg.SetTextSize(legendSize)

for n, i in enumerate(steps):
    print axes[i], "  ", effs[i]
    gr = TGraph(len(axes[i]), array('d', axes[i]), array('d', effs[i]))
    gr.SetLineColor(TColor.GetColor(colors[n]))
    gr.SetMarkerColor(TColor.GetColor(colors[n]))
    gr.SetMarkerStyle(markerStylesFull[n])
    gr.SetMarkerSize(1.5)
    grs.Add(gr)
    leg.AddEntry(gr, stepLegs[i], "p")

c0 = TCanvas("c", "c", 800, 750)
SetPadStyle(c0)
c0.SetGridy()
c0.SetGridx()

grs.SetTitle(";m_{a} GeV;Cut flow efficiency(%)")
grs.SetMaximum(60)
grs.SetMinimum(0)

grs.Draw("AP same")
leg.Draw("same")
DrawCMSLabels(c0, '')
c0.Update()


c.SaveAs(outLoc+"Eff_2017.pdf")
