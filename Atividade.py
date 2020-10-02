import requests
while True:
    try:
        query = input("Digite um país para saber sua capital (Em inglês): ")
        query = query.lower()
        print('')
        if len(query) == 0:
            break
        resp = requests.get("https://restcountries.eu/rest/v2/name/" + query)
        ddg = resp.json()
        p_id = ddg[0]["capital"]
        print("A capital é: " + p_id)
        print('')
        arquivo = open("pais_e_capital.tsv","a")
        arquivo.write("{}\t{}\n".format(ddg[0]["name"],ddg[0]["capital"]))
        arquivo.close()
        print("O país e sua capital foram salvos no arquivo .tsv")
        print('')
    except:
        print('Este país não foi encontrado, lembre-se de digitar o nome em Inglês')