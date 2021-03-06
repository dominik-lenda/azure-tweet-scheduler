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
python3 -m venv .venv
source .venv/bin/activate
```

## Create a local function project using TimerTrigger template

```bash
# create a function project
func init tweetSchedulerProj --python
cd tweetSchedulerProj

# create a function using TimerTrigger template
FUNC_NAME="timerTriggeredTweet"
func new \
    --name $FUNC_NAME \
    --template TimerTrigger
```
## Running functions locally
I've used [**Azurite**](https://marketplace.visualstudio.com/items?itemName=Azurite.azurite) in Visual Studio Code to test the function locally on Linux. Use Azure Storage Emulator on Windows.

Add this line to `local.settings.json` to test the function locally on Linux.
```json
"AzureWebJobsStorage": "UseDevelopmentStorage=true"
```

Run function locally. 
```bash
func start
```

## Create resources for Functions app deployment

### Create a resource group
Login to Azure Portal `az login`.
```bash
RESOURCE_GROUP_NAME="tweetSchedulerFunction-rg"
az group create \
    --name $RESOURCE_GROUP_NAME \
    --location norwayeast
```
### Create a storage account
```bash
STORAGE_ACCOUNT_NAME="tweetschedulerstorage"
az storage account create \
    --name $STORAGE_ACCOUNT_NAME \
    --location norwayeast \
    --resource-group $RESOURCE_GROUP_NAME \
    --sku Standard_LRS
```
### Create the function app
```
FUNCTION_NAME="ScheduleTweetsDL"
az functionapp create \
    --name $FUNCTION_NAME \
    --resource-group $RESOURCE_GROUP_NAME \
    --storage-account $STORAGE_ACCOUNT_NAME \
    --consumption-plan-location uksouth \
    --runtime python \
    --runtime-version 3.8 \
    --functions-version 3 \
    --os-type linux
```

## Deploy the function project to Azure
```bash
func azure functionapp publish ScheduleTweetsDL
```






