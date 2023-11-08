from flask import escape
import function_app
import json
import pandas as pd 

@function_app.http
def hello_http(request):

    request_args = request.args

    if request_args and "weight" in request_args:
        weight = request_args["weight"]
    else:
        weight = 100

    if request_args and "height" in request_args:
        height = request_args["height"]
    else:
        height = 175

    # Step 1 convert everything to numbers 
    weight_num = int(weight)
    height_num = int(height)

    # Step 2 we now some them all together 
    weight_height_sum = weight_num + height_num 

    # Step 3 create a json object to return to the user 
    output = json.dumps(
        {
            "entered_weight" : weight_num, 
            "entered_height": height_num, 
            "weight_height_sum" : weight_height_sum
        }
    )

    return output

