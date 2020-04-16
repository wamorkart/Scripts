from ROOT import *
nbins = 40
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/SignalComparison_2016and2017/'
Vars = []
Vars.append(['pho1_pt',';P_{T}(#gamma_{1}) [GeV]; Normalized Yields',nbins,20,100])
Vars.append(['pho2_pt',';P_{T}(#gamma_{2}) [GeV]; Normalized Yields',nbins,20,100])
Vars.append(['pho3_pt',';P_{T}(#gamma_{3}) [GeV]; Normalized Yields',nbins,10,70])
Vars.append(['pho4_pt',';P_{T}(#gamma_{4}) [GeV]; Normalized Yields',nbins,10,70])
Vars.append(['pho1_eta',';P_{T}(#gamma_{1}) [GeV]; Normalized Yields',nbins,-2.5,2.5])
Vars.append(['pho2_eta',';P_{T}(#gamma_{2}) [GeV]; Normalized Yields',nbins,-2.5,2.5])
Vars.append(['pho3_eta',';P_{T}(#gamma_{3}) [GeV]; Normalized Yields',nbins,-2.5,2.5])
Vars.append(['pho4_eta',';P_{T}(#gamma_{4}) [GeV]; Normalized Yields',nbins,-2.5,2.5])
Vars.append(['pho1_energy',';Energy(#gamma_{1}) [GeV]; Normalized Yields',nbins,20,150])
Vars.append(['pho2_energy',';Energy(#gamma_{2}) [GeV]; Normalized Yields',nbins,15,150])
Vars.append(['pho3_energy',';Energy(#gamma_{3}) [GeV]; Normalized Yields',nbins,0,100])
Vars.append(['pho4_energy',';Energy(#gamma_{4}) [GeV]; Normalized Yields',nbins,0,100])
Vars.append(['pho1_old_r9',';R9(#gamma_{1}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho2_old_r9',';R9(#gamma_{2}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho3_old_r9',';R9(#gamma_{3}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho4_old_r9',';R9(#gamma_{4}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho1_full5x5_r9',';full 5x5 R9(#gamma_{1}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho2_full5x5_r9',';full 5x5 R9(#gamma_{2}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho3_full5x5_r9',';full 5x5 R9(#gamma_{3}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho4_full5x5_r9',';full 5x5 R9(#gamma_{4}) ; Normalized Yields',nbins,0,1.1])
Vars.append(['pho1_MVA',';Photon ID MVA Score(#gamma_{1}) ; Normalized Yields',nbins,-1,1])
Vars.append(['pho2_MVA',';Photon ID MVA Score(#gamma_{2}) ; Normalized Yields',nbins,-1,1])
Vars.append(['pho3_MVA',';Photon ID MVA Score(#gamma_{3}) ; Normalized Yields',nbins,-1,1])
Vars.append(['pho4_MVA',';Photon ID MVA Score(#gamma_{4}) ; Normalized Yields',nbins,-1,1])
Vars.append(['pho12_dR',';#DeltaR(#gamma_{12}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho13_dR',';#DeltaR(#gamma_{13}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho14_dR',';#DeltaR(#gamma_{14}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho23_dR',';#DeltaR(#gamma_{23}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho24_dR',';#DeltaR(#gamma_{24}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho34_dR',';#DeltaR(#gamma_{34}) ; Normalized Yields',nbins,0,5])
Vars.append(['pho12_m',';Mass(#gamma_{12}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['pho13_m',';Mass(#gamma_{13}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['pho14_m',';Mass(#gamma_{14}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['pho23_m',';Mass(#gamma_{23}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['pho24_m',';Mass(#gamma_{24}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['pho34_m',';Mass(#gamma_{34}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['dp1_mass',';Mass(a_{1}) [GeV]; Normalized Yields',nbins,0,100])
Vars.append(['dp2_mass',';Mass(a_{2}) [GeV]; Normalized Yields',nbins,0,100])
Vars.append(['dp1_pt',';P_{T}(a_{1}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['dp2_pt',';P_{T}(a_{2}) [GeV]; Normalized Yields',nbins,0,150])
Vars.append(['tp_mass',';Mass(Higgs) [GeV]; Normalized Yields',nbins,0,180])
Vars.append(['absCosThetaStar_CS',';Abs. Cos Theta star; Normalized Yields',nbins,0,1])
Vars.append(['absCosTheta_pho_a1',';Abs. Cos Theta a1_pho; Normalized Yields',nbins,0,1])
Vars.append(['absCosTheta_pho_a2',';Abs. Cos Theta a2_pho; Normalized Yields',nbins,0,1])




mass  = [60,55,50,45,40,35,30,25,20,15]

files = [] ## [file name 2016,label name 2016, tree name 2016, file name 2017, label name 2017, tree name 2017]
files.append(['/eos/user/t/twamorka/EOY_2019/24Dec2019/hadd/signal_m_','m(a) = 60 GeV; 2016 MC','_TuneCUETP8M1_13TeV_pythia8_13TeV_4photons','/eos/user/t/twamorka/EOY_2019/2017Samples/wPairingApplied/Signal/signal_m_','m(a) = 60 GeV; 2017 MC','_TuneCP5_13TeV_pythia8_13TeV_4photons'])
