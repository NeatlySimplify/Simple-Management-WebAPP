module default {

    type Admin {
        required name: str;
        required email: str;
        required password: str;
    }

    type Address {
        state: str;
        city: str;
        district: str;
        street: str;
        number: int16;
        complement: str;
        postal: str;
    }

    type Contact {
        number: str;
        contact: str;
        complement: str;
    }

    type Unit {
        user: User;
        required timestamp: datetime {
            default := datetime_of_statement();
        };
        required email: str {
            delegated constraint exclusive;
        };
        govt_id: str;
        template_model: str;
        name: str;
        sex: str;
        relationship: str;
        details: str;
        type_unit: str;
        birth: cal::local_date;
        single phone : Contact{
            on source delete delete target;
            on target delete allow;
        };
        single address : Address{
            on source delete delete target;
            on target delete allow;
        };
        custom_fields: json;

        trigger log_update after update for each when ( <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user := __old__.user.id,
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

        trigger log_insert after insert for each do (
            insert Auditable {
                user := __new__.user.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.user.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__{*}
            }
        );
    }

    type Service {
        user: User;
        id_Service: str;
        status: bool;
        value: float32;
        template_model: str;
        details: str;
        custom_fields: json;
        unit: Unit {
            on source delete delete target;
        };
        multi event: Scheduler {
            on source delete delete target;
            on target delete allow;
        };
        action: Action {
            on source delete delete target;
            on target delete allow;
        };

        trigger log_update after update for each when (
            <json>__old__{*} != <json>__new__{*}
        ) do (
            insert Auditable {
                user := __old__.user.id,
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
                user := __new__.user.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__{*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.user.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__{*},
            }
        );
    }

    type Templates {
        user: User;
        name: str;
        category: str;
        fields: json;
    }

    type Auditable {
        required timestamp: datetime {
            default := datetime_of_statement();
        };
        id_objeto: uuid;
        user: uuid;
        action: str;
        details: json;
    }

    type Scheduler {
        user: User;
        tag_type: str;
        origin: uuid;
        name: str;
        status: bool {
            default:= false;
        };
        end_date: cal::local_date;
        effective_date: cal::local_date;
        beginning_time: cal::local_time;
        end_time: cal::local_time;
        details: str;
    }

    type MonthlySumary {
        bank_account : BankAccount;
        year: int16;
        month: int16;
        expense: float64;
        income: float64;
    }

    type BankAccount {
        bankName: str;
        agency: str;
        accountNumber: str;
        balance: float64 {
            constraint min_value(0);
        };
        accountType: str;
        multi sumary : MonthlySumary {
            on source delete delete target;
        };

        trigger create_monthly_sumary_on_insert after insert for each do (
            with date := (datetime_of_statement()),
            sumary_year := (select <int16>to_str(date, "YYYY")),
            sumary_month := (select <int16><int16>to_str(date, "MM")),
            insert MonthlySumary {
                bank_account := __new__,
                year := sumary_year,
                month := sumary_month,
                income := __new__.balance
            }
        );
        trigger update_monthly_sumary after update for each do (
            with date := (datetime_of_statement()),
            sumary_year := (select <int16>to_str(date, "YYYY")),
            sumary_month := (select <int16><int16>to_str(date, "MM")),
            existing := (
                select __old__.sumary
                filter .year = sumary_year and .month = sumary_month
            ),
            diff_income := (select (__new__.balance - __old__.balance) if __new__.balance > __old__.balance else 0),
            diff_expense := (select (__old__.balance - __new__.balance) if __new__.balance < __old__.balance else 0)
            update existing set {
                income := .income + diff_income,
                expense := .expense + diff_expense
            }
        );
    }

    type User {
        required name: str;
        required email: str {
            constraint exclusive;
        };
        required password: str;
        isActive: bool{
            default := false;
        };
        lastActiveDate: datetime;
        multi account: BankAccount {
            on target delete allow;
            on source delete delete target;
        };
        year: json;

        # Usando backlinks para selecionar de modo dinâmico todas as entradas com o uuid do usuário
        # quando o usuário é deletado, todas as entradas ligadas ao usuário são excluidas.
        multi service : Service {
            on target delete allow;
            on source delete delete target;
        };
        multi unit : Unit {
            on target delete allow;
            on source delete delete target;
        };
        multi actions : Action {
            on target delete allow;
            on source delete delete target;
        };
        multi event : Scheduler {
            on target delete allow;
            on source delete delete target;
        };
        multi templates : Templates {
            on target delete allow;
            on source delete delete target;
        };

#        trigger log_update after update for each do (
#            insert Auditable {
#                user := __old__.id,
#                id_objeto := __old__.id,
#                action := "update",
#                details := to_json('{' ++ '"before": ' ++ <str><json>__old__{*} ++ ',' ++ '"after": ' ++ <str><json>__new__{*} ++'}')
#            }
#        );

        trigger log_insert after insert for each do (
            insert Auditable {
                user := __new__.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
        trigger link_delete after delete for each do (
            delete (select User.<user)
        );
    }

    type Action {
        user: User;
        name: str;
        value: float32;
        installment: int16;
        cycle: str;
        effective: bool {
            default := false;
        };
        category: str;
        subcategory: str;
        account: BankAccount;
        multi payment: Payment{
            on source delete delete target;
            on target delete allow;
        };

        trigger log_update after update for each when (
            <json>__old__ {*} != <json>__new__ {*}
        ) do (
            insert Auditable {
                user := __old__.user.id,
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
                user := __new__.user.id,
                id_objeto := __new__.id,
                action := "insert",
                details := <json>__new__ {*}
            }
        );

        trigger log_delete after delete for each do (
            insert Auditable {
                user := __old__.user.id,
                id_objeto := __old__.id,
                action := "delete",
                details := <json>__old__ {*}
            }
        );
    }

    type Payment {
        user: User;
        action: Action;
        value: float32;
        paymentDate: cal::local_date;
        isDue: cal::local_date;
        status: bool{
            default:= false;
        };
        part: int16;
        event: Scheduler {
            on source delete delete target;
        }

        # Updates balance on action.account.balance when insert Payment.
        trigger update_balance_on_insert after insert for each when (
            __new__.status = true
        ) do (
            update BankAccount filter .id = __new__.action.account.id set {
                balance := .balance + __new__.value
            }
        );

        # Updates balance on action.account.balance when delete Payment.
        trigger update_balance_on_delete after delete for each when (
            __old__.status = true
        ) do (
            update BankAccount filter .id = __old__.action.account.id set {
                balance := .balance - __old__.value
            }
        );

        # Updates from balance on action.account.balance when update Payment.
        trigger update_balance_on_update after update for each when (
            (__old__.status = true or __new__.status = true) and (
                __old__.value != __new__.value or
                __old__.action.account != __new__.action.account or
                __old__.status != __new__.status
            )
        ) do (
            with
                update_account := (update BankAccount filter .id in {
                    __old__.action.account.id, __new__.action.account.id} set {
                    balance := (.balance - __old__.value) if .id = __old__.action.account.id
                    else (.balance + __new__.value) if .id = __new__.action.account.id
                    else .balance}),
                new_effective := (update BankAccount filter .id = __old__.action.account.id set {
                    balance := .balance + __old__.value}),

                not_effective := (update BankAccount filter .id = __old__.action.account.id set {
                        balance := .balance - __old__.value})

            select update_account if (__old__.value != __new__.value or __old__.action.account != __new__.action.account)
            else new_effective if __new__.status = true
            else not_effective
        );

        # Updates Action.effective to TRUE if all instances associated to Action.payment has status equal to TRUE. The query is executed on each insert or update on Payment.
        trigger update_status_action after update, insert for each when (__new__.status = true) do (
            with action_linked:= (select Action filter .id = __new__.action.id),
            not_effective:= (select Payment filter .action = __new__.action and .status = false),
            update Action filter .id = action_linked.id set {effective:= (select not exists not_effective)}
        );

        # Insert Payment.event.
        trigger create_event after insert for each do (
            with data := ( insert Scheduler {
                user:= __new__.user,
                origin:= __new__.action.id,
                name:= __new__.action.name,
                status:= __new__.status,
                end_date:= __new__.isDue,
                effective_date:= __new__.paymentDate,
                tag_type:= "Action",
                }
            )
            update Payment filter .id = __new__.id set {
                event := data
            }
        );

        # Updates Payment.event.
        trigger update_event after update for each do (
            update __old__.event set {
                name:= __new__.action.name,
                status:= __new__.status,
                end_date:= __new__.isDue,
                effective_date:= __new__.paymentDate,
            }
        )
    }

    #Functions

    #Count Number of institutions or individuals from user
    function unitNum (user_id: str) -> int64
        using (
            with units := (select User filter .id = <uuid>user_id).unit
            select count(units)
        );

    # Count Number of Services from user
    function serviceNum (user_id: str) -> int64
        using (
            with services := (select User filter .id = <uuid>user_id).service
            select count(services)
        );

    ## Count Number of Transactions from user
    function transactionNum (user_id: str) -> int64
        using (
            with action := (select User filter .id = <uuid>user_id).actions
            select count(action)
        );

    # Count Number of Events from user
    function eventNum (user_id: str) -> int64
        using (
            with events := (select User filter .id = <uuid>user_id).event
            select count(events)
        );

    # Count Number of Templates from user
    function templatesNum (user_id: str) -> int64
        using (
            with template := (select User filter .id = <uuid>user_id).templates
            select count(template)
        );

    # Return total balance from user
    function balanceTotal (user_id: str) -> float64
        using (
            with total := (select User filter .id = <uuid>user_id).account
            select sum(total.balance)
        );

    #
}
