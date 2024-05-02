from flask import Flask
import base64
import requests
app = Flask(__name__)

@app.route('/dividends/<string:company>')
def dividends(company):
    url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedSupplementCompany/"

    

    texto = '{"issuingCompany":"' + company +   '","language":"pt-br"}'
    texto_codificado = base64.b64encode(texto.encode('utf-8')).decode('utf-8')
    url = url + texto_codificado
    response = requests.get(url)
  
    response_json = response.json()
    return response_json

if __name__ == '__main__':
    app.run(debug=True, port=4002)