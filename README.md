# Azure Tweet Scheduler
> Tweet scheduler, which uses time-triggered Azure Functions

Work outline:
- [ ] Prepare Azure Function.
- [ ] Create program that connects with Twitter API.



# Prepare Azure Function

## Create and activate a virtual environment
```
$ python -m venv .venv
$ source .venv/bin/activate
```

## Create a local function project

```
$ func init tweetSchedulerProj --python
$ cd LocalFunctionProj
```




```
$ az login

# create a resource group
$ az group create \
    --name tweetSchedulerRG \
    --location norwayeast


```