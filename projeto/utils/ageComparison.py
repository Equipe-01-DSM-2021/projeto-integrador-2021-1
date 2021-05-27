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

col_eleitorado = ["ANO_ELEICAO", "SG_UF", "NM_MUNICIPIO", "DS_ESTADO_CIVIL",
                  "CD_FAIXA_ETARIA", "DS_FAIXA_ETARIA", "CD_GRAU_ESCOLARIDADE",
                  "DS_GRAU_ESCOLARIDADE", "QT_ELEITORES_PERFIL",
                  "QT_ELEITORES_INC_NM_SOCIAL"]


def ageComparisonYoung(year, csvPath):

    dfe = pd.read_csv(csvPath, usecols=col_eleitorado,
                      sep=';', encoding='iso-8859-1', error_bad_lines=False)

    # Cria um dataframe acumulador vazio
    dfm = pd.DataFrame(columns=["Macrorregião", "Município",
                       "Jovens_pct", "Jovens_abs", "Idosos_pct", "Idosos_abs"])

    # Calcula a porcentagem de eleitores jovens e idosos em cada município
    for cidade in CoberturaVanguarda.keys():
        filtroCidade = dfe.query("NM_MUNICIPIO == @cidade")
        filtroEleitoresTotal = filtroCidade['QT_ELEITORES_PERFIL'].sum()
        filtroEleitoresFaixaEtaria = filtroCidade.groupby(
            ['DS_FAIXA_ETARIA'])['QT_ELEITORES_PERFIL'].sum()

        # Eleitores Jovens
        f18anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '18 anos')]).values
        f19anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '19 anos')]).values
        f20anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '20 anos')]).values
        f21anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '21 a 24 anos')]).values
        f25anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '25 a 29 anos')]).values

    # Caso alguma faixa etária não exista no município analisado,
        # é atribuído o valor 0 à ela, para não atrapalhar nos cálculos.
        if len(f18anos) == 0:
            f18anos = 0
        if len(f19anos) == 0:
            f19anos = 0
        if len(f20anos) == 0:
            f20anos = 0
        if len(f21anos) == 0:
            f20anos = 0
        if len(f25anos) == 0:
            f20anos = 0

        # Output do cálculo
        abs_jovens = f18anos + f19anos + f20anos + f21anos + f25anos
        pct_jovens = abs_jovens / filtroEleitoresTotal

        # Gravando a cidade no dataframe acumulador
        dft = pd.DataFrame({"Macrorregião": [CoberturaVanguarda[cidade]], "Município": [cidade], "Jovens_pct": [
                           pct_jovens], "Jovens_abs": [abs_jovens]})
        dfm = dfm.append(dft)

    # Número de muncípios que aparecerão no ranking
    top = 3

    # Ranking de municípios com mais jovens
    topJovens = dfm[['Macrorregião', 'Município', 'Jovens_pct', 'Jovens_abs']]
    topJovensCoberturaVanguarda = topJovens.sort_values(
        "Jovens_pct", ascending=False).head(top)
    topJovensValeParaiba = topJovens.query('Macrorregião == "VALE DO PARAÍBA"').sort_values(
        "Jovens_pct", ascending=False).head(top)
    topJovensValeHistorico = topJovens.query('Macrorregião == "VALE HISTÓRICO"').sort_values(
        "Jovens_pct", ascending=False).head(top)
    topJovensLitoralNorte = topJovens.query('Macrorregião == "LITORAL NORTE"').sort_values(
        "Jovens_pct", ascending=False).head(top)
    topJovensSerraMantiqueira = topJovens.query(
        'Macrorregião == "SERRA DA MANTIQUEIRA"').sort_values("Jovens_pct", ascending=False).head(top)
    topJovensRegiaoBragantina = topJovens.query(
        'Macrorregião == "REGIÃO BRAGANTINA"').sort_values("Jovens_pct", ascending=False).head(top)

    # JOVENS POR REGIÃO
    # Cobertura Vanguarda
    topJovensCoberturaVanguardaMunicipio = topJovensCoberturaVanguarda.Município.tolist()
    topJovensCoberturaVanguardaPorcentagem = np.concatenate(
        topJovensCoberturaVanguarda.Jovens_pct.tolist(), axis=0)
    topJovensCoberturaVanguardaAbsoluto = np.concatenate(
        topJovensCoberturaVanguarda.Jovens_abs.tolist(), axis=0)

    # Vale do Paraíba
    topJovensValeParaibaMunicipio = topJovensValeParaiba.Município.tolist()
    topJovensValeParaibaPorcentagem = np.concatenate(
        topJovensValeParaiba.Jovens_pct.tolist(), axis=0)
    topJovensValeParaibaAbsoluto = np.concatenate(
        topJovensValeParaiba.Jovens_abs.tolist(), axis=0)

    # Vale Histórico
    topJovensValeHistoricoMunicipio = topJovensValeHistorico.Município.tolist()
    topJovensValeHistoricoPorcentagem = np.concatenate(
        topJovensValeHistorico.Jovens_pct.tolist(), axis=0)
    topJovensValeHistoricoAbsoluto = np.concatenate(
        topJovensValeHistorico.Jovens_abs.tolist(), axis=0)

    # Litoral Norte
    topJovensLitoralNorteMunicipio = topJovensLitoralNorte.Município.tolist()
    topJovensLitoralNortePorcentagem = np.concatenate(
        topJovensLitoralNorte.Jovens_pct.tolist(), axis=0)
    topJovensLitoralNorteAbsoluto = np.concatenate(
        topJovensLitoralNorte.Jovens_abs.tolist(), axis=0)

    # Serra da Mantiqueira
    topJovensSerraMantiqueiraMunicipio = topJovensSerraMantiqueira.Município.tolist()
    topJovensSerraMantiqueiraPorcentagem = np.concatenate(
        topJovensSerraMantiqueira.Jovens_pct.tolist(), axis=0)
    topJovensSerraMantiqueiraAbsoluto = np.concatenate(
        topJovensSerraMantiqueira.Jovens_abs.tolist(), axis=0)

    # Região Bragantina
    topJovensRegiaoBragantinaMunicipio = topJovensRegiaoBragantina.Município.tolist()
    topJovensRegiaoBragantinaPorcentagem = np.concatenate(
        topJovensRegiaoBragantina.Jovens_pct.tolist(), axis=0)
    topJovensRegiaoBragantinaAbsoluto = np.concatenate(
        topJovensRegiaoBragantina.Jovens_abs.tolist(), axis=0)

    # RETORNO DA FUNÇÃO

    # ESTRUTURA DA ReSPOSTA
    vanguarda = {"Cidades": topJovensCoberturaVanguardaMunicipio,
                 "Quantia": str(topJovensCoberturaVanguardaAbsoluto).strip('[]').split(),
                 "Porcentagem": str(topJovensCoberturaVanguardaPorcentagem).strip('[]').split()}

    valeParaiba = {"Cidades": topJovensValeParaibaMunicipio,
                   "Quantia": str(topJovensValeParaibaAbsoluto).strip('[]').split(),
                   "Porcentagem": str(topJovensValeParaibaPorcentagem).strip('[]').split()}

    valeHistorico = {"Cidades": topJovensValeHistoricoMunicipio,
                     "Quantia": str(topJovensValeHistoricoAbsoluto).strip('[]').split(),
                     "Porcentagem": str(topJovensValeHistoricoPorcentagem).strip('[]').split()}

    litoralNorte = {"Cidades": topJovensLitoralNorteMunicipio,
                    "Quantia": str(topJovensLitoralNorteAbsoluto).strip('[]').split(),
                    "Porcentagem": str(topJovensLitoralNortePorcentagem).strip('[]').split()}

    serraMantiqueira = {"Cidades": topJovensSerraMantiqueiraMunicipio,
                        "Quantia": str(topJovensSerraMantiqueiraAbsoluto).strip('[]').split(),
                        "Porcentagem": str(topJovensSerraMantiqueiraPorcentagem).strip('[]').split()}

    regiaoBragantina = {"Cidades": topJovensRegiaoBragantinaMunicipio,
                        "Quantia": str(topJovensRegiaoBragantinaAbsoluto).strip('[]').split(),
                        "Porcentagem": str(topJovensRegiaoBragantinaPorcentagem).strip('[]').split()}

    cards = {"Vanguarda": vanguarda, "ValeParaiba": valeParaiba, "ValeHistorico": valeHistorico,
             "Litoral": litoralNorte, "Serra": serraMantiqueira, "RegiaoBragantina": regiaoBragantina}

    print(cards)
    return cards


