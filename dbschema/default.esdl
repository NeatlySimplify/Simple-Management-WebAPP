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

        multi evento::= .<user_id[is Scheduler] {
            on source delete delete target if orphan;
            on target delete allow;
        };
        multi telefone: Telefone {
            on source delete delete target if orphan;
            on target delete allow;
        };
        multi endereco: Endereco {
            on source delete delete target if orphan;
            on target delete allow;
        };
    }

    abstract type Service {
        user_id: uuid;
        status: bool;
        valor: float32;
        categoria: str;
        details: str;

        multi evento: Scheduler {
            on source delete delete target if orphan;
            on target delete allow;
        };
        #multi finance: Finance {
        #    on source delete delete target if orphan;
        #    on target delete allow;
        #};
        multi pessoa: People {
            on source delete delete target if orphan;
            on target delete allow;
        };

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
        user_id: uuid;
        action: str;
        details: json;
    }

    type Scheduler {
        user_id: People;
        nome: str;
        status: bool {
            default:= false;
        };
        end_time: datetime;
        start_time: datetime;
        details: str;
        tag_tipo: str;
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
        user_id: uuid;
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
        user_id: uuid;
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

    type Processo extending Service {
        fase: str;
        classe: str;
        tipo: str;
        rito: str;
        forum: str;
        comarca: str;
        vara: str;
    }

    type Finance {
        user_id: uuid;
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
        details: str;
        conta: Conta;
        multi pagamento: .<finance[is Pagamento];
            
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
        user_id: uuid;
        finance: Finance;
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

    }

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


