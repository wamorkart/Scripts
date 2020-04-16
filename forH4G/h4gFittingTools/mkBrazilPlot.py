import ROOT
from ROOT import *
from mkBrazilPlotTools import *
from MyCMSStyle import *

def getLimits(file_name):
    file = TFile(file_name)
    tree = file.Get("limit")
    limits = []
    for quantile in tree:
        limits.append(float(tree.limit))
        # limits.append(float(tree.limit)/float(48610))
        print ">>>   %.3f" % limits[-1]
    print "DONE"
    print limits
    return limits[:6]

N = len(masses)
median = TGraph(N)
oneSigma = TGraph(2*N)
twoSigma = TGraph(2*N)

up2s = []
higgsXS =  48610
t = TText()
t.SetTextAlign(32)
t.SetTextSize(0.035)

for i in range(N):
    file_name = masses[i][0]
    # print file_name
    limit = getLimits(file_name)
    print "LIMIT ", limit
    print "median", limit[2]
    up2s.append(limit[4])
    twoSigma.SetPoint(i, masses[i][1], limit[4]) ## +2 sigma
    oneSigma.SetPoint(i, masses[i][1], limit[3]) ## +1 sigma
    median.SetPoint(i, masses[i][1], limit[2]) ## median
    oneSigma.SetPoint(2*N-1-i, masses[i][1], limit[1]) ## -1 sigma
    twoSigma.SetPoint(2*N-1-i, masses[i][1], limit[0]) ## -2 sigma
    t.DrawText(-0.42,masses[i][1],masses[i][2])


# c = TCanvas("c","c",100,100,W,H)
c = TCanvas()
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
# c.SetGrid()
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
frame.GetYaxis().SetTitle("95% CL on #sigma(pp#rightarrowH) x BR(H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma)")
# frame.GetYaxis().SetTitle("Limit on signal strength")\frac{n!}{k!(n-k)!}
# frame.GetYaxis().SetTitle("95% CL on #frac{#sigma(pp#rightarrowH)}{#sigma_{SM}} x BR(H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma)")
# frame.GetYaxis().SetTitle("95% CL on #sigma(pp#rightarrowH) x BR(H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma)/#sigma_{SM}")
# frame.GetXaxis().SetTitle("m_{a} [GeV]")
# frame.SetMinimum(0)
# frame.SetMaximum(0.5)
# frame.SetMaximum(max(up2s)*1.05)
# frame.SetLogy()
# frame.SetMaximum(0.01)
# frame.SetMinimum(0.000001)
frame.GetXaxis().SetLimits(1,6)
# frame.GetXaxis().SetBinLabel(1,'Angles+PhotonID')
# frame.GetXaxis().SetBinLabel(2,'Kin+PhotonID')
# frame.GetXaxis().SetBinLabel(3,'LimKin+PhotonID')
# frame.GetXaxis().SetBinLabel(4,'OnlyKin')
# frame.GetXaxis().SetBinLabel(5,'OnlyPhotonID')
# frame.GetXaxis().SetBinLabel(6,'PhoVars+HiggsVar+PhotonID')
# frame.GetYaxis().SetLimfloat(its(0,20))float(

twoSigma.SetFillColor(kYellow)
twoSigma.SetLineColor(kYellow)
twoSigma.SetFillStyle(1001)
twoSigma.Draw("F")

oneSigma.SetFillColor(kGreen+1)
oneSigma.SetLineColor(kGreen+1)
oneSigma.SetFillStyle(1001)
oneSigma.Draw("F same")

median.SetLineColor(1)
median.SetLineWidth(2)
median.SetMarkerStyle(20)
median.SetLineStyle(2)
median.Draw('LP same')

NoCat = TFile('limitGraph_NoCat.root')
NoCat_Limit = NoCat.Get('Graph')
NoCat_Limit.SetLineColor(kRed)
NoCat_Limit.SetMarkerStyle(20)
NoCat_Limit.SetMarkerColor(kRed)
NoCat_Limit.SetLineWidth(2)
# NoCat_Limit.Draw('LP same')
median.SaveAs("TEST.root")
# # leg = TLegend(0.156642, 0.693295, 0.447368, 0.883024)
# leg = TLegend(0.6, 0.7, 0.89, 0.89)
# leg.SetFillStyle(0)
# leg.SetBorderSize(0)
# leg.SetTextSize(0.035)
# leg.SetTextFont(42)
leg = TLegend(0.60,0.68,0.85,0.91)
leg.SetTextFont(42)
leg.SetTextSize(0.04)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.AddEntry(median,"Expected 95% upper limit","lp")
leg.AddEntry(oneSigma,"Expected limit #pm 1#sigma","f")
leg.AddEntry(twoSigma,"Expected limit #pm 2#sigma","f")
# leg.AddEntry(NoCat_Limit,"w/o Categorization","lp")
leg.Draw("same")

latex = TLatex()
latex.SetNDC()
latex.SetTextSize(25)
latex.SetTextAlign(33)
latex.SetTextFont(43)
# latex.DrawLatex(0.92,.92,"#bf{h#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma}")

l1 = DrawCMSLabels(c, lumi)
c.SetGrid()
c.Update()
# c.SetLogy()
c.SaveAs("9April2020_Limit.pdf")
# c.SetLogy()
# frame.SetMinimum(1)
# c.SaveAs("Limit_OldPairing_22Jan2020.pdf")
