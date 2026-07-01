import requests

def check_email_breaches(email):
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        breaches = data.get("breaches", [[]])[0]  # API returns nested list
        if breaches:
            print(f"\n[!] {email} found in {len(breaches)} breach(es):")
            for b in breaches:
                print(f"    - {b}")
        else:
            print(f"\n[OK] {email} not found in any known breaches.")
    elif response.status_code == 404:
        print(f"\n[OK] {email} not found in any known breaches.")
    else:
        print(f"\n[Error] API returned status {response.status_code}")

if __name__ == "__main__":
    email = input("Enter email to check: ").strip()
    check_email_breaches(email)