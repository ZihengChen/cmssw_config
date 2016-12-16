from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'step3'
config.General.workArea = 'DoubleB_4l_13TeV'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'
config.Data.inputDataset = '/bTag_B2bX_t_13TeV/zichen-step2_B2bX_13TeV-e095ae55313bf533ac8a376acb2dff3e/USER'

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
config.Data.outputDatasetTag = 'step3_DoubleB_4l_13TeV'

config.Site.storageSite = 'T3_US_FNALLPC'
