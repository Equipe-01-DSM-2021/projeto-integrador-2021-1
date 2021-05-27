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

col_evolucaoeleitorado = ["NR_ANO_ELEICAO",
                          "SG_UF", "NM_MUNICIPIO", "QTD_ELEITORES"]


def evolutionComparison(year, csvPaths):
    # Criando um DataFrame "dfmc" de macrorregiões e cidades a partir do dicionário
    dfmc = pd.DataFrame(columns=["Município", "Macrorregião"])
    for cidade in CoberturaVanguarda.keys():
        dfmc = dfmc.append(pd.DataFrame(
            {"Município": [cidade], "Macrorregião": [CoberturaVanguarda[cidade]]}))

    # DataFrames da evolução do número de eleitores
    eleitorado2014 = pd.read_csv(csvPaths[0], usecols=col_evolucaoeleitorado,
                                 encoding='iso-8859-1', sep=';', error_bad_lines=False)
    eleitorado2016 = pd.read_csv(csvPaths[1], usecols=col_evolucaoeleitorado,
                                 encoding='iso-8859-1', sep=';', error_bad_lines=False)
    eleitorado2018 = pd.read_csv(csvPaths[2], usecols=col_evolucaoeleitorado,
                                 encoding='iso-8859-1', sep=';', error_bad_lines=False)
    eleitorado2020 = pd.read_csv(csvPaths[3], usecols=col_evolucaoeleitorado,
                                 encoding='iso-8859-1', sep=';', error_bad_lines=False)
    if year == 2022:
        eleitorado2022 = pd.read_csv(csvPaths[4], usecols=col_evolucaoeleitorado,
                                     encoding='iso-8859-1', sep=';', error_bad_lines=False)
    if year == 2024:
        eleitorado2022 = pd.read_csv(csvPaths[4], usecols=col_evolucaoeleitorado,
                                     encoding='iso-8859-1', sep=';', error_bad_lines=False)
        eleitorado2024 = pd.read_csv(csvPaths[5], usecols=col_evolucaoeleitorado,
                                     encoding='iso-8859-1', sep=';', error_bad_lines=False)

    # Filtrando, pela estado de SP:
    elei2014 = eleitorado2014.loc[eleitorado2014['SG_UF'] == 'SP']
    elei2016 = eleitorado2016.loc[eleitorado2016['SG_UF'] == 'SP']
    elei2018 = eleitorado2018.loc[eleitorado2018['SG_UF'] == 'SP']
    elei2020 = eleitorado2020.loc[eleitorado2020['SG_UF'] == 'SP']
    if year == 2022:
        elei2022 = eleitorado2022.loc[eleitorado2022['SG_UF'] == 'SP']
    elif year == 2024:
        elei2022 = eleitorado2022.loc[eleitorado2022['SG_UF'] == 'SP']
        elei2024 = eleitorado2024.loc[eleitorado2024['SG_UF'] == 'SP']

    # Filtro por macrorregiões da cobertura da TV Vanguarda:
    cobertura_vanguarda = dfmc.Município.values
    vale_do_paraiba = dfmc.query(
        'Macrorregião == "VALE DO PARAÍBA"').Município.values
    vale_historico = dfmc.query(
        'Macrorregião == "VALE HISTÓRICO"').Município.values
    litoral_norte = dfmc.query(
        'Macrorregião == "LITORAL NORTE"').Município.values
    serra_da_mantiqueira = dfmc.query(
        'Macrorregião == "SERRA DA MANTIQUEIRA"').Município.values
    regiao_bragantina = dfmc.query(
        'Macrorregião == "REGIÃO BRAGANTINA"').Município.values

    # Criando DataFrames acumuladores:
    vanguarda2014 = elei2014.loc[elei2014['NM_MUNICIPIO'] == tuple(
        cobertura_vanguarda)]
    vanguarda2016 = elei2016.loc[elei2016['NM_MUNICIPIO'] == tuple(
        cobertura_vanguarda)]
    vanguarda2018 = elei2018.loc[elei2018['NM_MUNICIPIO'] == tuple(
        cobertura_vanguarda)]
    vanguarda2020 = elei2020.loc[elei2020['NM_MUNICIPIO'] == tuple(
        cobertura_vanguarda)]

    valep2014 = elei2014.loc[elei2014['NM_MUNICIPIO']
                             == tuple(vale_do_paraiba)]
    valep2016 = elei2016.loc[elei2016['NM_MUNICIPIO']
                             == tuple(vale_do_paraiba)]
    valep2018 = elei2018.loc[elei2018['NM_MUNICIPIO']
                             == tuple(vale_do_paraiba)]
    valep2020 = elei2020.loc[elei2020['NM_MUNICIPIO']
                             == tuple(vale_do_paraiba)]

    valeh2014 = elei2014.loc[elei2014['NM_MUNICIPIO'] == tuple(vale_historico)]
    valeh2016 = elei2016.loc[elei2016['NM_MUNICIPIO'] == tuple(vale_historico)]
    valeh2018 = elei2018.loc[elei2018['NM_MUNICIPIO'] == tuple(vale_historico)]
    valeh2020 = elei2020.loc[elei2020['NM_MUNICIPIO'] == tuple(vale_historico)]

    litoraln2014 = elei2014.loc[elei2014['NM_MUNICIPIO'] == tuple(
        litoral_norte)]
    litoraln2016 = elei2016.loc[elei2016['NM_MUNICIPIO'] == tuple(
        litoral_norte)]
    litoraln2018 = elei2018.loc[elei2018['NM_MUNICIPIO'] == tuple(
        litoral_norte)]
    litoraln2020 = elei2020.loc[elei2020['NM_MUNICIPIO'] == tuple(
        litoral_norte)]

    serram2014 = elei2014.loc[elei2014['NM_MUNICIPIO']
                              == tuple(serra_da_mantiqueira)]
    serram2016 = elei2016.loc[elei2016['NM_MUNICIPIO']
                              == tuple(serra_da_mantiqueira)]
    serram2018 = elei2018.loc[elei2018['NM_MUNICIPIO']
                              == tuple(serra_da_mantiqueira)]
    serram2020 = elei2020.loc[elei2020['NM_MUNICIPIO']
                              == tuple(serra_da_mantiqueira)]

    regiaob2014 = elei2014.loc[elei2014['NM_MUNICIPIO']
                               == tuple(regiao_bragantina)]
    regiaob2016 = elei2016.loc[elei2016['NM_MUNICIPIO']
                               == tuple(regiao_bragantina)]
    regiaob2018 = elei2018.loc[elei2018['NM_MUNICIPIO']
                               == tuple(regiao_bragantina)]
    regiaob2020 = elei2020.loc[elei2020['NM_MUNICIPIO']
                               == tuple(regiao_bragantina)]

    if year == 2022:
        vanguarda2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            cobertura_vanguarda)]
        valep2022 = elei2022.loc[elei2022['NM_MUNICIPIO']
                                 == tuple(vale_do_paraiba)]
        valeh2022 = elei2022.loc[elei2022['NM_MUNICIPIO']
                                 == tuple(vale_historico)]
        litoraln2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            litoral_norte)]
        serram2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            serra_da_mantiqueira)]
        regiaob2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            regiao_bragantina)]

    elif year == 2024:
        vanguarda2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            cobertura_vanguarda)]
        vanguarda2024 = elei2024.loc[elei2024['NM_MUNICIPIO'] == tuple(
            cobertura_vanguarda)]
        valep2022 = elei2022.loc[elei2022['NM_MUNICIPIO']
                                 == tuple(vale_do_paraiba)]
        valep2024 = elei2024.loc[elei2024['NM_MUNICIPIO']
                                 == tuple(vale_do_paraiba)]
        valeh2022 = elei2022.loc[elei2022['NM_MUNICIPIO']
                                 == tuple(vale_historico)]
        valeh2024 = elei2024.loc[elei2024['NM_MUNICIPIO']
                                 == tuple(vale_historico)]
        litoraln2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            litoral_norte)]
        litoraln2024 = elei2024.loc[elei2024['NM_MUNICIPIO'] == tuple(
            litoral_norte)]
        serram2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            serra_da_mantiqueira)]
        serram2024 = elei2024.loc[elei2024['NM_MUNICIPIO'] == tuple(
            serra_da_mantiqueira)]
        regiaob2022 = elei2022.loc[elei2022['NM_MUNICIPIO'] == tuple(
            regiao_bragantina)]
        regiaob2024 = elei2024.loc[elei2024['NM_MUNICIPIO'] == tuple(
            regiao_bragantina)]

    # Preenchendo os DataFrames com dados de cada região:
    for x in cobertura_vanguarda:
        vanguarda2014 = vanguarda2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in cobertura_vanguarda:
        vanguarda2016 = vanguarda2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in cobertura_vanguarda:
        vanguarda2018 = vanguarda2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in cobertura_vanguarda:
        vanguarda2020 = vanguarda2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])

    for x in vale_do_paraiba:
        valep2014 = valep2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in vale_do_paraiba:
        valep2016 = valep2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in vale_do_paraiba:
        valep2018 = valep2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in vale_do_paraiba:
        valep2020 = valep2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])

    for x in vale_historico:
        valeh2014 = valeh2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in vale_historico:
        valeh2016 = valeh2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in vale_historico:
        valeh2018 = valeh2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in vale_historico:
        valeh2020 = valeh2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])

    for x in litoral_norte:
        litoraln2014 = litoraln2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in litoral_norte:
        litoraln2016 = litoraln2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in litoral_norte:
        litoraln2018 = litoraln2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in litoral_norte:
        litoraln2020 = litoraln2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])

    for x in serra_da_mantiqueira:
        serram2014 = serram2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in serra_da_mantiqueira:
        serram2016 = serram2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in serra_da_mantiqueira:
        serram2018 = serram2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in serra_da_mantiqueira:
        serram2020 = serram2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])

    for x in regiao_bragantina:
        regiaob2014 = regiaob2014.append(
            elei2014.loc[elei2014['NM_MUNICIPIO'] == x])
    for x in regiao_bragantina:
        regiaob2016 = regiaob2016.append(
            elei2016.loc[elei2016['NM_MUNICIPIO'] == x])
    for x in regiao_bragantina:
        regiaob2018 = regiaob2018.append(
            elei2018.loc[elei2018['NM_MUNICIPIO'] == x])
    for x in regiao_bragantina:
        regiaob2020 = regiaob2020.append(
            elei2020.loc[elei2020['NM_MUNICIPIO'] == x])
    if year == 2022:
        for x in cobertura_vanguarda:
            vanguarda2022 = vanguarda2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in vale_do_paraiba:
            valep2022 = valep2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in vale_historico:
            valeh2022 = valeh2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in litoral_norte:
            litoraln2022 = litoraln2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in serra_da_mantiqueira:
            serram2022 = serram2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in regiao_bragantina:
            regiaob2022 = regiaob2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])

    elif year == 2024:
        for x in cobertura_vanguarda:
            vanguarda2022 = vanguarda2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in vale_do_paraiba:
            valep2022 = valep2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in vale_historico:
            valeh2022 = valeh2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in litoral_norte:
            litoraln2022 = litoraln2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in serra_da_mantiqueira:
            serram2022 = serram2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])
        for x in regiao_bragantina:
            regiaob2022 = regiaob2022.append(
                elei2022.loc[elei2022['NM_MUNICIPIO'] == x])

        for x in cobertura_vanguarda:
            vanguarda2024 = vanguarda2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])
        for x in vale_do_paraiba:
            valep2024 = valep2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])
        for x in vale_historico:
            valeh2024 = valeh2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])
        for x in litoral_norte:
            litoraln2024 = litoraln2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])
        for x in serra_da_mantiqueira:
            serram2024 = serram2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])
        for x in regiao_bragantina:
            regiaob2024 = regiaob2024.append(
                elei2024.loc[elei2024['NM_MUNICIPIO'] == x])

    # Estruturando a resposta da função
    if year == 2022:
        dados_vanguarda = {"2014": int(vanguarda2014[['QTD_ELEITORES']].sum(axis=0)),
                           "2016": int(vanguarda2016[['QTD_ELEITORES']].sum(axis=0)),
                           "2018": int(vanguarda2018[['QTD_ELEITORES']].sum(axis=0)),
                           "2020": int(vanguarda2020[['QTD_ELEITORES']].sum(axis=0)),
                           "2022": int(vanguarda2022[['QTD_ELEITORES']].sum(axis=0))}

        dados_valep = {"2014": int(valep2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valep2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valep2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valep2020[['QTD_ELEITORES']].sum(axis=0)),
                       "2022": int(valep2022[['QTD_ELEITORES']].sum(axis=0))}

        dados_valeh = {"2014": int(valeh2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valeh2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valeh2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valeh2020[['QTD_ELEITORES']].sum(axis=0)),
                       "2022": int(valeh2022[['QTD_ELEITORES']].sum(axis=0))}

        dados_litoraln = {"2014": int(litoraln2014[['QTD_ELEITORES']].sum(axis=0)),
                          "2016": int(litoraln2016[['QTD_ELEITORES']].sum(axis=0)),
                          "2018": int(litoraln2018[['QTD_ELEITORES']].sum(axis=0)),
                          "2020": int(litoraln2020[['QTD_ELEITORES']].sum(axis=0)),
                          "2022": int(litoraln2022[['QTD_ELEITORES']].sum(axis=0))}

        dados_serram = {"2014": int(serram2014[['QTD_ELEITORES']].sum(axis=0)),
                        "2016": int(serram2016[['QTD_ELEITORES']].sum(axis=0)),
                        "2018": int(serram2018[['QTD_ELEITORES']].sum(axis=0)),
                        "2020": int(serram2020[['QTD_ELEITORES']].sum(axis=0)),
                        "2022": int(serram2022[['QTD_ELEITORES']].sum(axis=0))}

        dados_regiaob = {"2014": int(regiaob2014[['QTD_ELEITORES']].sum(axis=0)),
                         "2016": int(regiaob2016[['QTD_ELEITORES']].sum(axis=0)),
                         "2018": int(regiaob2018[['QTD_ELEITORES']].sum(axis=0)),
                         "2020": int(regiaob2020[['QTD_ELEITORES']].sum(axis=0)),
                         "2022": int(regiaob2022[['QTD_ELEITORES']].sum(axis=0))}

    elif year == 2024:
        dados_vanguarda = {"2014": int(vanguarda2014[['QTD_ELEITORES']].sum(axis=0)),
                           "2016": int(vanguarda2016[['QTD_ELEITORES']].sum(axis=0)),
                           "2018": int(vanguarda2018[['QTD_ELEITORES']].sum(axis=0)),
                           "2020": int(vanguarda2020[['QTD_ELEITORES']].sum(axis=0)),
                           "2022": int(vanguarda2022[['QTD_ELEITORES']].sum(axis=0)),
                           "2024": int(vanguarda2024[['QTD_ELEITORES']].sum(axis=0))}

        dados_valep = {"2014": int(valep2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valep2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valep2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valep2020[['QTD_ELEITORES']].sum(axis=0)),
                       "2022": int(valep2022[['QTD_ELEITORES']].sum(axis=0)),
                       "2024": int(valep2024[['QTD_ELEITORES']].sum(axis=0))}

        dados_valeh = {"2014": int(valeh2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valeh2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valeh2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valeh2020[['QTD_ELEITORES']].sum(axis=0)),
                       "2022": int(valeh2022[['QTD_ELEITORES']].sum(axis=0)),
                       "2024": int(valeh2024[['QTD_ELEITORES']].sum(axis=0))}

        dados_litoraln = {"2014": int(litoraln2014[['QTD_ELEITORES']].sum(axis=0)),
                          "2016": int(litoraln2016[['QTD_ELEITORES']].sum(axis=0)),
                          "2018": int(litoraln2018[['QTD_ELEITORES']].sum(axis=0)),
                          "2020": int(litoraln2020[['QTD_ELEITORES']].sum(axis=0)),
                          "2022": int(litoraln2022[['QTD_ELEITORES']].sum(axis=0)),
                          "2024": int(litoraln2024[['QTD_ELEITORES']].sum(axis=0))}

        dados_serram = {"2014": int(serram2014[['QTD_ELEITORES']].sum(axis=0)),
                        "2016": int(serram2016[['QTD_ELEITORES']].sum(axis=0)),
                        "2018": int(serram2018[['QTD_ELEITORES']].sum(axis=0)),
                        "2020": int(serram2020[['QTD_ELEITORES']].sum(axis=0)),
                        "2022": int(serram2022[['QTD_ELEITORES']].sum(axis=0)),
                        "2024": int(serram2024[['QTD_ELEITORES']].sum(axis=0))}

        dados_regiaob = {"2014": int(regiaob2014[['QTD_ELEITORES']].sum(axis=0)),
                         "2016": int(regiaob2016[['QTD_ELEITORES']].sum(axis=0)),
                         "2018": int(regiaob2018[['QTD_ELEITORES']].sum(axis=0)),
                         "2020": int(regiaob2020[['QTD_ELEITORES']].sum(axis=0)),
                         "2022": int(regiaob2022[['QTD_ELEITORES']].sum(axis=0)),
                         "2024": int(regiaob2024[['QTD_ELEITORES']].sum(axis=0))}
    else:
        dados_vanguarda = {"2014": int(vanguarda2014[['QTD_ELEITORES']].sum(axis=0)),
                           "2016": int(
                           vanguarda2016[['QTD_ELEITORES']].sum(axis=0)),
                           "2018": int(
                           vanguarda2018[['QTD_ELEITORES']].sum(axis=0)),
                           "2020":  int(vanguarda2020[['QTD_ELEITORES']].sum(axis=0))}

        dados_valep = {"2014": int(valep2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valep2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valep2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valep2020[['QTD_ELEITORES']].sum(axis=0))}

        dados_valeh = {"2014": int(valeh2014[['QTD_ELEITORES']].sum(axis=0)),
                       "2016": int(valeh2016[['QTD_ELEITORES']].sum(axis=0)),
                       "2018": int(valeh2018[['QTD_ELEITORES']].sum(axis=0)),
                       "2020": int(valeh2020[['QTD_ELEITORES']].sum(axis=0))}

        dados_litoraln = {"2014": int(litoraln2014[['QTD_ELEITORES']].sum(axis=0)),
                          "2016": int(litoraln2016[['QTD_ELEITORES']].sum(axis=0)),
                          "2018": int(litoraln2018[['QTD_ELEITORES']].sum(axis=0)),
                          "2020": int(litoraln2020[['QTD_ELEITORES']].sum(axis=0))}

        dados_serram = {"2014": int(serram2014[['QTD_ELEITORES']].sum(axis=0)),
                        "2016": int(serram2016[['QTD_ELEITORES']].sum(axis=0)),
                        "2018": int(serram2018[['QTD_ELEITORES']].sum(axis=0)),
                        "2020": int(serram2020[['QTD_ELEITORES']].sum(axis=0))}

        dados_regiaob = {"2014": int(regiaob2014[['QTD_ELEITORES']].sum(axis=0)),
                         "2016": int(regiaob2016[['QTD_ELEITORES']].sum(axis=0)),
                         "2018": int(regiaob2018[['QTD_ELEITORES']].sum(axis=0)),
                         "2020": int(regiaob2020[['QTD_ELEITORES']].sum(axis=0))}

    cards = {"Vanguarda": dados_vanguarda, "ValeParaiba": dados_valep,
             "ValeHistorico": dados_valeh, "Litoral": dados_litoraln,
             "Serra": dados_serram, "RegiaoBragantina": dados_regiaob}
    print(cards)
    return cards
