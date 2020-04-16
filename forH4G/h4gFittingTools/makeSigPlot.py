#!/usr/bin/env python
from ROOT import *
from sigPlotter import *
import sys, getopt, os

# rooWsSig = TFile('/afs/cern.ch/work/t/twamorka/Tanvi_H4Gamma/CMSSW_7_4_7/src/flashggFinalFit/Plots/FinalResults/CMS_H4G_sigfit_20.root')
# rooWsSig = TFile('/afs/cern.ch/work/t/twamorka/Tanvi_H4Gamma/CMSSW_7_4_7/src/flashggFinalFit/Signal/CMS_H4G_sigfit_60_wScalenSmearings.root')
rooWsSig = TFile('/afs/cern.ch/work/t/twamorka/Tanvi_H4Gamma/CMSSW_7_4_7/src/flashggFinalFit/Signal/CMS_H4G_sigfit_60_wScalenSmearings_pho3pho4_15PtCut.root')
sigWs = rooWsSig.Get('wsig_13TeV')
# sigWs.Print()

tp_mass = sigWs.var('tp_mass')
# tp_mass.Print()
#tp_mass.setVal(125)
sigWs.var("MH").setVal(125)

anaSig_tp = sigWs.pdf('hggpdfsmrel_13TeV_h4g_fourphotons_rv_13TeV')
sigDataSet = sigWs.data('sig_h4g_mass_m125_fourphotons')

MakeSigPlot(sigDataSet,anaSig_tp,tp_mass,"",36,"tmp",40,110,140)
