import requests
import hashlib
import sys

def access_the_api(query_pass):
 url = 'https://api.pwnedpasswords.com/range/' + query_pass
 r = requests.get(url)


 if r.status_code != 200:
     print(f'The code is {r.status_code}, check the api again ')
 

 return r

def check_password_leaks(complete_hash,check_hash):

    complete_hash = (line.split(':') for line in complete_hash.text.splitlines())

    for h, count in complete_hash:
        if h == check_hash:
            return count
    return 0



def password_hash(password):
    hashing = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first_5 , remain = hashing[:5], hashing[5:]
    reqd_hash = access_the_api(first_5)
    return check_password_leaks(reqd_hash,remain)





def main(ar):
    for password in ar:
        count = password_hash(password)
        if count:
            print(f'{password} is hacked {count} times, Do not use it ')
        else:
            print(f'{password} is not hacked ever, You can go with this password ')
    return "Password checking complete "
if __name__  == '__main__':
    sys.exit(main(sys.argv[1:]))









