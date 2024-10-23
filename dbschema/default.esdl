module default {

    abstract type People {
        required timestamp: datetime {
            default := datetime_of_statement();
        }
        required email: str {
            delegated constraint exclusive;
        };
        nome: str;
        sexo: str;
        estado_civil: str;
        details: str;
        tag_tipo: str;
        nascimento: datetime;

        multi telefone: Telefone {
            on source delete delete target if orphan;
            on target delete allow;
        };
        multi endereco: Endereco {
            on source delete delete target if orphan;
            on target delete allow;
        };
    }

    type Service {
        id_serviço: str;
        user: User;
        status: bool;
        valor: float32;
        categoria: str;
        details: str;
        custom: json;
        multi cliente_id: People;

        multi evento: Scheduler {
            on source delete delete target if orphan;
            on target delete allow;
        };
        finance: Finance {
            on source delete delete target if orphan;
            on target delete allow;
        }
        trigger log_update after update for each when (
            <json>__old__{*} != <json>__new__{*}
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json(
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                )
            }
        );

        trigger log_insert after insert for each do (
            insert Auditable {
                user_id := __new__.user_id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__{*}
            }
        );
    }

    type ServiceTemplate {
        user: User;
        name: str;
        fields: json;
    }

    type Telefone {
        tipo: str;
        ddd: str;
        numero: str;
        contato: str;
        details: str;
    }

    type Auditable {
        required timestamp: datetime {
            default := datetime_of_statement();
        };
        id_objeto: uuid;
        user: User;
        action: str;
        details: json;
    }

    type Scheduler {
        user: User;
        nome: str;
        status: bool {
            default:= false;
        };
        end_time: datetime;
        start_time: datetime;
        peridiocidade: str;
        details: str;
        tag_tipo: str;
        auto_change_status: true;
    }

    type Conta {
        bankName: str;
        agency: str;
        accountNumber: str;
        saldo: float32;
        tipo_conta: str;
    }

    type Endereco {
        rua: str;
        numero: str;
        complemento: str;
        bairro: str;
        cep: str;
        cidade: str;
        estado: str;
    }

    type PessoaFisica extending People {
        user: User;
        cpf: str;
        rg: str;
        pis: str;
        ctps: str;
        serie: str;
        nacionalidade: str;
        profissao: str;
        nome_mae: str;

        trigger log_update after update for each when (
            (
                <json>__old__ {*} != <json>__new__ {*}
            ) and (
                __old__.tag_tipo = "Cliente"
            )
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json
                (
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                )
            }
        );

        trigger log_insert after insert for each when (
            __new__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user_id := __new__.user_id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each when (
            __old__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__{*}
            }
        );
    }

    type PessoaJuridica extending People {
        user: User;
        cnpj: str;
        responsavel: str;
        tipo_empresa: str;
        atividade_principal: str;
        inscricao_municipal: str;
        inscricao_estadual: str;

        trigger log_update after update for each when (
            (
                <json>__old__{*} != <json>__new__{*}
            ) and (
                __old__.tag_tipo = "Cliente"
            )
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json
                (
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                )
            }
        );

        trigger log_insert after insert for each when (
            __new__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user_id := __new__.user_id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each when (
            __old__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    type User extending People {
        required password: str;
        salt: str;

        multi conta: Conta;
        links_Service: .<user[is Service];
        links_ClientesPF: .<user[is PessoaFisica];
        links_ClientesPJ: .<user[is PessoaJuridica];
        links_Transaction: .<user[is Transacao];
        links_Pagamentos: .<user[is Pagamento];
        link_Evento::= .<user[is Scheduler];

        trigger log_update after update for each when (
            <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user_id := __old__.id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json
                (
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                )
            }
        );

        trigger log_insert after insert for each do (
            insert Auditable {
                user_id := __new__.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user_id := __old__.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    # type Processo extending Service {
    #     fase: str;
    #     classe: str;
    #     tipo: str;
    #     rito: str;
    #     forum: str;
    #     comarca: str;
    #     vara: str;
    # }

    type Transacao {
        user_id: .<user[is User];
        nome: str;
        valor: float32;
        parcelas: int16;
        periodicidade: str;
        tag_tipo: str;
        efetivado: bool {
            default := false;
        };
        categoria: str;
        subcategoria: str;
        conta: Conta;
        multi pagamento: Pagamento;
            on source delete delete target;
            on target delete allow;
        };


        trigger log_update after update for each when (
            <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json
                (
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                )
            }
        );

        trigger log_insert after insert for each do (
            insert Auditable {
                user_id := __new__.user_id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user_id := __old__.user_id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    type Pagamento {
        user: User;
        transacao: Transacao;
        valor: float32;
        data_pagamento: datetime;
        status: bool{
            default:= false;
        };
        parcela: int16;
        evento: Scheduler {
            on source delete delete target;
        }


        trigger update_saldo_on_insert after insert for each when (
            __new__.status = true
        ) do (
            update Conta filter .id = __new__.conta.id set {
                saldo := .saldo + __new__.valor,
            }
        );

        
        trigger update_saldo_on_delete after delete for each when (
            __old__.status = true
        ) do (
            update Conta filter .id = __old__.conta.id set {
                saldo := .saldo - __old__.valor
            }
        );

        trigger update_saldo_on_update after update for each when (
            (__old__.efetivado = true or __new__.efetivado = true) and (
                __old__.valor != __new__.valor or
                __old__.conta != __new__.conta or
                __old__.efetivado != __new__.efetivado
            )
        ) do (
            with update_account := (
                update Conta filter .id in {

                    __old__.conta.id, __new__.conta.id

                } set {
                    saldo := (.saldo - __old__.valor) if .id = __old__.conta.id 
                    else (.saldo + __new__.valor) if .id = __new__.conta.id 
                    else .saldo
                }

            ),
            new_efetivado := (
                update Conta filter .id = __old__.conta.id set {
                    saldo := .saldo + __old__.valor
                }
            ),
            not_efetivado := (
                update Conta filter .id = __old__.conta.id set {
                    saldo := .saldo - __old__.valor
                }
            )
            
            select update_account if (__old__.valor != __new__.valor or __old__.conta != __new__.conta) 
            else new_efetivado if __new__.efetivado = true
            else not_efetivado
        )

        # Quando um pagamento é efetivado ele verifica se todas as instancias de pagamento foram
        # efetivadas, se sim ele procura pela instancia de Finance para mudar seu status para efetivado
        trigger update_status_finance after update, insert for each when (
            __new__.status = true
        ) do (
            with finance_linked:= (select Finance filter .id = __new__.finance_id),
                pagamento_false:= (select Pagamento filter .id = __new__.finance_id and .status = false)
            update finance_linked {
                status:= not exists pagamento_false;
            }
        )

    }

    
}


