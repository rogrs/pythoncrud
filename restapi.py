import falcon
try:
    import ujson as json
except Exception, e:
    import json


class LeroleroResource:
    def on_get(self, req, resp):
        """Retorna um dicionário qualquer"""
        minha_frase = {
            'frase': "Acima de tudo, é fundamental ressaltar que a necessidade de renovação processual obstaculiza a apreciação da importância da gestão inovadora da qual fazemos parte.",
            'autor': 'Gerador de LeroLero'
        }

        resp.body = json.dumps(minha_frase)
        resp.set_header('Content-Type', 'application/json')
        resp.content_type = "application/json"

api = falcon.API()
api.add_route('/frase', LeroleroResource())
