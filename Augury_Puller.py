import requests
import os

API_key = input("What is you API key? ")
running = True
while running == True:
  def Puller():
    query_id_list = []
    with open("Query_ID_File.txt", "r") as f:
      for line in f:
        query_id_list.append(line)
        var = str(line)
        url = "https://augury5.heliumrain.com/api/results/" + var.rstrip('\n') + "?format=json"
        print (url)
        payload = ""
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": API_key}
        response = requests.request("GET", url, data=payload, headers=headers)
        filename = line.rstrip('\n') + ".json"
        file = open(os.path.join('C:\Data\Augury\Flows',filename), "w")

        file.write(response.text)
      file.close()

  Puller()
  running = False
print("Program has stopped running.")