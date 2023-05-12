import json


def reencode(jsonobj, from_codec, to_codec):

    if type(jsonobj) == list:
    
        for i in range(len(jsonobj)):
            jsonobj[i] = reencode(jsonobj[i], from_codec, to_codec)

    elif type(jsonobj) == dict:

        for k in jsonobj.keys():
            jsonobj[k] = reencode(jsonobj[k], from_codec, to_codec)

    elif type(jsonobj) == str:

        try:
            jsonobj = jsonobj.encode(from_codec).decode(to_codec)

        except UnicodeEncodeError as e:
            print(' - UnicodeEncodeError - ' + e.reason + ': ' + jsonobj)

        except UnicodeDecodeError as e:
            print(' - UnicodeDecodeError - ' + e.reason + ': ' + jsonobj)

    return(jsonobj)


if __name__=='__main__':

    print('\nRe-encode all text fields in a JSON file\n---')
    fpath = input('JSON file path: ')
    from_codec = input('Re-encode from codec: ')
    to_codec = input('Re-encode to codec: ')
    print('---')

    jf = json.load(open(fpath, 'r'))
    jf_new = reencode(jf, from_codec, to_codec)

    open(fpath[:-5] + '_converted.json','w').write(json.dumps(jf_new, indent=4))
    print('---\nDone.\n')