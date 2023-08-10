from behave import given,then,when
import requests
from utilities.payload import *
from utilities.configParser import getconfig

@given(u'GET Weather Data API with {location}')
def step_impl(context,location):
    context.getWeatherURL = context.URL+'/VisualCrossingWebServices/rest/services/timeline/'+location

@when(u'GET request is performed')
def step_impl(context):
    header = getWeatherDetailsheader()
    body = getWeatherDetailsbody()
    context.weatherResponse = requests.get(context.getWeatherURL,params=body,headers=header)


@then(u'API statusCode returned is {statusCode:d}')
def step_impl(context,statusCode):
    assert context.weatherResponse.status_code == statusCode


@then(u'address returned should match {location}')
def step_impl(context,location):
    assert context.weatherResponse.json()['address'] == location


@then(u'days arrays should not be empty')
def step_impl(context):
    assert len(context.weatherResponse.json()['days']) != 0