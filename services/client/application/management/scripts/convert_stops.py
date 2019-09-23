import json


def sptrans_to_json():
    try:
        file = open("/code/datasets/sptrans/stops.txt", mode="r")
        stop_dicts = []
        for lr in file.readlines():
            lr = lr.split(',')
            if lr[0] != 'stop_id':
                if len(lr) == 5:
                    id = lr[0]
                    address = str(lr[1]).replace('"', '')
                    latitude = lr[3]
                    longitude = lr[4]
                    reference = str(lr[2]).replace('"', '')
                else:
                    id = lr[0]
                    address = str(lr[1] + lr[2]).replace('"', '')
                    if len(lr) == 6:
                        latitude = lr[4]
                        longitude = lr[5]
                        reference = str(lr[3]).replace('"', '')
                    elif len(lr) == 7:
                        latitude = lr[5]
                        longitude = lr[6]
                        reference = str(lr[4]).replace('"', '')
                    else:
                        print("WTF: ", lr)
                stop_dicts.append({
                    "id": int(id),
                    "address": {
                        "location": str(address),
                        "coordinates": {
                            "latitude": float(latitude),
                            "longitude": float(longitude)
                        }
                    },
                    "reference": str(reference)
                })
        stop_dicts = json.dumps(stop_dicts, ensure_ascii=False).encode('utf8')
        with open("/code/datasets/sptrans/json/stops.json", 'w') as fp:
            fp.write(stop_dicts.decode())
        return False
    except Exception as e:
        print("Exceção em sptrans_to_json: ", e)
        return True