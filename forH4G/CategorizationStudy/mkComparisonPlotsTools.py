from ROOT import *

Cut_SR = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6 && !((tp_mass > 115 && tp_mass < 135))'
Cut_CR = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && (pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA < -0.6 && pho4_MVA < -0.6) || (pho1_MVA > -0.9 && pho3_MVA > -0.6 && pho2_MVA < -0.9 && pho4_MVA < -0.6) || (pho1_MVA > -0.9 && pho4_MVA > -0.6 && pho2_MVA < -0.9 && pho3_MVA < -0.6) || (pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho1_MVA < -0.9 && pho4_MVA < -0.6) || (pho2_MVA > -0.9 && pho4_MVA > -0.6 && pho1_MVA < -0.9 && pho3_MVA < -0.6) || (pho3_MVA > -0.6 && pho4_MVA > -0.6 && pho1_MVA < -0.9 && pho2_MVA < -0.9) && !((tp_mass > 115 && tp_mass < 135))'

Cut_Sig = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.6 && pho4_MVA > -0.6'

nbins = 30

Vars = []
Vars.append(['absCosThetaStar_CS','absCosThetaStar_CS',';absCosThetaStar_CS; Normalized Yields',nbins,0,1])
Vars.append(['absCosTheta_pho_a1','absCosTheta_pho_a1',';absCosTheta_pho_a1; Normalized Yields',nbins,0,1])
Vars.append(['absCosTheta_pho_a2','absCosTheta_pho_a2',';absCosTheta_pho_a2; Normalized Yields',nbins,0,1])
Vars.append(['dp1_pt/tp_mass','a1PtOverHiggsMass',';a1PtOverHiggsMass; Normalized Yields',nbins,0,1])
Vars.append(['dp2_pt/tp_mass','a2PtOverHiggsMass',';a2PtOverHiggsMass; Normalized Yields',nbins,0,1])
Vars.append(['dp1_PtoverMass','dp1_PtoverMass',';adp1_PtoverMass; Normalized Yields',nbins,0,10])
Vars.append(['dp2_PtoverMass','dp2_PtoverMass',';adp2_PtoverMass; Normalized Yields',nbins,0,10])
# Vars.append(['dp1_dr','dp1_dr',';dp1_dr; Normalized Yields',nbins,0,5])
