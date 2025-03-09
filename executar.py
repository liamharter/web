from flask import Flask, render_template, request

app = Flask(__name__)

# Página inicial onde o formulário é exibido
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Coletar os dados do formulário
        proposta_data = {
            'periodicidade_anual': request.form.get('pergunta1'),
            'periodicidade_mensal': request.form.get('pergunta2'),
            'calculo_parcelas': request.form.get('pergunta3'),
            'taxa_prefixada': request.form.get('pergunta4'),
            'taxa_5': request.form.get('pergunta5'),
            'seguro_prestamista': request.form.get('pergunta6'),
            'possui_avalistas': request.form.get('pergunta7'),
            'cadastro_avalistas_atualizado': request.form.get('pergunta8'),
            'informacoes_adicionais1': request.form.get('informacoes_adicionais'),
            
            # Painel do beneficiário
            'dap_valida': request.form.get('pergunta9'),
            'modulos_fiscais': request.form.get('pergunta10'),
            'renda_menor_500k': request.form.get('pergunta11'),
            'parecer_negocial': request.form.get('pergunta12'),
            'cadastro_atualizado_2025': request.form.get('pergunta13'),
            'informacoes_adicionais2': request.form.get('informacoes_adicionais2'),
            
            # Áreas beneficiadas
            'matriculas_espelhadas_mua': request.form.get('pergunta14'),
            'area_menor_igual_mua': request.form.get('pergunta15'),
            'matricula_arrendada': request.form.get('pergunta16'),
            'informacoes_adicionais3': request.form.get('informacoes_adicionais3'),
            
            # Documentação
            'car_presentes': request.form.get('pergunta17'),
            'area_consolidada_zerada': request.form.get('pergunta18'),
            'area_consolidada_menor': request.form.get('pergunta19'),
            'informacoes_adicionais4': request.form.get('informacoes_adicionais4'),
            
            # CND
            'cnd_valida': request.form.get('pergunta20'),
            'informacoes_adicionais5': request.form.get('informacoes_adicionais5'),
            
            # Protec
            'nome_associado': request.form.get('pergunta21'),
            'areas_beneficiadas_digiagro': request.form.get('pergunta22'),
            'operacao_traz_melhorias': request.form.get('pergunta23'),
            'atividade_principal_descrita': request.form.get('pergunta24'),
            'informacoes_adicionais6': request.form.get('informacoes_adicionais6'),
            
            # Equipamentos
            'equipamentos_novos_cfi': request.form.get('pergunta26'),
            'informacoes_adicionais7': request.form.get('informacoes_adicionais7'),
            
            # Digiagro
            'glebas_car_anexados': request.form.get('pergunta27'),
            'glebas_sobreposicao_necessaria': request.form.get('pergunta28'),
            'informacoes_adicionais8': request.form.get('informacoes_adicionais8'),
            
            # MUA
            'cor_etnia_preenchido': request.form.get('pergunta29'),
            'ocupacao_principal_agropecuaria': request.form.get('pergunta30'),
            'cnae_preenchido': request.form.get('pergunta31'),
            'informacoes_adicionais9': request.form.get('informacoes_adicionais9'),
        }
        
        # Após coletar os dados, renderize a página de resultados com os dados coletados
        return render_template('resultado.html', proposta_data=proposta_data)

    return render_template('index.html')

# Página para exibir os resultados
@app.route('/resultado', methods=['GET'])
def resultado():
    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
