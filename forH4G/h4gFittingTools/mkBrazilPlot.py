import ROOT
from ROOT import *
from mkBrazilPlotTools import *
from MyCMSStyle import *
gROOT.SetBatch(kTRUE)
def getLimits(file_name):
    file = TFile(file_name)
    tree = file.Get("limit")
    limits = []
    for quantile in tree:
        limits.append(float(tree.limit))
        # limits.append(float(tree.limit)/float(48610))
        # print ">>>   %.3f" % limits[-1]
    # print "DONE"
    # print limits
    return limits[:6]

def mkGraph(N,masses,color,style):
    median = TGraph(N)
    oneSigma = TGraph(2*N)
    twoSigma = TGraph(2*N)
    for i in range(N):
        file_name = masses[i][0]
        limit = getLimits(file_name)
        twoSigma.SetPoint(i, masses[i][1], limit[4]) ## +2 sigma
        oneSigma.SetPoint(i, masses[i][1], limit[3]) ## +1 sigma
        median.SetPoint(i, masses[i][1], limit[2])
        oneSigma.SetPoint(2*N-1-i, masses[i][1], limit[1]) ## -1 sigma
        twoSigma.SetPoint(2*N-1-i, masses[i][1], limit[0]) ## -2 sigma
    median.SetLineColor(color)
    median.SetLineWidth(2)
    median.SetMarkerColor(color)
    median.SetMarkerStyle(20)
    median.SetLineStyle(style)
    twoSigma.SetFillColorAlpha(kYellow,0.70)
    twoSigma.SetLineColor(kYellow)
    oneSigma.SetFillColorAlpha(kGreen+1,0.70)
    oneSigma.SetLineColor(kGreen+1)
    return median, oneSigma, twoSigma

def mkGraphOverSM(N,masses,color,style):
    graph = TGraph(N)
    higgs_SM_XS = 48.5*1000
    for i in range(N):
        file_name = masses[i][0]
        limit = getLimits(file_name)
        twoSigma.SetPoint(i, masses[i][1], limit[4]/higgs_SM_XS) ## +2 sigma
        oneSigma.SetPoint(i, masses[i][1], limit[3]/higgs_SM_XS) ## +1 sigma
        median.SetPoint(i, masses[i][1], limit[2]/higgs_SM_XS)
        oneSigma.SetPoint(2*N-1-i, masses[i][1], limit[1]/higgs_SM_XS) ## -1 sigma
        twoSigma.SetPoint(2*N-1-i, masses[i][1], limit[0]/higgs_SM_XS) ## -2 sigma
        # print limit[2]/higgs_SM_XS
    median.SetLineColor(color)
    median.SetLineWidth(2)
    median.SetMarkerColor(color)
    median.SetMarkerStyle(20)
    median.SetLineStyle(style)
    twoSigma.SetFillColorAlpha(kYellow,0.70)
    twoSigma.SetLineColor(kYellow)
    oneSigma.SetFillColorAlpha(kGreen+1,0.70)
    oneSigma.SetLineColor(kGreen+1)
    return median, oneSigma, twoSigma

def mkGraphRatio(N,masses_num,masses_denom,color,style):
    graph = TGraph(N)
    for i in range(N):
        file_name_num = masses_num[i][0]
        limit_num = getLimits(file_name_num)
        file_name_denom = masses_denom[i][0]
        limit_denom = getLimits(file_name_denom)
        graph.SetPoint(i, masses_num[i][1], limit_num[2]/limit_denom[2])
        #print limit_num[2]/limit_denom[2]
        # graph.SetPoint(i, masses[i][1], limit[2]*0.52194227317)
    graph.SetLineColor(color)
    graph.SetLineWidth(2)
    graph.SetMarkerColor(color)
    graph.SetMarkerStyle(20)
    graph.SetLineStyle(style)
    graph.Draw('LP same')
    return graph


N = len(mass)
median = TGraph(N)
oneSigma = TGraph(2*N)
twoSigma = TGraph(2*N)

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
frame.GetXaxis().SetTitle("m_{a} [GeV]")
frame.GetXaxis().SetLimits(15,60)

leg = TLegend(0.60,0.68,0.85,0.91)
leg.SetFillStyle(0)
leg.SetBorderSize(0)
leg.SetTextSize(0.04)
leg.SetTextFont(42)
leg.SetEntrySeparation(0.4)

if (mode=='Limit'):
    frame.GetYaxis().SetTitle("95% CL on #sigma(pp#rightarrowH) x BR(H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma) [fb]")
    frame.SetMaximum(4)
    frame.SetMinimum(0)

    gr = mkGraph(N,sample,kBlack,1)
    gr[2].Draw('F same')
    gr[1].Draw('F same')
    gr[0].Draw('LP same')

    leg.AddEntry(gr[0],"Expected 95% upper limit","lp")
    leg.AddEntry(gr[1],"Expected limit #pm 1#sigma","f")
    leg.AddEntry(gr[2],"Expected limit #pm 2#sigma","f")

    leg.Draw('same')

elif (mode=='LimitOverSM'):
    frame.GetYaxis().SetTitle("#frac{#sigma(pp#rightarrowH)}{#sigma_{SM}} x BR(H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma) ")
    frame.GetYaxis().SetTitleOffset(1.02)
    frame.SetMaximum(0.1e-03)
    frame.SetMinimum(0)

    gr = mkGraphOverSM(N,sample,kBlack,1)
    gr[2].Draw('F same')
    gr[1].Draw('F same')
    gr[0].Draw('LP same')

    leg.AddEntry(gr[0],"Expected 95% upper limit","lp")
    leg.AddEntry(gr[1],"Expected limit #pm 1#sigma","f")
    leg.AddEntry(gr[2],"Expected limit #pm 2#sigma","f")

    leg.Draw('same')


elif (mode=='Ratio'):
    frame.GetYaxis().SetTitle("Limit (No Vtx Split)/ Limit (With Vtx Split)")
    frame.SetMaximum(1.1)
    frame.SetMinimum(0.9)
    gr_ratio = mkGraphRatio(N,sample_num,sample_denom,1,1)
    gr_ratio.Draw('LP same')

c.SaveAs(outDir+outName+".pdf")
c.SaveAs(outDir+outName+".png")
