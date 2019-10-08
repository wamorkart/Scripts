import ROOT
from ROOT import *
from ratioPlotterTools import *
from math import *
from array import array
gROOT.SetBatch(1)
gStyle.SetOptStat(0)

def getRatio(hist1, hist2):
	graph = TGraphAsymmErrors(hist1)
	npoint = 0
	for i in xrange(0, hist1.GetNbinsX()):
		Bin = i+1
		b1 = hist1.GetBinContent(Bin)
		b2 = hist2.GetBinContent(Bin)

		if b1 == 0 or b2 == 0:
			continue

		ratio = b1/b2
		# print "ratio", ratio

		b1sq = b1*b1
		b2sq = b2*b2

		e1sq_up = hist1.GetBinErrorUp(Bin)*hist1.GetBinErrorUp(Bin)
		e2sq_up = hist2.GetBinErrorUp(Bin)*hist2.GetBinErrorUp(Bin)

		e1sq_low = hist1.GetBinErrorLow(Bin)*hist1.GetBinErrorLow(Bin)
		e2sq_low = hist2.GetBinErrorLow(Bin)*hist2.GetBinErrorLow(Bin)

		error_up = sqrt((e1sq_up * b2sq + e2sq_up * b1sq) / (b2sq * b2sq))
		error_low = sqrt((e1sq_low * b2sq + e2sq_low * b1sq) / (b2sq * b2sq))

		graph.SetPoint(npoint, hist1.GetBinCenter(Bin), ratio)
		graph.SetPointError(npoint, 0, 0, error_low, error_up)
		npoint += 1
	graph.Set(npoint)
	# graph.Draw()
	return graph


for v in Vars:
    for m in mass:
        print "mass ", m
        leg = TLegend(0.6, 0.7, 0.89, 0.89)
        leg.SetBorderSize(0)
        for fi, f in enumerate(files):
            ch1 = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(m)+f[2])
            ch1.Add(f[0]+str(m)+'.root')
            hname1 = v[0]+'_'+str(fi)
            h1 = TH1F(hname1,v[1],v[2],v[3],v[4])
            ch1.Draw(v[0]+'>>'+hname1)
            total1 = h1.Integral()
            h1.Scale(1./total1)
            h1.SetLineColor(kRed)
            h1.SetLineWidth(2)
            leg.AddEntry(h1,'m(a) = '+str(m)+'GeV; 2016 MC','l')
            ch2 = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(m)+f[5])
            ch2.Add(f[3]+str(m)+'.root')
            hname2 = v[0]+'_'+str(fi)
            h2 = TH1F(hname2,v[1],v[2],v[3],v[4])
            ch2.Draw(v[0]+'>>'+hname2)
            total2 = h2.Integral()
            h2.Scale(1./total2)
            h2.SetLineColor(kBlack)
            h2.SetLineWidth(2)
            leg.AddEntry(h2,'m(a) = '+str(m)+'GeV; 2017 MC','l')

            Max = h1.GetMaximum()
            h1.SetMaximum(Max+0.2*Max)


            c0 = TCanvas('a', 'a', 800, 900)

            pad1 = TPad('pad1','pad1',0,0.3,1,1)
            pad1.SetBottomMargin(0)
            pad1.Draw()
            pad1.cd()
            h1.GetYaxis().SetTitle("Normalized Yields")
            h1.Draw("hist")
            h2.Draw("hist same")
            leg.Draw("same")

            h1.GetYaxis().SetTitleSize(20)
            h1.GetYaxis().SetTitle("Normalized Yields")
            axis = TGaxis(0, 0, 0, 220, 0.001,220,510,"")
            axis.SetLabelFont(43)
            axis.SetLabelSize(15)
            axis.Draw("same")

            c0.cd()
            pad2 = TPad("pad2", "pad2", 0, 0.05, 1, 0.3)
            pad2.SetTopMargin(0)
            pad2.SetBottomMargin(0.2)
            pad2.SetGridx()
            pad2.Draw()
            pad2.cd()

            h_ratio = h2.Clone("h_ratio")
            h_ratio.SetLineColor(1)
            h_ratio.SetMinimum(0.5)
            h_ratio.SetMaximum(1.5)
            h_ratio.Sumw2()
            h_ratio.SetStats(0)
            h_ratio.Divide(h1)
            h_ratio.SetMarkerStyle(24)
            h_ratio.Draw("EP")
            pad2.Update()
            lline = TLine(pad2.GetUxmin(),1,pad2.GetUxmax(),1)
            lline.SetLineStyle(1)
            lline.Draw('same')
            h_ratio.GetYaxis().SetTitle("2017 MC/2016 MC")
            h_ratio.GetYaxis().SetNdivisions(505)
            h_ratio.GetYaxis().SetTitleSize(20)
            h_ratio.GetYaxis().SetTitleFont(43)
            h_ratio.GetYaxis().SetTitleOffset(1.55)
            h_ratio.GetYaxis().SetLabelFont(43) #Absolute font size in pixel (precision 3)
            h_ratio.GetYaxis().SetLabelSize(15)
            h_ratio.GetXaxis().SetNdivisions(100)
            h_ratio.GetXaxis().SetTitleSize(20)
            h_ratio.GetXaxis().SetTitleFont(43)
            h_ratio.GetXaxis().SetTitleOffset(4.)
            h_ratio.GetXaxis().SetLabelFont(43) # Absolute font size in pixel (precision 3)
            h_ratio.GetXaxis().SetLabelSize(15)
            h_ratio.GetXaxis().SetNdivisions(515)
            h_ratio.GetXaxis().SetTickLength(0.15)
            c0.SaveAs(outputLoc+v[0]+"_"+str(m)+"_ratio.pdf")
            c0.SaveAs(outputLoc+v[0]+"_"+str(m)+"_ratio.png")





    # for fi1, f1 in enumerate(Files_2016):
    #     ch1 = TChain(f1[2])
    #     ch1.Add(f1[0])
    #     hname1 = v[0]+'_'+str(fi1)
    #     h1 = TH1F(hname1,v[1],v[2],v[3],v[4])
    #     ch1.Draw(v[0]+'>>'+hname1)
    #     total1 = h1.Integral()
    #     h1.Scale(1./total1)
    #     h1.SetLineColor(kRed)
    #     h1.SetLineWidth(2)
    #     leg.AddEntry(h1,f1[1],'l')
    # for fi2, f2 in enumerate(Files_2017):
    #     ch2 = TChain(f2[2])
    #     ch2.Add(f2[0])
    #     hname2 = v[0]+'_'+str(fi2)
    #     h2 = TH1F(hname2,v[1],v[2],v[3],v[4])
    #     ch2.Draw(v[0]+'>>'+hname2)
    #     total2 = h2.Integral()
    #     h2.Scale(1./total2)
    #     h2.SetLineColor(kBlack)
    #     h2.SetLineWidth(2)
    #     leg.AddEntry(h2,f2[1],'l')
