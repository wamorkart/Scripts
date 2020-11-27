##################################################
##################################################
## Configuration parameters to run MakeStack.py ##
##################################################
##################################################

debug = 1
doSignalOnly = True
doBlind = True
doSignalRegion = False
doKinCut = True
doHggMVALoose = False
doHggMVATight = False
doEGMVA = False
doHiggsWindow = True
mvaWP = 'veryLoose'
bkgtype = 'mix'
doreweight = False
Norm = 'DataSB'
mass='60'


doDataDriven = True
year = 1 ## year == 1 refers to full run 2
isPhoCR = False
hideData = False
lumi = 1
#do pile up reweighting
doPUweight = False
doSignal = False

file_json = ''

#dirName = '/eos/user/t/twamorka/www/13Oct2020_NewReweighting_Run2_Check_m45/'
#dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v3/'#Reweighting_v4_'+str(year)+'/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/PerMass_FullRun2_DataMix_v8_SignalDataMix_NormalizedToDataSideband/'+str(year)+'/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v3/'+str(Norm)
# dirName='/eos/user/t/twamorka/www/H4G_Pre_PreApp/PerMass_FullRun2_DataMix_v8_SignalDataMix_NormalizedToDataSideband/'+str(Norm)
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v10_v3_15Nov2020_noSel_'+str(Norm)+'/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_phoMVAReweight_PhotonMVAOnly_16Nov2020/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_KinVars_dataSBScaling_MinimalVariables_17Nov2020_OnlyPhoMVAReweighted'
#dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v10_Training_v3_17Nov2020/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v10_AllVariables_M60_DFReweighting_18Nov2020/'
# dirName='/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v10_Training_M25_19Nov2020'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_Old_NoWeightApplied_20Nov2020/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/BDTOutput_DataMix_v10_M'+mass+'_22Nov2020/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/DataMix_v10_NoWeight/FullRun2/'
dirName='TEST'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/DataMix_v10_OnlyKinVars_NoPhotonMVA_M60_noWeightAppliedDuringTraining/'
# SignalLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_noPhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m60_24Nov2020_Final/'
# DataLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_noPhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m60_24Nov2020_Final/'
# BkgLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_noPhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m60_24Nov2020_Final/'
# SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m25_17Nov2020_Final/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m25_17Nov2020_Final/'
# DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m25_17Nov2020_Final/'
# SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'+mass+'_17Nov2020_Final/'
SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'
DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'
BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'#+str(year)+'/Data_NoPreselectionsApplied/Mixing/'
#BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/2016/Data_NoPreselectionsApplied/Mixing/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'+mass+'_17Nov2020_Final/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'+str(year)+'/Data_NoPreselectionsApplied/Mixing/'
# DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'+mass+'_17Nov2020_Final/'
# SignalLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_final_fullRun2_datamix_FullRun2_dataFrame_dataSBScaling_m60_DFReweighting_18Nov2020/'
# BkgLocation='/eos/user/t/twamorka/h4g_forPreApp_Nov2020/2018/hadd/'
# BkgLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_final_fullRun2_datamix_FullRun2_dataFrame_dataSBScaling_m60_DFReweighting_18Nov2020/'
# DataLocation='/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_final_fullRun2_datamix_FullRun2_dataFrame_dataSBScaling_m60_DFReweighting_18Nov2020/'
# dirName = '/eos/user/t/twamorka/www/H4G_Pre_PreApp/DataMix_v8_CutsApplied_LumiNorm/'+Norm+'/NoAdditionalCutsApplied/'
# SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_addCuts/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_addCuts/'
# DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/dataset_PhoMVA_KinVars_fullRun2_datamix_v8_lumiScaling_addCuts/'
# SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/Standard_M60_Run2_OldTraining/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/Standard_M60_Run2_OldTraining/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'
# DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied/Standard_M60_Run2_OldTraining/'
#SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'+str(year)+'/hadd/'
#SignalLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
#BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
#DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/Training_CombinedMass_PerYear/'
#BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'+str(year)+'/hadd/'
#DataLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'+str(year)+'/hadd/'
# BkgLocation = '/eos/user/t/twamorka/h4g_fullRun2/withSystematics/'


