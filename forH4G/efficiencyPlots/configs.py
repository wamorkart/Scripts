##
## Configs for effs plotter
##

import argparse

parser =  argparse.ArgumentParser(description='H4G Efficiency Plotter')
parser.add_argument('-c', '--cut', dest='cut', required=True, type=str) ## pt cut on 3rd and 4th photon
parser.add_argument('-m', '--mcut', dest='mcut', required=True, type=str) ## MVA cut on 3rd and 4th photon

opt = parser.parse_args()
cut = opt.cut
mcut = opt.mcut
DEBUG=0

outLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/EfficiencyPlots/'

stepLegs = {
# 0:"Total",
0:"4#gamma",
1:"Online requirements",
2:"Higgs mass window selection",
3:"Photon Kin-selection",
4:"Photon ID selection"
}

steps = [0,1,2,3,4]
colors = ["#4A2545", "#389187","#DB995A", "#064789", "#B33951", "#FF1D15","#F0A202"]

cuts = ['pho1_pt > 30 && pho2_pt > 18 && pho3_pt >'+str(cut)+' && pho4_pt >' +str(cut)+' &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566)','pho1_pt > 30 && pho2_pt > 18 && pho3_pt >'+str(cut)+' && pho4_pt >' +str(cut)+' &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0','pho1_pt > 30 && pho2_pt > 18 && pho3_pt >'+str(cut)+' && pho4_pt >' +str(cut)+' &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 100 && tp_mass < 180','pho1_pt > 30 && pho2_pt > 18 && pho3_pt >'+str(cut)+' && pho4_pt >' +str(cut)+' &&  abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 100 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA >'+str(mcut)+' && pho4_MVA >'+str(mcut)]

outName = ""

header = "#font[61]{H#rightarrowaa#rightarrow#gamma#gamma#gamma#gamma}"
# xaxis = [15,20,25,30,35,40,45,50,55,60]
xaxis = [30,60]
xtitle = "Pseudoscalar mass [GeV]"
drawOpt = "P"

inFolder = '/eos/user/t/twamorka/Signal_Oct28_Lumi_1e3/hadd_Tree/'
files = [
# 'signal_m_15.root',
# 'signal_m_20.root',
# 'signal_m_25.root',
'signal_m_30.root',
# 'signal_m_35.root',
# 'signal_m_40.root',
# 'signal_m_45.root',
# 'signal_m_50.root',
# 'signal_m_55.root',
'signal_m_60.root'
]
