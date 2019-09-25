from ROOT import *
from massWindow_cumulative_tools import *

for f in file:
    chain = TChain('h4gCandidateDumper/trees/SUSYGluGluToHToAA_AToGG_M_'+str(f[1])+'_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons')
    chain.Add(f[0])

    for w in range(0,len(windowSize)):
        print "window size = ", windowSize[w]
        h = TH1F("h",";Avg. Diphoton Mass[GeV];# of events",n_bins, f[2],f[3] )
        chain.Draw('avg_dp_mass >> h',TCut(cut))

        n_bins =  h.GetNbinsX()
        print n_bins
        maxBin = h.GetMaximumBin()
        sum_low = 0
        sum_high = 0
        total = h.Integral()
        lowRange = 0
        highRange = 0

        for i2 in range(maxBin,0,-1):
            sum_low += h.GetBinContent(i2)
            lowRange = i2
            if ((sum_low*100/total) > (windowSize[w]/2)):
                break

        for i1 in range(maxBin,n_bins):
            sum_high += h.GetBinContent(i1)
            highRange = i1
            if ((sum_high*100/total) > (windowSize[w]/2)):
                break


        ma_low = h.GetXaxis().GetBinCenter(lowRange)
        ma_high = h.GetXaxis().GetBinCenter(highRange)

        y_max = h.GetMaximum()
        line_low = TLine(ma_low,0,ma_low,y_max);
        line_high = TLine(ma_high,0,ma_high,y_max);

        # print h.Integral(lowRange,maxBin)/h.Integral()
        # print h.Integral(maxBin,highRange)/h.Integral()
        # print (h.Integral(lowRange,maxBin)+h.Integral(maxBin,highRange))/h.Integral

        c = TCanvas('c', 'c', 800, 600)

        h.Draw("hist same")
        line_low.Draw("same")
        line_high.Draw("same")
        lat = TLatex()
        lat.SetNDC()
        lat.SetTextColor(kBlack)
        lat.SetTextAlign(11)
        lat.SetTextFont(63)
        lat.SetTextSize(25)
        lat.DrawLatex(0.11,0.91,"Mass window: "+str(ma_low)+"--"+str(ma_high))
        c.Update()
        c.SaveAs(outputLoc+'cumulative_M'+str(f[1])+'_'+str(windowSize[w])+'.pdf')
        c.SaveAs(outputLoc+'cumulative_M'+str(f[1])+'_'+str(windowSize[w])+'.png')
