print("Starting..\n")
def sree_handler(event, context):
    kg=event['Kg']
    lb=float(kg)*2.20462
    ans = str(kg) + " Kgs is " + str(round(lb, 2)) + " lbs\n" 
    print(ans)
    return ans

# LAMBDA - den kan köra serverless
#          - utanför vår vanliga last
#         - LAMBDA ÄR JU som ett API. 
#            lambda är serverless - förvaltningsfri    
#           lambdas som triggas via HTTP - förvaltningsfri
#
#   serverless Databaser