module default {

    abstract type People {
        required timestamp: datetime {
            default := datetime_of_statement();
        };
        required email: str {
            delegated constraint exclusive;
        };
        nome: str;
        sexo: str;
        estado_civil: str;
        details: str;
        tag_tipo: str;
        nascimento: datetime;
        cidade_atual: str;
        estado_atual: str;

        # multi telefone: Phone {
        #     on source delete delete target if orphan;
        #     on target delete allow;
        # };
        # multi endereco: Endereco {
        #     on source delete delete target if orphan;
        #     on target delete allow;
        # };
        telefone: json;
        endereco: json;
    }

    type Service {
        id_Service: str;
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
        finance: Transacao {
            on source delete delete target if orphan;
            on target delete allow;
        };

        trigger log_update after update for each when (
            <json>__old__{*} != <json>__new__{*}
        ) do (
            insert Auditable {
                user := __old__.user,
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
                user := __new__.user,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.user,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__{*},
            }
        );
    }

    type ServiceTemplate {
        user: User;
        name: str;
        fields: json;
    }

    # type Phone {
    #     tipo: json;
    #     numero: str;
    #     contato: str;
    #     details: str;
    # }

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
        auto_change_status: bool {
            default:= false;
        };
    }

    type Conta {
        bankName: str;
        agency: str;
        accountNumber: str;
        saldo: float32;
        tipo_conta: str;
    }

    # type Endereco {
    #     rua: str;
    #     numero: str;
    #     complemento: str;
    #     bairro: str;
    #     cep: str;
    #     cidade: str;
    #     estado: str;
    # }

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
            (<json>__old__ {*} != <json>__new__ {*}) and (__old__.tag_tipo = "Cliente")
        ) do (
            insert Auditable {
                user := __old__.user,
                id_objeto := __old__.id,
                action := "update",
                details := to_json(
                    '{' ++
                    '"before": ' ++ <str><json>__old__{*} ++ ',' ++
                    '"after": ' ++ <str><json>__new__{*} ++
                    '}'
                ),
            }
        );

        trigger log_insert after insert for each when (
            __new__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user := __new__.user,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each when (
            __old__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user := __old__.user,
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
                user := __old__.user,
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
                user := __new__.user,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each when (
            __old__.tag_tipo = "Cliente"
        ) do (
            insert Auditable {
                user := __old__.user,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    type User extending People {
        required password: str;
        conta_ativa: bool{
            default := true;
        };
        ultimo_login: datetime{
            default := datetime_of_statement();
        };
        multi conta: Conta {
            on target delete allow;
            on source delete delete target;
        };

        # Usando backlinks para selecionar de modo dinâmico todas as entradas com o uuid do usuário
        # quando o usuário é deletado, todas as entradas ligadas ao usuário são excluidas.
        multi service := (.<user[is Service]);
        multi clientesPF := (.<user[is PessoaFisica]);
        multi clientesPJ := (.<user[is PessoaJuridica]);
        multi transactions := (.<user[is Transacao]);
        multi evento := (.<user[is Scheduler]);

        trigger log_update after update for each when (
            <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user := <User>__old__.id,
                id_objeto := __old__.id,
                action := "update",
                details := to_json('{' ++ '"before": ' ++ <str><json>__old__{*} ++ ',' ++ '"after": ' ++ <str><json>__new__{*} ++'}')
            }
        );

        trigger log_insert after insert for each do (
            insert Auditable {
                user := <User>__new__.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := <User>__old__.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    type Transacao {
        user: User;
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
        multi pagamento: Pagamento{
            on source delete delete target;
            on target delete allow;
        };

        trigger log_update after update for each when (
            <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user := __old__.user,
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
                user := __new__.user,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.user,
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
            update Conta filter .id = __new__.transacao.conta.id set {
                saldo := .saldo + __new__.valor
            }
        );


        trigger update_saldo_on_delete after delete for each when (
            __old__.status = true
        ) do (
            update Conta filter .id = __old__.transacao.conta.id set {
                saldo := .saldo - __old__.valor
            }
        );

        trigger update_saldo_on_update after update for each when (
            (__old__.status = true or __new__.status = true) and (
                __old__.valor != __new__.valor or
                __old__.transacao.conta != __new__.transacao.conta or
                __old__.status != __new__.status
            )
        ) do (
            with
                update_account := (update Conta filter .id in {
                    __old__.transacao.conta.id, __new__.transacao.conta.id} set {
                    saldo := (.saldo - __old__.valor) if .id = __old__.transacao.conta.id
                    else (.saldo + __new__.valor) if .id = __new__.transacao.conta.id
                    else .saldo}),

                new_efetivado := (update Conta filter .id = __old__.transacao.conta.id set {
                    saldo := .saldo + __old__.valor}),

                not_efetivado := (update Conta filter .id = __old__.transacao.conta.id set {
                        saldo := .saldo - __old__.valor})

            select update_account if (__old__.valor != __new__.valor or __old__.transacao.conta != __new__.transacao.conta)
            else new_efetivado if __new__.status = true
            else not_efetivado
        );
        trigger update_status_finance after update, insert for each when (__new__.status = true) do (
            with finance_linked:= (select Transacao filter .id = __new__.transacao.id),
            pagamento_false:= (select Pagamento filter .transacao = __new__.transacao and .status = false),
            update Transacao filter .id = finance_linked.id set {efetivado:= (select not exists pagamento_false)}
        );

    }
}
