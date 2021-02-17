import urllib.request
import json

with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
    data = response.read()

postinumerot = json.loads(data)


def main():

    postinumero = (input("Kirjoita postinumero: "))

    if postinumero in postinumerot:
        print(postinumerot[postinumero])
    else:
        print("tuntematon postinumero!")


if __name__ == '__main__':
    main()
