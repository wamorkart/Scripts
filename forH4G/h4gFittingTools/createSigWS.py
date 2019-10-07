import ROOT
from ROOT import *
import sys
sys.modules['RooFit'] = ROOT.RooFit
from RooFit import *

inFile = '/eos/user/t/twamorka/19Signal2019/Signal/60/output_SUSYGluGluToHToAA_AToGG_M-60_TuneCUETP8M1_13TeV_pythia8_0.root'
ws_name = 'h4gCandidateDumper/cms_h4g_13TeV'
dataset_name = 'SUSYGluGluToHToAA_AToGG_M_60_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons'

temp_ws = TFile(inFile).Get(ws_name)

temp_dataset = temp_ws.data(dataset_name)
print temp_dataset.numEntries()

temp_dataset_reduced = temp_dataset.reduce('pho1_pt > 30 && pho2_pt > 20 && pho3_pt > 10 && pho4_pt > 10 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) &&  (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && tp_mass > 100 && tp_mass < 180 ')

tp_mass = temp_ws.var("tp_mass")
tp_mass.setBins(40)
frame = tp_mass.frame(100,180)
temp_dataset_reduced.plotOn(frame)
frame.Draw()

## import other variables
IntLumi = temp_ws.var("IntLumi")
dZ = temp_ws.var("dZ_zeroVtx")

mhLow=115
mhHigh=135
MH = ROOT.RooRealVar("MH","m_{H}",mhLow,mhHigh)

temp_dataset_reduced_var = temp_dataset_reduced.reduce(RooArgSet(tp_mass,IntLumi,dZ))
# getattr(ws_new,'import')(temp_dataset_reduced,RooArgSet(tp_mass))
# getattr(ws_new,'import')(temp_dataset_reduced_var,RooCmdArg())
# # temp_ws.factory("a_mass[40,80]")
# # temp_ws.factory("RooCBShape:sig_dcb_pdf(a_mass,mean[50,70],sigma[0.3,20],alpha[0,1000],n[0,10000])")
# # sig_pdf = temp_ws.pdf("sig_dcb_pdf")
# c1.SaveAs("test.pdf")
#
# # mean = ROOT.RooRealVar("ma","ma",63,57,66)
# # dm = ROOT.RooRealVar("dm","dm",0.1,-10,10)
# # mean = ROOT.RooFormulaVar("mean","mean","(@0+@1)",ROOT.RooArgList(mass,dm))
# # sigma = ROOT.RooRealVar("sigma","sigma",2,0.4,20)
#
mean = ROOT.RooRealVar("mean","mean",125,122,127)
sigma = ROOT.RooRealVar("sigma","sigma",1,0.1,3.0)
alpha1 = ROOT.RooRealVar("alpha1","alpha1",1.0,0.05,10)
n1 = ROOT.RooRealVar("n1","n1",2,0.1,10)
alpha2 = ROOT.RooRealVar("alpha2","alpha2",1.0,0.05,10)
n2 = ROOT.RooRealVar("n2","n2",2,0.1,10)
# alpha1 = ROOT.RooRealVar("alpha1","alpha1",1,0.1,3.0)
# n1 = ROOT.RooRealVar("n1","n1",1,0.1,10)
#
# gaus_pdf = ROOT.RooGaussian("gaus_pdf","gaus_pdf",a_mass,mean,sigma1)
#
# # frame = a_mass.frame()
# # g
# # fitresult = sig_pdf.fitTo(temp_dataset_reduced,RooFit.Save())
# #
# # dcb_pdf = ROOT.RooDoubleCB("dcb","dcb",a_mass,mean,sigma1,alpha1,n1,alpha1,n1)
# # pdf = temp_ws.pdf("gauss_pdf")
# fitResult = gaus_pdf.fitTo(temp_dataset_reduced,ROOT.RooFit.PrintLevel(-1))
dcb = ROOT.RooDoubleCB("dcb","dcb",tp_mass,mean,sigma,alpha1,n1,alpha2,n2)
# # temp_ws.factory( "Gaussian:sig_gaus_pdf(avg_dp_mass, mass[59.6,40,80], sigma[1.3,-5,5])")
# # temp_ws.factory( "RooDoubleCB:sig_dcb_pdf(avg_dp_mass, mean[60,40,80], sigma[2,1,20],a1[5,0.01,100],n1[20.,2.0001,500.],a2[5., 0.01, 100.],n2[20.,2.0001,500])")
# pdf = temp_ws.pdf("dcb")
fitresult = dcb.fitTo(temp_dataset_reduced,ROOT.RooFit.PrintLevel(-1))

# print fitresult.
# itResult = pdf.fitTo(temp_dataset,RooFit.Save(),RooFit.PrintLevel(-1))
# # fitResult = pdf.fitTo(temp_dataset,RooFit.SumW2Error(1),RooFit.PrintLevel(-1))
dcb.plotOn(frame)

outFileWS = 'test.root'
output = TFile(outFileWS,'Recreate')
ws_new = RooWorkspace('ws_13TeV','ws_13TeV')
getattr(ws_new,'import')(dcb,RooCmdArg())
getattr(ws_new,'import')(temp_dataset_reduced_var,RooCmdArg())
getattr(ws_new,'import')(IntLumi,RooCmdArg())
getattr(ws_new,'import')(dZ,RooCmdArg())
getattr(ws_new,'import')(MH,RooCmdArg())
# ws_new.import(dcb)
ws_new.Write()
output.Close()
#
frame.Draw()
c1.SaveAs("test.pdf")
