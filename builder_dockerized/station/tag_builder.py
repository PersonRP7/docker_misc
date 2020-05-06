import requests

def filter_tags(link, *args):
    return [
        tag['name'] for tag in requests.get(link).json() \
            if args[0] not in tag['name'] and \
                args[1] not in tag['name']
    ]

if __name__ == "__main__":
    filter_tags("https://registry.hub.docker.com/v1/repositories/python/tags", "alpine", "windows")
# print(filter_tags("https://registry.hub.docker.com/v1/repositories/python/tags", "alpine", "windows"))
