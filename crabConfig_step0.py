from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'step0'
config.General.workArea = 'bTag_DoubleB_4l_13TeV'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'pSet_step0.py'

config.Data.outputPrimaryDataset = 'bTag_DoubleB_4l_13TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
NJOBS = 60  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'bTag_DoubleB_4l_13TeV'

config.Site.storageSite = 'T3_US_FNALLPC'