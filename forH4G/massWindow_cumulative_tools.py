from ROOT import *

file = []
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_60.root',60,40,80])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_55.root',55,35,75])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_50.root',50,30,70])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_45.root',45,25,65])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_40.root',40,30,50])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_35.root',35,27,42])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_30.root',30,20,40])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_25.root',25,20,30])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_20.root',20,14,26])
file.append(['/eos/user/t/twamorka/19Signal2019/Signal/hadd/signal_m_15.root',15,10,20])

windowSize = [50,55,60,65,67,70,75,80,85,90]

n_bins = 100
outputLoc = '/afs/cern.ch/user/t/twamorka/www/H4Gamma/Sep2019/MassWindow/'

cut = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 10 && pho4_pt > 10 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6'
