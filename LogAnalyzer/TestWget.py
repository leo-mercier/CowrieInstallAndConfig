import requests

image_url = "http://143.198.43.169:64002/cowrie.json"

# URL of the image to be downloaded is defined as image_url
r = requests.get(image_url)  # create HTTP response object

# send a HTTP request to the server and save
# the HTTP response in a response object called r
with open("logs/dwd.txt", 'w') as f:
    # Saving received content as a png file in
    # binary format

    # write the contents of the response (r.content)
    # to a new file in binary mode.
    f.writelines(str(r.content))
