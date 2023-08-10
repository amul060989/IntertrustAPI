from pyexpat import features

def before_feature(context,feature):
    if "staging" in feature.tags:
        context.URL = "https://weather.visualcrossing.com"