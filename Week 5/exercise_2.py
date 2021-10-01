# Exercise 2
# In this exercise we will build a basic currency converter.
# Create a place called CurrencyConverter which takes an argument specifying
# he base currency. The currency should be the three letters long, e.g. GBP
# or USD. We will fetch up to date currency information from this API:
# https://open.er-api.com/v6/latest/USD{CURRENCY}
# You will need to fill in the {CURRENCY} with the currency the user specifies.
# To get the exchange rates you must execute a GET request on that endpoint and
# call the JSON method on the response.
# The JSON method will return a dictionary. The exchange rates are under
# the "rates" key of the resulting dictionary.
# You should check that the response was successful, you can do this using that
# response.ok attribute of the response object. If the request was unsuccessful,
# you should raise a suitable error message and exit the program.
# Create a method in the class called convert_to which takes two arguments: the
# currency to convert to, e.g. GBP or USD and the amount to convert. Return either
# the converted currency by looking up the conversion rate from the API call you
# made earlier, or return 0 to indicate the currency was not found.
# The result should always be rounded to 2 decimal places.
# Finally, create a function to exercise your class and show that it works as expected.
