from ROOT import *

## Get all MC files:
mass = '60'
Cut = 'weight*!(tp_mass > 115 && tp_mass < 135)'
var='a1_mass_dM'
var_min=0
var_max=100
lumi_2016 = 35.9
lumi_2017 = 41.5
lumi_2018 = 54.38
inDir = '/eos/user/t/twamorka/h4g_fullRun2/TrainingApplied_19Nov2020/dataset_PhoMVA_manyKinVars_fullRun2_datamix_v10_dataSBScaling_m'+mass+'_17Nov2020_Final/Reduced_8Events/'
infile = []

infile.append(['QCD_30to40_'+mass+'_2016_skim_5Cats.root'])
infile.append(['QCD_30to40_'+mass+'_2017_skim_5Cats.root'])
infile.append(['QCD_30toInf_'+mass+'_2016_skim_5Cats.root'])
infile.append(['QCD_30toInf_'+mass+'_2017_skim_5Cats.root'])
infile.append(['QCD_30toInf_'+mass+'_2018_skim_5Cats.root'])
infile.append(['QCD_40toInf_'+mass+'_2016_skim_5Cats.root'])
infile.append(['QCD_40toInf_'+mass+'_2017_skim_5Cats.root'])
infile.append(['QCD_40toInf_'+mass+'_2018_skim_5Cats.root'])
infile.append(['GJet_20to40_'+mass+'_2016_skim_5Cats.root'])
infile.append(['GJet_20to40_'+mass+'_2017_skim_5Cats.root'])
infile.append(['GJet_20to40_'+mass+'_2018_skim_5Cats.root'])
infile.append(['GJet_20toInf_'+mass+'_2016_skim_5Cats.root'])
infile.append(['GJet_20toInf_'+mass+'_2017_skim_5Cats.root'])
infile.append(['GJet_20toInf_'+mass+'_2018_skim_5Cats.root'])
infile.append(['GJet_40toInf_'+mass+'_2016_skim_5Cats.root'])
infile.append(['GJet_40toInf_'+mass+'_2017_skim_5Cats.root'])
infile.append(['GJet_40toInf_'+mass+'_2018_skim_5Cats.root'])
infile.append(['DiPho_40to80_'+mass+'_2016_skim_5Cats.root'])
infile.append(['DiPho_40to80_'+mass+'_2017_skim_5Cats.root'])
infile.append(['DiPho_40to80_'+mass+'_2018_skim_5Cats.root'])
infile.append(['DiPho_80toInf_'+mass+'_2016_skim_5Cats.root'])
infile.append(['DiPho_80toInf_'+mass+'_2017_skim_5Cats.root'])
infile.append(['DiPho_80toInf_'+mass+'_2018_skim_5Cats.root'])

ch_2016 = TChain()
ch_2017 = TChain()
ch_2018 = TChain()
for f in infile:
    if '2016' in f[0]:
        ch_2016.AddFile(inDir+f[0]+'/H4GTag_Cat0_13TeV')
    if '2017' in f[0]:
        ch_2017.AddFile(inDir+f[0]+'/H4GTag_Cat0_13TeV')
    if '2018' in f[0]:
        ch_2018.AddFile(inDir+f[0]+'/H4GTag_Cat0_13TeV')

h_2016 = TH1F('h_2016',';'+var+'; Number of events',30,var_min,var_max)
h_2017 = TH1F('h_2017',';'+var+'; Number of events',30,var_min,var_max)
h_2018 = TH1F('h_2018',';'+var+'; Number of events',30,var_min,var_max)




print 'Before weight 2016:' ,ch_2016.GetEntries()
print 'Before weight 2017:' ,ch_2017.GetEntries()
print 'Before weight 2018:' ,ch_2018.GetEntries()

ch_2016.Draw(var+' >> h_2016',TCut(Cut))
ch_2017.Draw(var+' >> h_2017',TCut(Cut))
ch_2018.Draw(var+' >> h_2018',TCut(Cut))

print 'After weight 2016:' ,h_2016.Integral()
print 'After weight 2017:' ,h_2017.Integral()
print 'After weight 2018:' ,h_2018.Integral()

h_2016.Scale(lumi_2016)
h_2017.Scale(lumi_2017)
h_2018.Scale(lumi_2018)

print 'After scaling to lumi 2016:' ,h_2016.Integral()
print 'After scaling to lumi 2017:' ,h_2017.Integral()
print 'After scaling to lumi 2018:' ,h_2018.Integral()


h_2016.Add(h_2017)
h_2016.Add(h_2018)

print 'After adding 3 years together: ', h_2016.Integral()

c = TCanvas()
gStyle.SetOptStat(0)
h_2016.SetLineWidth(2)
h_2016.SetLineColor(kBlack)

h_2016.SetMarkerColor(kBlack)
h_2016.SetMarkerStyle(8)
# h_2016.Draw('PE')
h_2016.Draw('hist')


c.SaveAs('/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/MC_BDTChecks/MC_M'+mass+'_'+var+'.pdf')
c.SaveAs('/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/MC_BDTChecks/MC_M'+mass+'_'+var+'.png')
c.SetLogy()
c.SaveAs('/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/MC_BDTChecks/MC_M'+mass+'_'+var+'_log.pdf')
c.SaveAs('/eos/user/t/twamorka/www/H4G_Pre_PreApp_24Nov2020/MC_BDTChecks/MC_M'+mass+'_'+var+'_log.png')
