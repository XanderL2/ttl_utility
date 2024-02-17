import os, sys, re; 

arguments = sys.argv #Returns a list with the parameters


def match_text(std_out):
    if(re.search(r"Host\sUnreachable", std_out)):

        return print("Host not found, check host IP")

    else:
        
        ttl = int(re.search(r"ttl\=(\d*)", std_out).group(1)) 

        if(ttl >= 0 and ttl <= 64):
            return print(f'SO =>  {arguments[1]} : Unix (Linux, Mac or Android)')

        elif(ttl >= 64 and ttl <= 244):

            return print(f'SO =>  {arguments[1]} TTL = {ttl}: Windows ')

        else:
            return print(f"SO => {arguments[1]} TTL ={ttl}: Router SO")


if(len(arguments) > 3 or len(arguments) < 0):

    print("Incorrect: ")
    print("Use:     ttl <ip>")
         

elif(arguments[1] == "-r"):

    traceroute = os.popen(f"ping -c 1 {arguments[2]} -R").read();
    print(traceroute)

else:
    
    std_out = os.popen(f"ping -c 1 {arguments[1]}").read(); 
    match_text(std_out);



    













