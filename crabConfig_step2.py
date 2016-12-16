from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'step2'
config.General.workArea = 'DoubleB_4l_13TeV'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'


config.Data.inputDataset = '/PYTHIA_DoubleB_4l_13TeV/zichen-step1_DoubleB_4l_13TeV-9e33a528e0ad91388312ad584fc95346/USER'
config.Data.inputDBS = 'phys03'
#config.Data.outputPrimaryDataset = 'axgamma_step1'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_US*"]

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 60  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'step2_DoubleB_4l_13TeV'

config.Site.storageSite = 'T3_US_FNALLPC'