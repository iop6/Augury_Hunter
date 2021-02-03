import requests

running = True
while running == True:
  def Puller():
    query_id_list = []
    open("mass_pull.json", "w")
    with open("Query_ID_File", "r") as f:
      for line in f:
        query_id_list.append(line)
        var = str(line)
        url = "https://augury5.heliumrain.com/api/results/" + var.rstrip('\n') + "?format=json"
        print (url)
        payload = ""
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "8397cb23f42e8a8ca73d8b7a5098ce02afbce154"}
        response = requests.request("GET", url, data=payload, headers=headers)

        file = open("mass_pull.json", "a")
        file.write(response.text)
      file.close()  

  Puller()
  running = False
print("Program has stopped running.")