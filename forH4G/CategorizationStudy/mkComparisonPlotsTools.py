from ROOT import *

Cut_SR = '(weight)*(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9 && !((tp_mass > 115 && tp_mass < 135)))'

Cut_CR = 'pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && (pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA < -0.9 && pho4_MVA < -0.9) || (pho1_MVA > -0.9 && pho3_MVA > -0.9 && pho2_MVA < -0.9 && pho4_MVA < -0.9) || (pho1_MVA > -0.9 && pho4_MVA > -0.9 && pho2_MVA < -0.9 && pho3_MVA < -0.9) || (pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho1_MVA < -0.9 && pho4_MVA < -0.9) || (pho2_MVA > -0.9 && pho4_MVA > -0.9 && pho1_MVA < -0.9 && pho3_MVA < -0.9) || (pho3_MVA > -0.9 && pho4_MVA > -0.9 && pho1_MVA < -0.9 && pho2_MVA < -0.9) && !((tp_mass > 115 && tp_mass < 135))'

Cut_Sig = '(weight)*(pho1_pt > 30 && pho2_pt > 18 && pho3_pt > 15 && pho4_pt > 15 && abs(pho1_eta) < 2.5 && abs(pho2_eta) < 2.5 && abs(pho3_eta) < 2.5 && abs(pho4_eta) < 2.5 && (abs(pho1_eta) < 1.4442 || abs(pho1_eta) > 1.566) && (abs(pho2_eta) < 1.4442 || abs(pho2_eta) > 1.566) && (abs(pho3_eta) < 1.4442 || abs(pho3_eta) > 1.566) && (abs(pho4_eta) < 1.4442 || abs(pho4_eta) > 1.566) && pho1_pixelseed==0 && pho2_pixelseed==0 && pho3_pixelseed==0 && pho4_pixelseed==0 && tp_mass > 110 && tp_mass < 180 && pho1_MVA > -0.9 && pho2_MVA > -0.9 && pho3_MVA > -0.9 && pho4_MVA > -0.9)'

nbins = 50

Vars = []
Vars.append(['CTStarCS','CTStarCS',';absCosThetaStar_CS; Normalized Yields',nbins,0,1])
Vars.append(['CT_a1Pho1','CT_a1Pho1',';absCosTheta_pho_a1; Normalized Yields',nbins,0,1])
Vars.append(['CT_a2Pho1','CT_a2Pho1',';absCosTheta_pho_a2; Normalized Yields',nbins,0,1])
Vars.append(['a1_Pt/tp_mass','a1PtOverHiggsMass',';a1PtOverHiggsMass; Normalized Yields',nbins,0,1])
Vars.append(['a2_Pt/tp_mass','a2PtOverHiggsMass',';a2PtOverHiggsMass; Normalized Yields',nbins,0,1])
Vars.append(['a1_Pt/a1_mass','dp1_PtoverMass',';dp1_PtoverMass; Normalized Yields',nbins,0,3])
Vars.append(['a2_Pt/a2_mass','dp2_PtoverMass',';dp2_PtoverMass; Normalized Yields',nbins,0,3])
Vars.append(['a1_a2_DR','a1_a2_DR',';a_{12} dR; Normalized Yields',nbins,0,5])
Vars.append(['a1_Pho1PtOvera1Mass','a1_Pho1PtOvera1Mass',';a1_Pho1PtOvera1Mass; Normalized Yields',nbins,0,3])
Vars.append(['a1_Pho2PtOvera1Mass','a1_Pho2PtOvera1Mass',';a1_Pho2PtOvera1Mass; Normalized Yields',nbins,0,3])
Vars.append(['a2_Pho1PtOvera2Mass','a2_Pho1PtOvera2Mass',';a2_Pho1PtOvera2Mass; Normalized Yields',nbins,0,3])
Vars.append(['a2_Pho2PtOvera2Mass','a2_Pho2PtOvera2Mass',';a2_Pho2PtOvera2Mass; Normalized Yields',nbins,0,3])
Vars.append(['a1_mass','a1_mass',';a1_Mass; Normalized Yields',nbins,0,100])
Vars.append(['a2_mass','a2_mass',';a2_Mass; Normalized Yields',nbins,0,100])

# Vars.append(['pairMVAscore','pairMVAscore',';diphoPair_MVA Score; Normalized Yields',nbins,-1,1])
