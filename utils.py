from wit import Wit

access_token = "TIGB7EFOOFZA4G3DNEK5DRIZVPEQQIP4"

client = Wit(access_token = access_token)

# message_text = "quero marcar horário"


def wit_response(message_text):
    resp = client.message(message_text)
    entity = None
    value = None

    try:
        entity = list(resp['entities'])[0]
        value = resp['entities'][entity][0]['value']
    except:
        pass
    return (entity, value)

#print(wit_response("quais os serviços"))
