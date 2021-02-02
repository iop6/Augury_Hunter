import requests
import json

#url = "https://augury5.heliumrain.com/api"
#payload = ""
auth = str(input("What is your auth key? "))
print(auth)
#headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": auth}
running = True

while running == True:
  '''
  def Puller():
    print ("------------------------------------------------")
    #Read file and create a list of query ids from the data within the file.
    query_ids = []
    with open("Query_ID_File", "r") as f:
      print ("-")
      for line in f:
        query_ids.append(line)
      print (query_ids[1])

    #Retrieve results from previous input to generate desired results and append them to a new file.
    var1 = open("mass_pull.json", "w")
    for line in query_ids:
      #results = requests.request("GET", url + str(line) + "?format=json", data=payload, headers=headers)
      results = requests.request("GET", url+"/results/" + line + "?format=json", data=payload, headers=headers)
      var1 = open("mass_pull.json", "w")
      var1.write(results.text)
      var1.close()
    print('\n------------------------------------------------')
    '''
  def Puller():
    url = "https://augury5.heliumrain.com/api/results/11534044?format=json"
    payload = ""
    headers = {'Authorization': 	"	8397cb23f42e8a8ca73d8b7a5098ce02afbce154"} #<----- THE ISSUE --------

    response = requests.request("GET", url, data=payload, headers=headers)
    #optional output method
    file = open("mass_pull.json", "w")
    file.write(response.text)
    file.close()  

  Puller()
  running = False
print("Program has stopped running.")