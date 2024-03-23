import Controllers
from API import app

class UserTests:

    user_default_names = ["Freddie Mercury", "John Lennon", "Elvis Presley", "Michael Jackson", "David Bowie"]
    user_default_password = '12345'
    user_update_names = ["Freddie Mercury from Queen", "John Lennon from The Beatles", "Elvis Presley the King", "Michael Jackson the King of Pop", "David Bowie from Ziggy Stardust"]

    @staticmethod
    def generate_unique_email(username):
        return f"{username.replace(' ', '_')}@example.com"

    @staticmethod
    def test_create_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[0]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                assert user is not None
                assert user.name == user_default_name
                print("Test create_user passed.")
            except AssertionError as e:
                print("Test create_user failed:", e)

    @staticmethod
    def test_get_user_by_id():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[1]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                retrieved_user = Controllers.User_controller.get_user_by_id(user.id)
                assert retrieved_user is not None
                assert retrieved_user.name == user_default_name
                print("Test get_user_by_id passed.")
            except AssertionError as e:
                print("Test get_user_by_id failed:", e)

    @staticmethod
    def test_update_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[2]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                updated_user = Controllers.User_controller.update_user(user.id, UserTests.user_update_names[0])
                assert updated_user is not None
                assert updated_user.name == UserTests.user_update_names[0]
                print("Test update_user passed.")
            except AssertionError as e:
                print("Test update_user failed:", e)

    @staticmethod
    def test_delete_user():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[3]
                user_email = UserTests.generate_unique_email(user_default_name)
                user = Controllers.User_controller.create_user(user_default_name, user_email, UserTests.user_default_password)
                deleted = Controllers.User_controller.delete_user(user.id)
                assert deleted
                print("Test delete_user passed.")
            except AssertionError as e:
                print("Test delete_user failed:", e)
    
    @staticmethod
    def test_login():
        with app.app_context():
            try:
                user_default_name = UserTests.user_default_names[4]
                user_email = UserTests.generate_unique_email(user_default_name)
                response = app.test_client().post('/login', json={'email': user_email, 'password': UserTests.user_default_password})
                data = response.get_json()

                assert response.status_code == 200
                assert data['message'] == 'Login successful'

                user_data = data.get('user')
                assert user_data is not None
                assert 'id' in user_data
                assert 'name' in user_data
                assert 'email' in user_data

                print("Test login passed.")
            except AssertionError as e:
                print("Test login failed:", e)

    @staticmethod
    def run_all_tests():
        UserTests.test_create_user()
        UserTests.test_get_user_by_id()
        UserTests.test_update_user()
        UserTests.test_delete_user()

        print("All user tests completed.")

