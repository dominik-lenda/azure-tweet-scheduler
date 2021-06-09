# Azure Tweet Scheduler
> Tweet scheduler, which uses time-triggered Azure Functions

Work outline:
- [x] Create and deploy timer-triggered Azure Functions
- [X] Create Cosmos DB account, database, and container
- [ ] Bind Azure Functions with database
- [ ] Create program that interacts with Twitter API

# Create and deploy timer-triggered Azure Functions
## Create and activate a virtual environment
```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

## Create a local function project using TimerTrigger template

```bash
$ func init tweetSchedulerProj --python
$ cd LocalFunctionProj
$ func new \
    --name timerTriggeredTweet \
    --template TimerTrigger
```

* Test the function locally using Azurite on Linux or Azure Storage Emulator on Windows.

## Create other needed Azure resources
```bash
# create a resource group
$ az group create \
    --name tweetSchedulerFunction-rg \
    --location norwayeast
# create a storage account
$ az storage account create \
    --name tweetschedulerstorage \
    --location norwayeast \
    --resource-group tweetSchedulerFunction-rg \
    --sku Standard_LRS
# create the function app
$ az functionapp create \
    --name ScheduleTweetsDL \
    --resource-group tweetSchedulerFunction-rg \
    --storage-account tweetschedulerstorage \
    --consumption-plan-location uksouth \
    --runtime python \
    --runtime-version 3.8 \
    --functions-version 3 \
    --os-type linux
```

## Deploy the function project to Azure
```
func azure functionapp publish ScheduleTweetsDL
```

# Create Cosmos DB account, database, and container
I've done it in Azure Portal; I'll prepare it in Bicep soon.

