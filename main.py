import requests
from datetime import date
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "fjdakfhvuicbvrnsfdasj",
    "username": "sauravbista",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#Creating USER
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

#Creating a graph
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
graph_config ={
    "id": "graph169",
    "name": "Python Practice Graph",
    "unit": "Days",
    "type": "int",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": user_params["token"]
}
# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

#Posting value to the graph

post_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today_date = date.today()
formatted_date = today_date.strftime("%Y%m%d")

post_config = {
    "date": formatted_date,
    "quantity": "1",
}
# post_response = requests.post(url=post_endpoint, json=post_config, headers=headers)
# print(post_response.text)

#editing a data

put_endpoint = f"{post_endpoint}/{formatted_date}"
put_config = {
    "quantity": "3"
}
put_response = requests.put(url=put_endpoint, json=put_config, headers=headers)
print(put_response.text)

#Updating the graph to change unit from days to total projects completed

update_config = {
    "unit": "Projects Completed"
}
update_response = requests.put(url=post_endpoint, json=update_config, headers=headers)
print(update_response.status_code)