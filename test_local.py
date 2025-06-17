import requests
import json
import time
from requests.auth import HTTPBasicAuth

def test_terneo_api(host, serial, port=80, username=None, password=None):
    base_url = f"http://{host}:{port}/api.cgi"
    auth = HTTPBasicAuth(username, password) if username and password else None
    
    def make_request(cmd, params=None):
        data = {"cmd": cmd, "sn": serial}
        if params:
            data["par"] = params
            
        print(f"\nMaking request: {json.dumps(data, indent=2)}")
        try:
            response = requests.post(base_url, json=data, auth=auth, timeout=5)
            print(f"Status code: {response.status_code}")
            try:
                result = response.json()
                print(f"Response: {json.dumps(result, indent=2)}")
                return result
            except json.JSONDecodeError:
                print(f"Raw response: {response.text}")
                return None
        except Exception as e:
            print(f"Error: {str(e)}")
            return None

    # Test 1: Get status
    print("\n=== Test 1: Get Status ===")
    status = make_request(4)
    
    # Test 2: Get power state
    print("\n=== Test 2: Get Power State ===")
    power = make_request(1)
    
    # Test 3: Turn off
    print("\n=== Test 3: Turn Off ===")
    turn_off = make_request(1, [[125, 7, "1"]])
    
    # Wait a bit
    time.sleep(2)
    
    # Test 4: Get status after turn off
    print("\n=== Test 4: Get Status After Turn Off ===")
    status_after_off = make_request(4)
    
    # Test 5: Turn on
    print("\n=== Test 5: Turn On ===")
    turn_on = make_request(1, [[125, 7, "0"]])
    
    # Wait a bit
    time.sleep(2)
    
    # Test 6: Get status after turn on
    print("\n=== Test 6: Get Status After Turn On ===")
    status_after_on = make_request(4)

if __name__ == "__main__":
    # Replace these values with your device details
    HOST = "PUT_YOUR_IP"
    SERIAL = "PUT_YOUR_SERIAL"
    PORT = 80
    USERNAME = None  # Add if needed
    PASSWORD = None  # Add if needed
    
    test_terneo_api(HOST, SERIAL, PORT, USERNAME, PASSWORD) 