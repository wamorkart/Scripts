import ROOT
from ROOT import *
from math import sqrt
from NiceColors import *
from MyCMSStyle import *
import sys
sys.modules['RooFit'] = ROOT.RooFit
from RooFit import *

def getEffSigma(mass, pdf, wmin=110., wmax=130.,  step=0.01, epsilon=1.e-4):
  cdf = pdf.createCdf(RooArgSet(mass))
  point=wmin;
  points = [];
  if wmax > 179: step = 0.1

  while (point <= wmax):
    mass.setVal(point)
    if (pdf.getVal() > epsilon):
      points.append([point,cdf.getVal()]);
    point+=step

  low = wmin;
  high = wmax;
  width = wmax-wmin;

  for i in range(0, len(points)):
    for j in range(i, len(points)):
      wy = points[j][1] - points[i][1]
      if (abs(wy-0.683) < epsilon):
        wx = points[j][0] - points[i][0]
        if (wx < width):
          low = points[i][0];
          high = points[j][0];
          width=wx;
  print "effSigma: [", low, "-", high, "] = ", width/2.
  return width/2.


def MakeSigPlot(data,pdf,var,label,lumi,fname,binning,Xmin=-1,Xmax=-1):
    gROOT.SetBatch(kTRUE)

    frame = var.frame(RooFit.Title(" "),RooFit.Bins(binning))

    data.plotOn(frame,RooFit.MarkerStyle(kOpenSquare), RooFit.DataError(RooAbsData.SumW2),RooFit.XErrorSize(0))

    SigColor = TColor.GetColor(NiceBlueDark)
    GausColor = TColor.GetColor(NiceGreen2)
    DCBColor = TColor.GetColor(NiceRed)
    var.setRange("plot", Xmin, Xmax)
    pdf.plotOn(frame,RooFit.LineColor(SigColor),RooFit.Precision(1E-5), RooFit.Range("plot"))
    pdf.plotOn(frame,RooFit.LineColor(GausColor),RooFit.LineStyle(kDashDotted),RooFit.Components("gaus_h4g_fourphotons_rv_13TeV"), RooFit.Precision(1E-5))
    pdf.plotOn(frame,RooFit.LineColor(DCBColor),RooFit.LineStyle(kDashed),RooFit.Components("dcb_h4g_fourphotons_rv_13TeV"), RooFit.Precision(1E-5))

    curve = frame.getObject( int(1) )
    datah = frame.getObject( int(0) )
    datah.SetLineWidth(1)
    gauss = frame.getObject( int(2) )
    cbs = frame.getObject( int(3) )

    Max = frame.GetMaximum()
    SetGeneralStyle()
    c = TCanvas("c", "c", 800, 600)
    SetPadStyle(c)
    frame.Draw()
    xmax = frame.GetXaxis().GetXmax()
    xmin = frame.GetXaxis().GetXmin()

    deltabin = (xmax-xmin)/binning
    #sigmas = MakeBands(data,pdf,var,frame,curve,xmin,xmax,deltabin)

    c.Update()

    frame.Draw("same")
    datah.Draw("EPsame")
    tlatex = TLatex()
    tlatex.SetNDC()
    tlatex.SetTextAngle(0)
    tlatex.SetTextColor(kBlack)
    tlatex.SetTextFont(63)
    tlatex.SetTextAlign(11)
    tlatex.SetTextSize(25)
    tlatex.DrawLatex(0.17, 0.96, "CMS Simulation 13 TeV (36fb^{-1})")
    tlatex.SetTextFont(43)
    #tlatex.SetTextSize(20)
    tlatex.SetTextSize(25)
    xbegin = 0.60
    ybegin = 0.87

    analysis = "H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma"
    tlatex.DrawLatex(0.65, ybegin-0.1, analysis)
    # leg = TLegend(0.7, ybegin-0.61, 0.935, ybegin-0.21)
    leg = TLegend(0.156642, 0.693295, 0.447368, 0.883024)
    leg.SetFillStyle(0)
    leg.SetLineWidth(0)
    leg.SetBorderSize(0)
    leg.AddEntry(datah, "Signal Simulation", "pe")
    leg.AddEntry(gauss, "Gaussian component", "l")
    leg.AddEntry(cbs, "Crystal Ball component", "l")

    #pdf.Print("t")
    components = pdf.getComponents()
    mean = components.find("mean_dcb_h4g_fourphotons_rv_13TeV")
    meanValue = mean.getVal()
    sigmaEff = getEffSigma(var,pdf,Xmin,Xmax)
    leg.AddEntry("","Mean = "+str("%.2f"%meanValue) + "GeV","")
    leg.AddEntry("","#sigma_{Eff} = "+str("%.2f"%sigmaEff) + "GeV","")
    leg.Draw()
    c.SaveAs("test_plot_diffParameters_diffgausparam_v2_60p_coverage.pdf")


#def MakeBands(data, pdf, var, frame, curve, xmin, xmax, deltabin):
    #onesigma = TGraphAsymmErrors()
    #twosigma = TGraphAsymmErrors()

    #bins = []
    #bins.append([xmin*1.001, xmin, xmin+deltabin])
    #for ibin in range(1,frame.GetXaxis().GetNbins()+1):
		#lowedge = frame.GetXaxis().GetBinLowEdge(ibin)
		#upedge  = frame.GetXaxis().GetBinUpEdge(ibin)
		#center  = frame.GetXaxis().GetBinCenter(ibin)
		#bins.append(  (center,lowedge,upedge) )
    #bins.append([xmax*0.999, xmax-deltabin, xmax])

    #allbins = []
    #for ibin,bin in enumerate(bins):
             #center,lowedge,upedge = bin
	     #nombkg = curve.interpolate(center)
	     #largeNum = nombkg*50
             #largeNum = max(1,largeNum)
             #nlim = RooRealVar("nlim%s" % var.GetName(),"",0.,-largeNum,largeNum)
             #onesigma.SetPoint(ibin,center,nombkg)
             #twosigma.SetPoint(ibin,center,nombkg)
