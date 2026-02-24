import urllib.request
import json

def test_request():
    """
    Sends a POST request to the RNG service to retrieve a random ticket ID
    using built-in urllib to avoid external dependencies.
    """
    url = "http://localhost:5001/generate-id"
    payload = {
        "api_key": "A3F91C2B44F0E1D9B07C8E5A12F4B6D3"
    }
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(url, data=data, method='POST')
    req.add_header('Content-Type', 'application/json')

    print(f"Requesting data from {url}...")
    
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                res_body = response.read().decode('utf-8')
                data = json.loads(res_body)
                print("Successfully received data!")
                print(f"Ticket ID: {data.get('ticket_id')}")
            else:
                print(f"Error: Received status code {response.status}")
                
    except urllib.error.URLError as e:
        print(f"Error: Could not connect to the RNG service. Reason: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    test_request()
