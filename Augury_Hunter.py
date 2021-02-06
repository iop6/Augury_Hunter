import requests
import json
#-------------------------------------------------------------------------------------------------------------------------------------
#Test query 11645485
url = "https://augury5.heliumrain.com/api"
payload = ""
auth = str(input("What is your auth key? "))
headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": auth}
running = True
#-------------------------------------------------------------------------------------------------------------------------------------
while running == True:

  def Get_Bi_Directional():
    query_id = str(input("What is your query ID? "))
    src_dst = []
    flipped_ips = []
    detailed_lines = []
    BD_list = []
    Var_list = []

#-------------------------------------------------------------------------------------------------------------------------------------

    results = requests.request("GET", url+"/results/" + query_id + "?format=json", data=payload, headers=headers)
    BD_file = open("Bi_Directional.json", "w")
    BD_file.write(results.text)
    BD_file.close()

#-------------------------------------------------------------------------------------------------------------------------------------

    with open("Bi_Directional.json", "r") as f:
      for line in f:
        json_line = json.loads(line)
        #All needed field for daily tasking.
        timestamp = json_line["start_time"]
        src_ip = json_line["src_ip_addr"]
        src_cc = json_line["src_cc"]
        dst_ip = json_line["dst_ip_addr"]
        dst_cc = json_line["dst_cc"]
        proto = str(json_line["proto"])
        src_port = str(json_line["src_port"])
        dst_port = str(json_line["dst_port"])
        tcp_flags = str(json_line["tcp_flags"])
        num_pkts = str(json_line["num_pkts"])
        num_octets = str(json_line["num_octets"])

#-------------------------------------------------------------------------------------------------------------------------------------

        line = src_ip + "   " + dst_ip
        src_dst.append(line)
        flipper = dst_ip + "   " + src_ip
        flipped_ips.append(flipper)
        line_details = timestamp + "," + src_ip + "," + src_cc + "," + proto + ","  + dst_ip + ","  + dst_cc + "," + proto + "," + dst_port + "," + src_port + "," + tcp_flags + "," + num_pkts + "," + num_octets + "\n"
        detailed_lines.append(line_details)

#-------------------------------------------------------------------------------------------------------------------------------------
    '''
    x = 0
    for line in src_dst:
        y = x + 1
        while y < len(flipped_ips):
            if line == flipped_ips[y]:
                BD_list.append(detailed_lines[x])
            y += 1
        x += 1

    with open("Bi_Directional.csv", "w") as f:
        for line in BD_list:
            f.write(line)
    f.close()
    '''
    x = 0
    for line in src_dst:
        y = x + 1
        while y < len(flipped_ips):
            if line in Var_list:
                print("Howdy")
                break
            if line == flipped_ips[y]:
                print("Test")
                Var_list.append(src_dst[x])
                BD_list.append(detailed_lines[x])
            y += 1
        x += 1

    with open("Bi_Directional.csv", "w") as f:
        for line in BD_list:
            f.write(line)
    f.close()

#-------------------------------------------------------------------------------------------------------------------------------------
  Get_Bi_Directional()
  running = False
print("Script has stopped running.")
