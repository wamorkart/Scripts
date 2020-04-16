from ROOT import *

files = [
# ["M60_Pho1_QCD.root", "QCD", kGreen+2],
["M60_Pho1_GJet.root", "GJet", kBlue+2],
# ["M60_Pho1_DiPho.root", "DiPho", kRed+2]

]

dummy = TFile("dummy.root", "RECREATE")
grs = []

for f in files:
  ff = TFile(f[0])
  gr = ff.Get("ROC")
  dummy.cd()
  gr.SetLineColor(f[2])
  gr.SetMarkerColor(f[2])
  # gr.SetMarkerStyle(20)
  gr.Write()
  grs.append([gr, f[1]])

c = TCanvas("c", "c", 800, 600)
c.SetGrid()
leg = TLegend(0.6, 0.7, 0.89, 0.89)
leg.SetLineWidth(0)
leg.SetBorderSize(0)
leg.SetFillStyle(0)
leg.SetTextSize(0.04)
for ig,g in enumerate(grs):
  if ig == 0:
    g[0].Draw("ALP")
    g[0].GetXaxis().SetLimits(0, 1)
    g[0].GetXaxis().SetTitle("Signal Efficiency")
    g[0].GetYaxis().SetTitle("Background Rejection (1-Eff)")
    c.Update()
  else:
    g[0].Draw("same")
  g[0].SetLineWidth(2)
  c.Update()
  leg.AddEntry(g[0], g[1], "l")
leg.Draw("same")
c.SaveAs("M60_Pho1.pdf")
