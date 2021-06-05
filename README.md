# Azure Tweet Scheduler
> Tweet scheduler, which uses time-triggered Azure Functions

Work outline:
- [ ] Prepare timer-triggered Azure Functions
- [ ] Create database using CosmosDB
- [ ] Bind Azure Functions with database
- [ ] Create programt that interacts with Twitter API



# Prepare timer-triggered Azure Functions

## Create and activate a virtual environment
```
$ python -m venv .venv
$ source .venv/bin/activate
```

## Create a local function project using TimerTrigger template

```
$ func init tweetSchedulerProj --python
$ cd LocalFunctionProj
$ func new \
    --name timerTriggeredTweet \
    --template TimerTrigger
```

* Test the function locally using Azurite on Linux or Azure Storage Emulator on Windows.