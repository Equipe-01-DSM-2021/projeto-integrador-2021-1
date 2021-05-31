import pandas as pd
import numpy as np

CoberturaVanguarda = {
    "APARECIDA":               "VALE DO PARAÍBA",
    "CAÇAPAVA":                "VALE DO PARAÍBA",
    "CACHOEIRA PAULISTA":      "VALE DO PARAÍBA",
    "CANAS":                   "VALE DO PARAÍBA",
    "CUNHA":                   "VALE DO PARAÍBA",
    "GUARATINGUETÁ":           "VALE DO PARAÍBA",
    "IGARATÁ":                 "VALE DO PARAÍBA",
    "JACAREÍ":                 "VALE DO PARAÍBA",
    "JAMBEIRO":                "VALE DO PARAÍBA",
    "LAGOINHA":                "VALE DO PARAÍBA",
    "LORENA":                  "VALE DO PARAÍBA",
    "NATIVIDADE DA SERRA":     "VALE DO PARAÍBA",
    "PARAIBUNA":               "VALE DO PARAÍBA",
    "PINDAMONHANGABA":         "VALE DO PARAÍBA",
    "PIQUETE":                 "VALE DO PARAÍBA",
    "POTIM":                   "VALE DO PARAÍBA",
    "REDENÇÃO DA SERRA":       "VALE DO PARAÍBA",
    "ROSEIRA":                 "VALE DO PARAÍBA",
    "SANTA BRANCA":            "VALE DO PARAÍBA",
    "SÃO JOSÉ DOS CAMPOS":     "VALE DO PARAÍBA",
    "SÃO LUÍS DO PARAITINGA":  "VALE DO PARAÍBA",
    "TAUBATÉ":                 "VALE DO PARAÍBA",
    "TREMEMBÉ":                "VALE DO PARAÍBA",

    "ARAPEÍ":                  "VALE HISTÓRICO",
    "AREIAS":                  "VALE HISTÓRICO",
    "BANANAL":                 "VALE HISTÓRICO",
    "CRUZEIRO":                "VALE HISTÓRICO",
    "LAVRINHAS":               "VALE HISTÓRICO",
    "QUELUZ":                  "VALE HISTÓRICO",
    "SÃO JOSÉ DO BARREIRO":    "VALE HISTÓRICO",
    "SILVEIRAS":               "VALE HISTÓRICO",

    "CARAGUATATUBA":           "LITORAL NORTE",
    "ILHABELA":                "LITORAL NORTE",
    "SÃO SEBASTIÃO":           "LITORAL NORTE",
    "UBATUBA":                 "LITORAL NORTE",

    "CAMPOS DO JORDÃO":        "SERRA DA MANTIQUEIRA",
    "MONTEIRO LOBATO":         "SERRA DA MANTIQUEIRA",
    "SANTO ANTÔNIO DO PINHAL": "SERRA DA MANTIQUEIRA",
    "SÃO BENTO DO SAPUCAÍ":    "SERRA DA MANTIQUEIRA",

    "ATIBAIA":                 "REGIÃO BRAGANTINA",
    "BOM JESUS DOS PERDÕES":   "REGIÃO BRAGANTINA",
    "BRAGANÇA PAULISTA":       "REGIÃO BRAGANTINA",
    "JOANÓPOLIS":              "REGIÃO BRAGANTINA",
    "NAZARÉ PAULISTA":         "REGIÃO BRAGANTINA",
    "PIRACAIA":                "REGIÃO BRAGANTINA",
    "VARGEM":                  "REGIÃO BRAGANTINA"
}

# Criando um DataFrame "dfmc" de macrorregiões e cidades a partir do dicionário
dfmc = pd.DataFrame(columns=["Município", "Macrorregião"])


