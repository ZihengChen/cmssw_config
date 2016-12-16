from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'step1'
config.General.workArea = 'DoubleB_4l_13TeV'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1.py'

#fix b Tag
config.Data.inputDataset = '/bTag_DoubleB_4l_13TeV/zichen-bTag_DoubleB_4l_13TeV-137c744f4cc36464660debd408c29100/USER'
#config.Data.inputDataset = '/bTag_B2bX_t_13TeV/zichen-bTag_B2bX_t_13TeV-883aac71e059fcf7d6af37391c2881c8/USER'
#config.Data.inputDataset = '/bTag_FCNC_13TeV/zichen-bTag_FCNC_13TeV-6f6f8e2f989c4a3edc5d82980afdbf95/USER'

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
config.Data.outputDatasetTag = 'step1_DoubleB_4l_13TeV'
config.Site.storageSite = 'T3_US_FNALLPC'