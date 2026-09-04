from Tools.tavily_tool import tavily_search
# res=tavily_search("Best places to visit in Europe")
# print(res)
from Tools.flight_tool import search_flights
res=search_flights("Plan a 7 days Nepal trip from India")
print(res)