def incomeComparison(csvPath):

    # DataFrame da renda dos municípios
    dfr = pd.read_csv(csvPath, sep=';', error_bad_lines=False)

    # Filtrando somente as informações de salário médio mensal do DataFrame "dfr"
    df_sp = dfr.query(
        'Nome == "Salário médio mensal"').loc[:, 'Localidade':'2018']
    df_sp = df_sp.drop(columns=["2006", "2007"])
    df_sp['Localidade'] = df_sp['Localidade'].str.upper()

    # Criando um DataFrame "dfmc" de macrorregiões e cidades a partir do dicionário
    dfmc = pd.DataFrame(columns=["Município", "Macrorregião"])

    for cidade in CoberturaVanguarda.keys():
        dfmc = dfmc.append(pd.DataFrame(
            {"Município": [cidade], "Macrorregião": [CoberturaVanguarda[cidade]]}))

    # Filtrando cidades e serapando em macrorregiões de cobertura da TV Vanguarda
    df_vanguarda = df_sp.loc[df_sp['Localidade'].isin(dfmc.Município.values)]
    df_paraiba = df_sp.loc[df_sp['Localidade'].isin(dfmc.query(
        'Macrorregião == "VALE DO PARAÍBA"').Município.values)]
    df_historico = df_sp.loc[df_sp['Localidade'].isin(
        dfmc.query('Macrorregião == "VALE HISTÓRICO"').Município.values)]
    df_litoral = df_sp.loc[df_sp['Localidade'].isin(
        dfmc.query('Macrorregião == "LITORAL NORTE"').Município.values)]
    df_serra = df_sp.loc[df_sp['Localidade'].isin(dfmc.query(
        'Macrorregião == "SERRA DA MANTIQUEIRA"').Município.values)]
    df_bragantina = df_sp.loc[df_sp['Localidade'].isin(
        dfmc.query('Macrorregião == "REGIÃO BRAGANTINA"').Município.values)]

    # Média de salários mensais, por macrorregiões e cidades da cobertura da TV Vanguarda
    vanguarda = paraiba = historico = litoral = serra = bragantina = []

    for n in list(range(2008, 2019)):
        vanguarda.append(df_vanguarda[str(n)].mean())
        paraiba.append(df_paraiba[str(n)].mean())
        historico.append(df_historico[str(n)].mean())
        litoral.append(df_litoral[str(n)].mean())
        serra.append(df_serra[str(n)].mean())
        bragantina.append(df_bragantina[str(n)].mean())

    # Formatando um DataFrame para média de salários mensais com uma casa descimal
    vanguarda_cobertura = {'2008': round(vanguarda[0], 1),
                           '2009': round(vanguarda[1], 1),
                           '2010': round(vanguarda[2], 1),
                           '2011': round(vanguarda[3], 1),
                           '2012': round(vanguarda[4], 1),
                           '2013': round(vanguarda[5], 1),
                           '2014': round(vanguarda[6], 1),
                           '2015': round(vanguarda[7], 1),
                           '2016': round(vanguarda[8], 1),
                           '2017': round(vanguarda[9], 1),
                           '2018': round(vanguarda[10], 1)}

    vanguarda_paraiba = {'2008': round(paraiba[0], 1),
                         '2009': round(paraiba[1], 1),
                         '2010': round(paraiba[2], 1),
                         '2011': round(paraiba[3], 1),
                         '2012': round(paraiba[4], 1),
                         '2013': round(paraiba[5], 1),
                         '2014': round(paraiba[6], 1),
                         '2015': round(paraiba[7], 1),
                         '2016': round(paraiba[8], 1),
                         '2017': round(paraiba[9], 1),
                         '2018': round(paraiba[10], 1)}

    vanguarda_historico = {'2008': round(historico[0], 1),
                           '2009': round(historico[1], 1),
                           '2010': round(historico[2], 1),
                           '2011': round(historico[3], 1),
                           '2012': round(historico[4], 1),
                           '2013': round(historico[5], 1),
                           '2014': round(historico[6], 1),
                           '2015': round(historico[7], 1),
                           '2016': round(historico[8], 1),
                           '2017': round(historico[9], 1),
                           '2018': round(historico[10], 1)}

    vanguarda_litoral = {'2008': round(litoral[0], 1),
                         '2009': round(litoral[1], 1),
                         '2010': round(litoral[2], 1),
                         '2011': round(litoral[3], 1),
                         '2012': round(litoral[4], 1),
                         '2013': round(litoral[5], 1),
                         '2014': round(litoral[6], 1),
                         '2015': round(litoral[7], 1),
                         '2016': round(litoral[8], 1),
                         '2017': round(litoral[9], 1),
                         '2018': round(litoral[10], 1)}

    vanguarda_serra = {'2008': round(serra[0], 1),
                       '2009': round(serra[1], 1),
                       '2010': round(serra[2], 1),
                       '2011': round(serra[3], 1),
                       '2012': round(serra[4], 1),
                       '2013': round(serra[5], 1),
                       '2014': round(serra[6], 1),
                       '2015': round(serra[7], 1),
                       '2016': round(serra[8], 1),
                       '2017':  round(serra[9], 1),
                       '2018': round(serra[10], 1)}

    vanguarda_bragantina = {'2008': round(bragantina[0], 1),
                            '2009': round(bragantina[1], 1),
                            '2010': round(bragantina[2], 1),
                            '2011': round(bragantina[3], 1),
                            '2012': round(bragantina[4], 1),
                            '2013': round(bragantina[5], 1),
                            '2014': round(bragantina[6], 1),
                            '2015': round(bragantina[7], 1),
                            '2016': round(bragantina[8], 1),
                            '2017': round(bragantina[9], 1),
                            '2018': round(bragantina[10], 1)}

    cards = {"Vanguarda": vanguarda_cobertura, "ValeParaiba": vanguarda_paraiba,
             "ValeHistorico": vanguarda_historico, "Litoral": vanguarda_litoral,
             "Serra": vanguarda_serra, "RegiaoBragantina": vanguarda_bragantina}

    print(cards)
    return cards
