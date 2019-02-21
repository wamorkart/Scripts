## script for calculating weights on MC events -- Thanks Rafael!
import json, os

eosOutput = '/eos/cms/store/user/twamorka/'

GJets20to40 = ['GJets20to40',
'/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_backup_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

GJets20toInf = ['GJets20toInf',
'/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

GJets40toInf = ['GJets40toInf',
'/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD30toInf = ['QCD30toInf',
'/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD30to40 = ['QCD30to40',
'/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

QCD40toInf = ['QCD40toInf',
'/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUETP8M1_13TeV_Pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

DiPho40to80 = ['DiPho40to80',
'/DiPhotonJetsBox_M40_80-Sherpa/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

DiPho80toInf = ['DiPho80toInf',
'/DiPhotonJetsBox_MGG-80toInf_13TeV-Sherpa/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

DYJets = ['DYJets',
'/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6_ext2-v1-74c0514daa3d87bd951f57782e8afcd5/USER'
]

Data_F = ['Data_F',
'/DoubleEG/sethzenz-ReMiniAOD-03Feb2017-2_5_5-2_5_5-v0-Run2016C-03Feb2017-v1-a56cd34be537fa6f2c9a0e455e52bfcd/USER'
]

GluGluHToGG = ['GluGluHToGG',
'/GluGluHToGG_M-125_13TeV_powheg_pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-53d3ac6d2aa4d9bf300e04bdc8636d58/USER'
]

VBFHToGG = ['VBFHToGG',
'/VBFHToGG_M-125_13TeV_powheg_pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-4899ef0a862eed7e22d3c7ad59d6a784/USER'
]

VHTOGG = ['VHTOGG',
'/VHToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-91f695d98afd34b3751740a965bf460b/USER'
]

TTGG = ['TTGG',
'/TTGG_0Jets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

TTGJets = ['TTGJets',
'/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

TGJets = ['TGJets',
'/TGJets_TuneCUETP8M1_13TeV_amcatnlo_madspin_pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

TTJets = ['TTJets',
'/TTJets_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-17c645750168c82731e0bcef4523b51c/USER'
]

ttHJetToGG = ['ttHJetToGG',
'/ttHJetToGG_M125_13TeV_amcatnloFXFX_madspin_pythia8_v2/sethzenz-RunIISummer16-2_4_1-25ns_Moriond17-2_4_1-v0-RunIISummer16MiniAODv2-BS2016_BSandPUSummer16_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1-a441a93bb50ffde2d33d432edd33f748/USER'
]
bkgSample = QCD30toInf

#localDir = os.getcwd()

data_file_location = '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg//MetaData/data/RunIISummer16-2_4_1-25ns_Moriond17/datasets.json'
# if 'crovelli' in bkgSample[1] or 'musella' in bkgSample[1]:
# 	data_file_location = localDir + '/../MetaData/data/microAODdatasets/Spring15BetaV2_MetaV3/bkgPasquale.json'
#data_file_location = '/afs/cern.ch/work/t/twamorka/CMSSW_8_0_26_patch1/src/flashgg//MetaData/data/ReMiniAOD-03Feb2017-2_5_Y/datasets_7.json'

data_file = open(data_file_location)
data = json.load(data_file)

dataFiles = data[bkgSample[1]]['files']

totalWeight = 0
totalEvents = 0

for files in dataFiles:
	if int(files['nevents']) == 0: continue
	# print files['name'], files['nevents']#, files['weights']
	totalWeight += float(files['weights'])
	totalEvents += float(files['nevents'])



print "#################################################################"
print "## Dataset        ## Sum of events        ## Sum of Weights    ##"
print "## ",bkgSample[0],"    ##", totalEvents, "    ##", format(totalWeight, 'f'), " ##"
print "#################################################################"
