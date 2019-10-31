import ROOT
from ROOT import *
from mkBrazilPlotTools import *
from MyCMSStyle import *

def getLimits(file_name):
    file = TFile(file_name)
    tree = file.Get("limit")
    limits = []
    for quantile in tree:
        limits.append(tree.limit)
        print ">>>   %.3f" % limits[-1]
    print "DONE"
    print limits
    return limits[:6]

N = len(masses)
median = TGraph(N)
oneSigma = TGraph(2*N)
twoSigma = TGraph(2*N)

up2s = []
for i in range(N):
    file_name = masses[i][0]
    limit = getLimits(file_name)
    up2s.append(limit[4])
    twoSigma.SetPoint(i, masses[i][1], limit[4]) ## +2 sigma
    oneSigma.SetPoint(i, masses[i][1], limit[3]) ## +1 sigma
    median.SetPoint(i, masses[i][1], limit[2]) ## median
    oneSigma.SetPoint(2*N-1-i, masses[i][1], limit[1]) ## -1 sigma
    twoSigma.SetPoint(2*N-1-i, masses[i][1], limit[0]) ## -2 sigma


c = TCanvas("c","c",100,100,W,H)
c.SetFillColor(0)
c.SetBorderMode(0)
c.SetFrameFillStyle(0)
c.SetFrameBorderMode(0)
c.SetLeftMargin( L/W )
c.SetRightMargin( R/W )
c.SetTopMargin( T/H )
c.SetBottomMargin( B/H )
c.SetTickx(0)
c.SetTicky(0)
c.SetGrid()
c.cd()

frame = c.DrawFrame(1.4,0.001, 4.1, 10)
frame.GetYaxis().CenterTitle()
frame.GetYaxis().SetTitleSize(0.05)
frame.GetXaxis().SetTitleSize(0.05)
frame.GetXaxis().SetLabelSize(0.04)
frame.GetYaxis().SetLabelSize(0.04)
frame.GetYaxis().SetTitleOffset(0.9)
frame.GetXaxis().SetNdivisions(508)
frame.GetYaxis().CenterTitle(True)
frame.GetYaxis().SetTitle("Limit on signal strength")
frame.GetXaxis().SetTitle("m_{a} [GeV]")
frame.SetMinimum(0)
frame.SetMaximum(max(up2s)*1.05)
frame.GetXaxis().SetLimits(20,60)
frame.GetYaxis().SetLimits(0,20)

twoSigma.SetFillColor(kOrange)
twoSigma.SetLineColor(kOrange)
twoSigma.SetFillStyle(1001)
twoSigma.Draw("F")

oneSigma.SetFillColor(kGreen+1)
oneSigma.SetLineColor(kGreen+1)
oneSigma.SetFillStyle(1001)
oneSigma.Draw("F same")

median.SetLineColor(1)
median.SetLineWidth(2)
median.SetLineStyle(2)
median.Draw('Lsame')

# leg = TLegend(0.156642, 0.693295, 0.447368, 0.883024)
leg = TLegend(0.6, 0.7, 0.89, 0.89)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetTextSize(0.035)
leg.SetTextFont(42)
leg.AddEntry(median,"Expected 95% upper limit","l")
leg.AddEntry(oneSigma,"Expected limit #pm 1#sigma","f")
leg.AddEntry(twoSigma,"Expected limit #pm 2#sigma","f")
leg.Draw("same")

latex = TLatex()
latex.SetNDC()
latex.SetTextSize(25)
latex.SetTextAlign(33)
latex.SetTextFont(43)
latex.DrawLatex(0.92,.92,"#bf{h#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma}")

l1 = DrawCMSLabels(c, lumi)
c.Update()


c.SaveAs("test_limitplot.pdf")