def ageComparisonSenior(year, csvPath):

    dfe = pd.read_csv(csvPath, usecols=col_eleitorado,
                      sep=';', encoding='iso-8859-1', error_bad_lines=False)

    # Cria um dataframe acumulador vazio
    dfm = pd.DataFrame(columns=["Macrorregião", "Município",
                       "Jovens_pct", "Jovens_abs", "Idosos_pct", "Idosos_abs"])

    # Calcula a porcentagem de eleitores jovens e idosos em cada município
    for cidade in CoberturaVanguarda.keys():
        filtroCidade = dfe.query("NM_MUNICIPIO == @cidade")
        filtroEleitoresTotal = filtroCidade['QT_ELEITORES_PERFIL'].sum()
        filtroEleitoresFaixaEtaria = filtroCidade.groupby(
            ['DS_FAIXA_ETARIA'])['QT_ELEITORES_PERFIL'].sum()

        # Eleitores Idosos
        f60anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '60 a 64 anos')]).values
        f65anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '65 a 69 anos')]).values
        f70anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '70 a 74 anos')]).values
        f75anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '75 a 79 anos')]).values
        f80anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '80 a 84 anos')]).values
        f85anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '85 a 89 anos')]).values
        f90anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '90 a 94 anos')]).values
        f95anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '95 a 99 anos')]).values
        f100anos = (filtroEleitoresFaixaEtaria[filtroEleitoresFaixaEtaria.index.str.startswith(
            '100 anos ou mais')]).values

        # Caso alguma faixa etária não exista no município analisado,
        # é atribuído o valor 0 à ela, para não atrapalhar nos cálculos.
        if len(f60anos) == 0:
            f60anos = 0
        if len(f65anos) == 0:
            f65anos = 0
        if len(f70anos) == 0:
            f70anos = 0
        if len(f75anos) == 0:
            f75anos = 0
        if len(f80anos) == 0:
            f80anos = 0
        if len(f85anos) == 0:
            f85anos = 0
        if len(f90anos) == 0:
            f90anos = 0
        if len(f95anos) == 0:
            f95anos = 0
        if len(f100anos) == 0:
            f100anos = 0

        # Output do cálculo
        abs_idosos = f60anos + f65anos + f70anos + f75anos + \
            f80anos + f85anos + f90anos + f95anos + f100anos
        pct_idosos = abs_idosos / filtroEleitoresTotal

        # Gravando a cidade no dataframe acumulador
        dft = pd.DataFrame({"Macrorregião": [CoberturaVanguarda[cidade]],
                            "Município": [cidade], "Idosos_pct": [pct_idosos],
                            "Idosos_abs": [abs_idosos]})
        dfm = dfm.append(dft)

    # Número de muncípios que aparecerão no ranking
    top = 3

    # Ranking de municípios com mais idosos
    topIdosos = dfm[['Macrorregião', 'Município', 'Idosos_pct', 'Idosos_abs']]
    topIdososCoberturaVanguarda = topIdosos.sort_values(
        "Idosos_pct", ascending=False).head(top)
    topIdososValeParaiba = topIdosos.query('Macrorregião == "VALE DO PARAÍBA"').sort_values(
        "Idosos_pct", ascending=False).head(top)
    topIdososValeHistorico = topIdosos.query('Macrorregião == "VALE HISTÓRICO"').sort_values(
        "Idosos_pct", ascending=False).head(top)
    topIdososLitoralNorte = topIdosos.query('Macrorregião == "LITORAL NORTE"').sort_values(
        "Idosos_pct", ascending=False).head(top)
    topIdososSerraMantiqueira = topIdosos.query(
        'Macrorregião == "SERRA DA MANTIQUEIRA"').sort_values("Idosos_pct", ascending=False).head(top)
    topIdososRegiaoBragantina = topIdosos.query(
        'Macrorregião == "REGIÃO BRAGANTINA"').sort_values("Idosos_pct", ascending=False).head(top)

    # IDOSOS POR REGIÃO
    # Cobertura Vanguarda
    topIdososCoberturaVanguardaMunicipio = topIdososCoberturaVanguarda.Município.tolist()
    topIdososCoberturaVanguardaPorcentagem = np.concatenate(
        topIdososCoberturaVanguarda.Idosos_pct.tolist(), axis=0)
    topIdososCoberturaVanguardaAbsoluto = np.concatenate(
        topIdososCoberturaVanguarda.Idosos_abs.tolist(), axis=0)

    # Vale do Paraíba
    topIdososValeParaibaMunicipio = topIdososValeParaiba.Município.tolist()
    topIdososValeParaibaPorcentagem = np.concatenate(
        topIdososValeParaiba.Idosos_pct.tolist(), axis=0)
    topIdososValeParaibaAbsoluto = np.concatenate(
        topIdososValeParaiba.Idosos_abs.tolist(), axis=0)

    # Vale Histórico
    topIdososValeHistoricoMunicipio = topIdososValeHistorico.Município.tolist()
    topIdososValeHistoricoPorcentagem = np.concatenate(
        topIdososValeHistorico.Idosos_pct.tolist(), axis=0)
    topIdososValeHistoricoAbsoluto = np.concatenate(
        topIdososValeHistorico.Idosos_abs.tolist(), axis=0)

    # Litoral Norte
    topIdososLitoralNorteMunicipio = topIdososLitoralNorte.Município.tolist()
    topIdososLitoralNortePorcentagem = np.concatenate(
        topIdososLitoralNorte.Idosos_pct.tolist(), axis=0)
    topIdososLitoralNorteAbsoluto = np.concatenate(
        topIdososLitoralNorte.Idosos_abs.tolist(), axis=0)

    # Serra da Mantiqueira
    topIdososSerraMantiqueiraMunicipio = topIdososSerraMantiqueira.Município.tolist()
    topIdososSerraMantiqueiraPorcentagem = np.concatenate(
        topIdososSerraMantiqueira.Idosos_pct.tolist(), axis=0)
    topIdososSerraMantiqueiraAbsoluto = np.concatenate(
        topIdososSerraMantiqueira.Idosos_abs.tolist(), axis=0)

    # Região Bragantina
    topIdososRegiaoBragantinaMunicipio = topIdososRegiaoBragantina.Município.tolist()
    topIdososRegiaoBragantinaPorcentagem = np.concatenate(
        topIdososRegiaoBragantina.Idosos_pct.tolist(), axis=0)
    topIdososRegiaoBragantinaAbsoluto = np.concatenate(
        topIdososRegiaoBragantina.Idosos_abs.tolist(), axis=0)

    # RETORNO DA FUNÇÃO

    # ESTRUTURAS DA RESPOSTA
    vanguarda = {"Cidades": topIdososCoberturaVanguardaMunicipio,
                 "Quantia": str(topIdososCoberturaVanguardaAbsoluto).strip('[]').split(),
                 "Porcentagem": str(topIdososCoberturaVanguardaPorcentagem).strip('[]').split()}

    valeParaiba = {"Cidades": topIdososValeParaibaMunicipio,
                   "Quantia": str(topIdososValeParaibaAbsoluto).strip('[]').split(),
                   "Porcentagem": str(topIdososValeParaibaPorcentagem).strip('[]').split()}

    valeHistorico = {"Cidades": topIdososValeHistoricoMunicipio,
                     "Quantia": str(topIdososValeHistoricoAbsoluto).strip('[]').split(),
                     "Porcentagem": str(topIdososValeHistoricoPorcentagem).strip('[]').split()}

    litoralNorte = {"Cidades": topIdososLitoralNorteMunicipio,
                    "Quantia": str(topIdososLitoralNorteAbsoluto).strip('[]').split(),
                    "Porcentagem": str(topIdososLitoralNortePorcentagem).strip('[]').split()}

    serraMantiqueira = {"Cidades": topIdososSerraMantiqueiraMunicipio,
                        "Quantia": str(topIdososSerraMantiqueiraAbsoluto).strip('[]').split(),
                        "Porcentagem": str(topIdososSerraMantiqueiraPorcentagem).strip('[]').split()}

    regiaoBragantina = {"Cidades": topIdososRegiaoBragantinaMunicipio,
                        "Quantia": str(topIdososRegiaoBragantinaAbsoluto).strip('[]').split(),
                        "Porcentagem": str(topIdososRegiaoBragantinaPorcentagem).strip('[]').split()}

    cards = {"Vanguarda": vanguarda, "ValeParaiba": valeParaiba, "ValeHistorico": valeHistorico,
             "Litoral": litoralNorte, "Serra": serraMantiqueira, "RegiaoBragantina": regiaoBragantina}

    print(cards)
    return cards
