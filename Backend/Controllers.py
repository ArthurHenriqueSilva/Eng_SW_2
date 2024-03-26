from Models import db, User, FolhaPagamento, Favorito
from sqlalchemy import func

class User_controller:
    @staticmethod
    def create_user(name, email, password):
        try:
            user = User(name=name, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, new_name=None, new_email=None, new_password=None):
        try:
            user = User.query.get(user_id)
            if not user: return False
            if new_name: user.name = new_name
            if new_email: user.email = new_email
            if new_password: user.set_password(new_password)
            db.session.commit()
            return user
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user: return False
            db.session.delete(user)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e

    @staticmethod
    def login(email, password):
        try:
            user = User.query.filter_by(email=email).first()
            if not user: return None
            if not user.check_password(password): return False
            return user
        except Exception as e:
            db.session.rollback()
            raise e

class Folha_Pagamento_Controller:
    
    @staticmethod
    def create_folha(mes, ano, nome, lotacao, cargo, remuneracao, vantagens, subsidio_comissao,
                    indenizacoes, vantagens_eventuais, gratificacoes, total_credito, previdencia_publica,
                    imposto_renda, descontos, retencao_teto, total_debitos, rendimento_liquido,
                    remuneracao_orgao_origem, diarias):
        try:
            folha = FolhaPagamento(mes=mes, ano=ano, nome=nome, lotacao=lotacao, cargo=cargo,
                                remuneracao=remuneracao, vantagens=vantagens,
                                subsidio_comissao=subsidio_comissao, indenizacoes=indenizacoes,
                                vantagens_eventuais=vantagens_eventuais, gratificacoes=gratificacoes,
                                total_credito=total_credito, previdencia_publica=previdencia_publica,
                                imposto_renda=imposto_renda, descontos=descontos,
                                retencao_teto=retencao_teto, total_debitos=total_debitos,
                                rendimento_liquido=rendimento_liquido,
                                remuneracao_orgao_origem=remuneracao_orgao_origem, diarias=diarias)
            db.session.add(folha)
            db.session.commit()
            return folha
        except Exception as e:
            db.session.rollback()
            raise e    
        
    @staticmethod
    def get_folha(mes, ano, nome, lotacao, cargo, remuneracao, vantagens, subsidio_comissao,
                    indenizacoes, vantagens_eventuais, gratificacoes, total_credito, previdencia_publica,
                    imposto_renda, descontos, retencao_teto, total_debitos, rendimento_liquido,
                    remuneracao_orgao_origem, diarias):
        
        query = FolhaPagamento.query

        try:        
            if mes is not None:
                query = query.filter(FolhaPagamento.mes == mes)
            if ano is not None:
                query = query.filter(FolhaPagamento.ano == ano)
            if nome is not None:
                query = query.filter(func.lower(FolhaPagamento.nome).ilike(func.lower(f'%{nome}%')))
            if lotacao is not None:
                query = query.filter(func.lower(FolhaPagamento.lotacao).ilike(func.lower(f'%{lotacao}%')))
            if cargo is not None:
                query = query.filter(func.lower(FolhaPagamento.cargo).ilike(func.lower(f'%{cargo}%')))
            if remuneracao is not None:
                query = query.filter(FolhaPagamento.remuneracao == remuneracao)
            if vantagens is not None:
                query = query.filter(FolhaPagamento.vantagens == vantagens)
            if subsidio_comissao is not None:
                query = query.filter(FolhaPagamento.subsidio_comissao == subsidio_comissao)
            if indenizacoes is not None:
                query = query.filter(FolhaPagamento.indenizacoes == indenizacoes)
            if vantagens_eventuais is not None:
                query = query.filter(FolhaPagamento.vantagens_eventuais == vantagens_eventuais)
            if gratificacoes is not None:
                query = query.filter(FolhaPagamento.gratificacoes == gratificacoes)
            if total_credito is not None:
                query = query.filter(FolhaPagamento.total_credito == total_credito)
            if previdencia_publica is not None:
                query = query.filter(FolhaPagamento.previdencia_publica == previdencia_publica)
            if imposto_renda is not None:
                query = query.filter(FolhaPagamento.imposto_renda == imposto_renda)
            if descontos is not None:
                query = query.filter(FolhaPagamento.descontos == descontos)
            if retencao_teto is not None:
                query = query.filter(FolhaPagamento.retencao_teto == retencao_teto)
            if total_debitos is not None:
                query = query.filter(FolhaPagamento.total_debitos == total_debitos)
            if rendimento_liquido is not None:
                query = query.filter(FolhaPagamento.rendimento_liquido == rendimento_liquido)
            if remuneracao_orgao_origem is not None:
                query = query.filter(FolhaPagamento.remuneracao_orgao_origem == remuneracao_orgao_origem)
            if diarias is not None:
                query = query.filter(FolhaPagamento.diarias == diarias)    
            return query.all()            
        except Exception as e:
            raise e 

class Consulta_Controller:

    def get_busca(self,mes=None, ano=None, lotacao=None, cargo=None, nome=None, lim_inferior_remun=None,
                 lim_superior_remun=None, id=None):
        query = FolhaPagamento.query

        if mes is not None:
            query = query.filter(FolhaPagamento.mes == mes)
        if ano is not None:
            query = query.filter(FolhaPagamento.ano == ano)
        if lotacao is not None:
            query = query.filter(FolhaPagamento.lotacao.ilike(func.lower(f'%{lotacao}%')))
        if cargo is not None:
            query = query.filter(FolhaPagamento.cargo.ilike(func.lower(f'%{cargo}%')))
        if nome is not None:
            query = query.filter(FolhaPagamento.nome.ilike(func.lower(f'%{nome}%')))
        if lim_inferior_remun is not None:
            query = query.filter(FolhaPagamento.remuneracao >= lim_inferior_remun)
        if lim_superior_remun is not None:
            query = query.filter(FolhaPagamento.remuneracao <= lim_superior_remun)
        if id is not None:
            query = query.filter(FolhaPagamento.id)
            
        return query.all()

class Favorito_Controller:
    
    @staticmethod
    def get_favoritos(id_owner):
        return Favorito.query.filter_by(id_owner=id_owner)
    
    @staticmethod
    def create_favorito(id_owner, mes, ano, tipo_servidor,
                        cargo, nome_servidor, 
                        limite_superior_remun, limite_inferior_remun):
        try:
          new_favorito = Favorito(id_owner=id_owner, mes=mes, ano=ano,
                                  tipo_servidor=tipo_servidor, cargo=cargo,
                                  nome_servidor=nome_servidor, 
                                  limite_superior_remun=limite_superior_remun, limite_inferior_remun=limite_inferior_remun)
          db.session().add(new_favorito)
          db.session().commit()
          return new_favorito
        except Exception as e:
          db.session.rollback()
          raise e
        
    @staticmethod
    def delete_favorito(id):
        try:
            favorito_to_delete = Favorito.query.get(id)
            if not favorito_to_delete: return False
            db.session.delete(favorito_to_delete)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e