class FolhaTests:

    folha_default_mes = [1, 2, 3]
    folha_default_ano = [2024, 2023, 2022]
    folha_default_nome = ['ABDIAS LOPES PADRE', 'ABEDNIGO SILVA DA PAIXAO', 'ABELARDO DA SILVA BAHIA FILHO']
    folha_default_lotacao = ['JURISDICAO PLENA - BARRA DO CHOCA', 'VARA DO SISTEMA DOS JUIZADOS ESPECIAIS - SENHOR DO BONFIM', 'SALVADOR - SALVADOR']
    folha_default_cargo = ['ASSESSOR DE JUIZ - LEI 10.845/2007', 'TÉCNICO DE NÍVEL MÉDIO', 'OFICIAL DE JUSTIÇA AVALIADOR']
    folha_default_remuneracao = [5375.56, 5140.75, 10703.25]
    folha_default_vantagens = [2617.27, 2134.94, 5957.84]
    folha_default_subsidio_comissao = [1746.36, 0.00, 0.00]
    folha_default_indenizacoes = [2306.31, 2614.78, 0.00]
    folha_default_vantagens_eventuais = [7834.52, 7928.63, 0.00]
    folha_default_gratificacoes = [5821.21, 0.00, 0.00]
    folha_default_total_credito = [25094.92, 16904.32, 16661.09]
    folha_default_previdencia_publica = [2176.16, 1003.62, 1739.51]
    folha_default_imposto_renda = [2624.81, 1822.02, 2642.74]
    folha_default_descontos = [0.00, 0.00, 0.00]
    folha_default_retencao_teto = [0.00, 0.00, 0.00]
    folha_default_total_debitos = [4800.97, 2917.05, 4382.25]
    folha_default_rendimento_liquido = [20293.95, 13987.27, 12278.84]
    folha_default_remuneracao_orgao_origem = [0.00, 0.00, 0.00]
    folha_default_diarias = [0.00, 0.00, 0.00]

    @staticmethod
    def test_create_folha():
        with app.app_context():
            try:
                folha_default_mes = FolhaTests.folha_default_mes[0]
                folha_default_ano = FolhaTests.folha_default_ano[0]
                folha_default_nome = FolhaTests.folha_default_nome[0]
                folha_default_lotacao = FolhaTests.folha_default_lotacao[0]
                folha_default_cargo = FolhaTests.folha_default_cargo[0]
                folha_default_remuneracao = FolhaTests.folha_default_remuneracao[0]
                folha_default_vantagens = FolhaTests.folha_default_vantagens[0]
                folha_default_subsidio_comissao = FolhaTests.folha_default_subsidio_comissao[0]
                folha_default_indenizacoes = FolhaTests.folha_default_indenizacoes[0]
                folha_default_vantagens_eventuais = FolhaTests.folha_default_vantagens_eventuais[0]
                folha_default_gratificacoes = FolhaTests.folha_default_gratificacoes[0]
                folha_default_total_credito = FolhaTests.folha_default_total_credito[0]
                folha_default_previdencia_publica = FolhaTests.folha_default_previdencia_publica[0]
                folha_default_imposto_renda = FolhaTests.folha_default_imposto_renda[0]
                folha_default_descontos = FolhaTests.folha_default_descontos[0]
                folha_default_retencao_teto = FolhaTests.folha_default_retencao_teto[0]
                folha_default_total_debitos = FolhaTests.folha_default_total_debitos[0]
                folha_default_rendimento_liquido = FolhaTests.folha_default_rendimento_liquido[0]
                folha_default_remuneracao_orgao_origem = FolhaTests.folha_default_remuneracao_orgao_origem[0]
                folha_default_diarias = FolhaTests.folha_default_diarias[0]

                folha = Controllers.Folha_Pagamento_Controller.create_folha(folha_default_mes, folha_default_ano, folha_default_nome,
                                                                folha_default_lotacao, folha_default_cargo, folha_default_remuneracao,
                                                                folha_default_vantagens, folha_default_subsidio_comissao,
                                                                folha_default_indenizacoes, folha_default_vantagens_eventuais, folha_default_gratificacoes,
                                                                folha_default_total_credito, folha_default_previdencia_publica,
                                                                folha_default_imposto_renda, folha_default_descontos, folha_default_retencao_teto,
                                                                folha_default_total_debitos, folha_default_rendimento_liquido,
                                                                folha_default_remuneracao_orgao_origem, folha_default_diarias)
                assert folha is not None
                print("Test create_folha passed.")
            except AssertionError as e:
                print("Test create_folha failed:", e)

    @staticmethod
    def test_get_folha():
        with app.app_context():
            try:
                folha_default_mes = FolhaTests.folha_default_mes[0]
                folha_default_ano = FolhaTests.folha_default_ano[0]
                folha_default_nome = FolhaTests.folha_default_nome[0]
                folha_default_lotacao = FolhaTests.folha_default_lotacao[0]
                folha_default_cargo = FolhaTests.folha_default_cargo[0]
                folha_default_remuneracao = FolhaTests.folha_default_remuneracao[0]
                folha_default_vantagens = FolhaTests.folha_default_vantagens[0]
                folha_default_subsidio_comissao = FolhaTests.folha_default_subsidio_comissao[0]
                folha_default_indenizacoes = FolhaTests.folha_default_indenizacoes[0]
                folha_default_vantagens_eventuais = FolhaTests.folha_default_vantagens_eventuais[0]
                folha_default_gratificacoes = FolhaTests.folha_default_gratificacoes[0]
                folha_default_total_credito = FolhaTests.folha_default_total_credito[0]
                folha_default_previdencia_publica = FolhaTests.folha_default_previdencia_publica[0]
                folha_default_imposto_renda = FolhaTests.folha_default_imposto_renda[0]
                folha_default_descontos = FolhaTests.folha_default_descontos[0]
                folha_default_retencao_teto = FolhaTests.folha_default_retencao_teto[0]
                folha_default_total_debitos = FolhaTests.folha_default_total_debitos[0]
                folha_default_rendimento_liquido = FolhaTests.folha_default_rendimento_liquido[0]
                folha_default_remuneracao_orgao_origem = FolhaTests.folha_default_remuneracao_orgao_origem[0]
                folha_default_diarias = FolhaTests.folha_default_diarias[0]

                folha = Controllers.Folha_Pagamento_Controller.create_folha(folha_default_mes, folha_default_ano, folha_default_nome,
                                                                folha_default_lotacao, folha_default_cargo, folha_default_remuneracao,
                                                                folha_default_vantagens, folha_default_subsidio_comissao,
                                                                folha_default_indenizacoes, folha_default_vantagens_eventuais, folha_default_gratificacoes,
                                                                folha_default_total_credito, folha_default_previdencia_publica,
                                                                folha_default_imposto_renda, folha_default_descontos, folha_default_retencao_teto,
                                                                folha_default_total_debitos, folha_default_rendimento_liquido,
                                                                folha_default_remuneracao_orgao_origem, folha_default_diarias)
                retrieved_folha = Controllers.Folha_Pagamento_Controller.get_folha(folha.mes, folha.ano, folha.nome, folha.lotacao, folha.cargo,
                                                                                   folha.remuneracao, folha.vantagens, folha.subsidio_comissao,
                                                                                   folha.indenizacoes, folha.vantagens_eventuais, folha.gratificacoes,
                                                                                   folha.total_credito, folha.previdencia_publica,
                                                                                   folha.imposto_renda, folha.descontos, folha.retencao_teto, folha.total_debitos,
                                                                                   folha.rendimento_liquido,folha.remuneracao_orgao_origem, folha.diarias)
                assert retrieved_folha is not None
                print("Test get_folha passed.")
            except AssertionError as e:
                print("Test get_folha failed:", e)
    
    @staticmethod
    def test_get_folha_by_nome():
        with app.app_context():
            try:
                folha_default_mes = FolhaTests.folha_default_mes[1]
                folha_default_ano = FolhaTests.folha_default_ano[1]
                folha_default_nome = FolhaTests.folha_default_nome[1]
                folha_default_lotacao = FolhaTests.folha_default_lotacao[1]
                folha_default_cargo = FolhaTests.folha_default_cargo[1]
                folha_default_remuneracao = FolhaTests.folha_default_remuneracao[1]
                folha_default_vantagens = FolhaTests.folha_default_vantagens[1]
                folha_default_subsidio_comissao = FolhaTests.folha_default_subsidio_comissao[1]
                folha_default_indenizacoes = FolhaTests.folha_default_indenizacoes[1]
                folha_default_vantagens_eventuais = FolhaTests.folha_default_vantagens_eventuais[1]
                folha_default_gratificacoes = FolhaTests.folha_default_gratificacoes[1]
                folha_default_total_credito = FolhaTests.folha_default_total_credito[1]
                folha_default_previdencia_publica = FolhaTests.folha_default_previdencia_publica[1]
                folha_default_imposto_renda = FolhaTests.folha_default_imposto_renda[1]
                folha_default_descontos = FolhaTests.folha_default_descontos[1]
                folha_default_retencao_teto = FolhaTests.folha_default_retencao_teto[1]
                folha_default_total_debitos = FolhaTests.folha_default_total_debitos[1]
                folha_default_rendimento_liquido = FolhaTests.folha_default_rendimento_liquido[1]
                folha_default_remuneracao_orgao_origem = FolhaTests.folha_default_remuneracao_orgao_origem[1]
                folha_default_diarias = FolhaTests.folha_default_diarias[1]

                folha = Controllers.Folha_Pagamento_Controller.create_folha(folha_default_mes, folha_default_ano, folha_default_nome,
                                                                folha_default_lotacao, folha_default_cargo, folha_default_remuneracao,
                                                                folha_default_vantagens, folha_default_subsidio_comissao,
                                                                folha_default_indenizacoes, folha_default_vantagens_eventuais, folha_default_gratificacoes,
                                                                folha_default_total_credito, folha_default_previdencia_publica,
                                                                folha_default_imposto_renda, folha_default_descontos, folha_default_retencao_teto,
                                                                folha_default_total_debitos, folha_default_rendimento_liquido,
                                                                folha_default_remuneracao_orgao_origem, folha_default_diarias)
                retrieved_folha = Controllers.Folha_Pagamento_Controller.get_folha(None, None,folha.nome, None, None,
                                                                                   None, None, None, None, None, None, None,
                                                                                   None, None, None, None, None, None, None, None)
                assert retrieved_folha is not None
                print("Test get_folha_by_nome passed.")
            except AssertionError as e:
                print("Test get_folha_by_nome failed:", e)

    @staticmethod
    def test_get_folha_by_mes_ano():
        with app.app_context():
            try:
                folha_default_mes = FolhaTests.folha_default_mes[2]
                folha_default_ano = FolhaTests.folha_default_ano[2]
                folha_default_nome = FolhaTests.folha_default_nome[2]
                folha_default_lotacao = FolhaTests.folha_default_lotacao[2]
                folha_default_cargo = FolhaTests.folha_default_cargo[2]
                folha_default_remuneracao = FolhaTests.folha_default_remuneracao[2]
                folha_default_vantagens = FolhaTests.folha_default_vantagens[2]
                folha_default_subsidio_comissao = FolhaTests.folha_default_subsidio_comissao[2]
                folha_default_indenizacoes = FolhaTests.folha_default_indenizacoes[2]
                folha_default_vantagens_eventuais = FolhaTests.folha_default_vantagens_eventuais[2]
                folha_default_gratificacoes = FolhaTests.folha_default_gratificacoes[2]
                folha_default_total_credito = FolhaTests.folha_default_total_credito[2]
                folha_default_previdencia_publica = FolhaTests.folha_default_previdencia_publica[2]
                folha_default_imposto_renda = FolhaTests.folha_default_imposto_renda[2]
                folha_default_descontos = FolhaTests.folha_default_descontos[2]
                folha_default_retencao_teto = FolhaTests.folha_default_retencao_teto[2]
                folha_default_total_debitos = FolhaTests.folha_default_total_debitos[2]
                folha_default_rendimento_liquido = FolhaTests.folha_default_rendimento_liquido[2]
                folha_default_remuneracao_orgao_origem = FolhaTests.folha_default_remuneracao_orgao_origem[2]
                folha_default_diarias = FolhaTests.folha_default_diarias[2]

                folha = Controllers.Folha_Pagamento_Controller.create_folha(folha_default_mes, folha_default_ano, folha_default_nome,
                                                                folha_default_lotacao, folha_default_cargo, folha_default_remuneracao,
                                                                folha_default_vantagens, folha_default_subsidio_comissao,
                                                                folha_default_indenizacoes, folha_default_vantagens_eventuais, folha_default_gratificacoes,
                                                                folha_default_total_credito, folha_default_previdencia_publica,
                                                                folha_default_imposto_renda, folha_default_descontos, folha_default_retencao_teto,
                                                                folha_default_total_debitos, folha_default_rendimento_liquido,
                                                                folha_default_remuneracao_orgao_origem, folha_default_diarias)
                retrieved_folha = Controllers.Folha_Pagamento_Controller.get_folha(folha.mes, folha.ano, None, None, None,
                                                                                   None, None, None, None, None, None, None,
                                                                                   None, None, None, None, None, None, None, None)
                assert retrieved_folha is not None
                print("Test get_folha_by_mes_ano passed.")
            except AssertionError as e:
                print("Test get_folha_by_mes_ano failed:", e)

    @staticmethod
    def run_all_tests():
        FolhaTests.test_create_folha()
        FolhaTests.test_get_folha()
        FolhaTests.test_get_folha_by_mes_ano()
        FolhaTests.test_get_folha_by_nome()

        print("All folha tests completed.")


if __name__ == '__main__':
    UserTests.run_all_tests()
    FolhaTests.run_all_tests()