if (year==2016):
   lumi = 35.9
   file_json = 'datasets/Datasets_Mix_2016.json'
   # file_json = 'datasets/Datasets_BkgMC_2016.json'

elif (year==2017):
    lumi = 41.5
    file_json = 'datasets/Datasets_Mix_2017.json'
    # file_json = 'datasets/Datasets_BkgMC_2017.json'
elif (year==2018):
    lumi = 54.38
    file_json = 'datasets/Datasets_Mix_2018.json'
    # file_json = 'datasets/Datasets_BkgMC_2018.json'
elif (year==1):
    lumi = 35.9+41.5+54.38
    file_json = 'datasets/Datasets_Mix_FullRun2.json'
signalFactor = 1

# print year
# print lumi

print file_json
data_file = open(file_json)

#number of bins in histograms
nbin = 30

prefix = ''

#plots to be made
plots = []
plots.append(["cosThetaStarCS_dM","cosThetaStarCS_dM","Cos #theta*",nbin,-1,1])
plots.append(["cosTheta_a1_dM","cosTheta_a1_dM","Cos #theta_{#gamma a_{1}}",nbin,-1,1])
plots.append(["cosTheta_a2_dM","cosTheta_a2_dM","Cos #theta_{#gamma a_{2}}",nbin,-1,1])
plots.append(["a1_mass_dM","a1_mass_dM","M(a1) [GeV]",nbin,0,150])
plots.append(["a2_mass_dM","a2_mass_dM","M(a2) [GeV]",nbin,0,150])
plots.append(["a1_a2_dR_dM","a1_a2_dR_dM","#Delta R (a1,a2)",nbin,0,10])
plots.append(["a1_dR_dM","a1_dR_dM","#Delta R (#gamma1, #gamma2)",nbin,0,6])
plots.append(["a2_dR_dM","a2_dR_dM","#Delta R (#gamma3, #gamma4)",nbin,0,6])
plots.append(["a1_pt_dM","a1_pt_dM","a1 (pT) [GeV]",nbin,0,300])
# plots.append(["a2_pt_dM","a2_pt_dM","a2 (pT) [GeV]",nbin,0,200])
plots.append(["a1_eta_dM","a1_eta_dM","a1 #eta",nbin,-7.5,7.5])
plots.append(["a2_eta_dM","a2_eta_dM","a2 #eta",nbin,-7.5,7.5])

plots.append(["a1_energy_dM","a1_energy_dM","a1 (energy) [GeV]",nbin,0,800])
plots.append(["a2_energy_dM","a2_energy_dM","a2 (energy) [GeV]",nbin,0,800])
plots.append(["a1_a2_MassDiff","a1_mass_dM-a2_mass_dM","(a1 M - a2 M) [GeV]",nbin,-100,100])

plots.append(["tp_mass","tp_mass","Higgs Mass [GeV]",nbin,110,180])
plots.append(["tp_pt","tp_pt","Higgs pT [GeV]",nbin,0,400])
plots.append(["tp_eta","tp_eta","Higgs #eta",nbin,-4,4])
plots.append(["pho1_MVA","pho1_MVA","#gamma1 MVA",nbin,-1,1])
plots.append(["pho2_MVA","pho2_MVA","#gamma2 MVA",nbin,-1,1])
plots.append(["pho3_MVA","pho3_MVA","#gamma3 MVA",nbin,-1,1])
plots.append(["pho4_MVA","pho4_MVA","#gamma4 MVA",nbin,-1,1])
#
plots.append(["pho1_pt","pho1_pt","#gamma1 pT [GeV]",nbin,30,300])
plots.append(["pho2_pt","pho2_pt","#gamma2 pT [GeV]",nbin,18,200])
plots.append(["pho3_pt","pho3_pt","#gamma3 pT [GeV]",nbin,15,100])
plots.append(["pho4_pt","pho4_pt","#gamma4 pT [GeV]",nbin,15,70])
plots.append(["pho1_eta","pho1_eta","#gamma1 #eta",nbin,-2.5,2.5])
plots.append(["pho2_eta","pho2_eta","#gamma2 #eta",nbin,-2.5,2.5])
plots.append(["pho3_eta","pho3_eta","#gamma3 #eta",nbin,-2.5,2.5])
plots.append(["pho4_eta","pho4_eta","#gamma4 #eta",nbin,-2.5,2.5])
plots.append(["pho1_pixelseed","pho1_pixelseed","#gamma1 Pixel Seed Veto",nbin,0,2])
plots.append(["pho2_pixelseed","pho2_pixelseed","#gamma2 Pixel Seed Veto",nbin,0,2])
plots.append(["pho3_pixelseed","pho3_pixelseed","#gamma3 Pixel Seed Veto",nbin,0,2])
plots.append(["pho4_pixelseed","pho4_pixelseed","#gamma4 Pixel Seed Veto",nbin,0,2])

