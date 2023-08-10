@staging
Feature: To test GET Weather Data API


    Scenario Outline: Pass different location to test GET Weather data API

        Given GET Weather Data API with <location>
        When GET request is performed
        Then API statusCode returned is 200
        And address returned should match <location>
        And days arrays should not be empty


        Examples:
        |location|
        |Delhi|



