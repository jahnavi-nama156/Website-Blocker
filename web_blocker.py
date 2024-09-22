from datetime import datetime as dt
import time
import os

#the site names which want to block
websites_to_block = ["www.youtube.com",
    "youtube.com",
    "www.gmail.com",
    "gmail.com"]

#different hosts for different os
Linux_host = "/etc/hosts"
Window_host = r"C:\Windows\System32\drivers\etc\hosts"
default_hoster = Window_host # if you are on Linux then change it to Linux_host
redirect = "127.0.0.1"


if os.name == 'posix':
  default_hoster = Linux_host

elif os.name == 'nt':
  default_hoster = Window_host

else:
  print("Unknown OS")
  exit()


def blockwebsite(start_time , end_time):
  while True:
    try:
      current_time = dt.now()
      start_dt = dt(current_time.year,current_time.month,current_time.day,start_time)
      end_dt = dt(current_time.year,current_time.month,current_time.day,end_time)

      if start_dt < current_time < end_dt:
        print(f"Do work now... Current time: {current_time}")
        with open(default_hoster,"r+") as hostfile:
          hosts = hostfile.read()
          for site in websites_to_block:
            if site not in hosts:
              hostfile.write(redirect + " " + site + "\n")
      else:
        print(f"Good time... Current time: {current_time}")
        with open(default_hoster,"r+") as hostfile:
          hosts = hostfile.readlines()
          hostfile.seek(0)
          for host in hosts:
            if not any(site in host for site in websites_to_block):
              hostfile.write(host)
                
          hostfile.truncate()
        
      time.sleep(3)
    except PermissionError as e:
      print(f"Caught a permission error: Try Running as Admin {e}")
      # handle the error here or exit the program gracefully
      break

if __name__ == "__main__":
  blockwebsite(19,21)
