from ROOT import *

files = [
["M_60_DiPho_pho1_Hgg_EB.root", "EB; Hgg MVA", kGreen+2],
["M_60_DiPho_pho1_EGM_EB.root", "EB; EGamma MVA", kBlue+2],

]

dummy = TFile("dummy.root", "RECREATE")
grs = []

for f in files:
  ff = TFile(f[0])
  gr = ff.Get("ROC")
  dummy.cd()
  gr.SetLineColor(f[2])
  gr.Write()
  grs.append([gr, f[1]])

c = TCanvas("c", "c", 800, 600)
leg = TLegend(0.2, 0.2, 0.5, 0.6)
leg.SetLineWidth(0)
leg.SetBorderSize(0)
leg.SetFillStyle(0)
for ig,g in enumerate(grs):
  if ig == 0:
    g[0].Draw("ACP")
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
c.SaveAs("ROC_60_pho1_DiPho_EB.pdf")