plots.append(["a1_pt_dM_Over_tp_mass","a1_pt_dM/tp_mass","a1_pt_dM_Over_tp_mass",nbin,0,4])
plots.append(["a2_pt_dM_Over_tp_mass","a2_pt_dM/tp_mass","a2_pt_dM_Over_tp_mass",nbin,0,1.5])

plots.append(["a1_pt_dM_Over_a1_mass","a1_pt_dM/a1_mass_dM","a1_pt_dM_Over_a1_mass",nbin,0,30])
plots.append(["a2_pt_dM_Over_a2_mass","a2_pt_dM/a2_mass_dM","a2_pt_dM_Over_a2_mass",nbin,0,30])
plots.append(["pho1_pt_Over_a1_mass","pho1_pt/a1_mass_dM","pho1_pt_Over_a1_mass",nbin,0,15])
plots.append(["pho2_pt_Over_a1_mass","pho2_pt/a1_mass_dM","pho2_pt_Over_a1_mass",nbin,0,15])
plots.append(["pho3_pt_Over_a1_mass","pho3_pt/a1_mass_dM","pho3_pt_Over_a1_mass",nbin,0,15])
plots.append(["pho4_pt_Over_a1_mass","pho4_pt/a1_mass_dM","pho4_pt_Over_a1_mass",nbin,0,15])

plots.append(["pho1_pt_Over_a2_mass","pho1_pt/a2_mass_dM","pho1_pt_Over_a2_mass",nbin,0,15])
plots.append(["pho2_pt_Over_a2_mass","pho2_pt/a2_mass_dM","pho2_pt_Over_a2_mass",nbin,0,15])
plots.append(["pho3_pt_Over_a2_mass","pho3_pt/a2_mass_dM","pho3_pt_Over_a2_mass",nbin,0,15])
plots.append(["pho4_pt_Over_a2_mass","pho4_pt/a2_mass_dM","pho4_pt_Over_a2_mass",nbin,0,15])
# plots.append(["bdt","bdt","bdt",nbin,-1,1])
# if doSignalRegion:
#    plots.append(["bdt_SR","bdt","BDT",nbin,-1,1])
# else:
# plots.append(["bdt_WithWeight","bdt","BDT",nbin,-1,1])

# plots.append(["BDTTransform_SignalNormalizedToDataSB_50MBins","bdtTransformed","Transformed MVA",nbin,0,1])




#cuts to be used to make plots
Cut = "("
Cut_Signal = "1>0"
Cut_Bkg = "("
Cut_additional = "&& 1>0)"
# Cut_additional = "&& pho1_MVA>=-0.9 && pho2_MVA>=-0.9 && pho3_MVA>=-0.9 && pho4_MVA>=-0.9)"
#Cut_additional = "&& tp_mass > 115 && tp_mass < 135)"
# Cut_additional = "&& a1_pt_dM<140. && a2_pt_dM<70. && a1_mass_dM-a2_mass_dM>-50. && pho1_MVA>=-0.9 && pho2_MVA>=-0.9 && pho3_MVA>=-0.9 && pho4_MVA>=-0.9)"
