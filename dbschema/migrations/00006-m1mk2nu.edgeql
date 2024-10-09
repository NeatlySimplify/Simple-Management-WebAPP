CREATE MIGRATION m1mk2nuvewzke4v7y4tccgi55td6h56l4f77pcxeifsif7vvjed44q
    ONTO m1qcgqzexn266jndulu6udkl2spwmngxx2vfxud4z5daawca74ngsa
{
  CREATE TYPE default::Finance {
      CREATE LINK conta: default::Conta {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
      CREATE PROPERTY efetivado: std::bool {
          SET default := false;
      };
      CREATE PROPERTY valor: std::float32;
      CREATE TRIGGER update_saldo_on_delete
          AFTER DELETE 
          FOR EACH 
              WHEN ((__old__.efetivado = true))
          DO (UPDATE
              default::Conta
          FILTER
              (.id = __old__.conta.id)
          SET {
              saldo := (.saldo - __old__.valor)
          });
      CREATE TRIGGER update_saldo_on_insert
          AFTER INSERT 
          FOR EACH 
              WHEN ((__new__.efetivado = true))
          DO (UPDATE
              default::Conta
          FILTER
              (.id = __new__.conta.id)
          SET {
              saldo := (.saldo + __new__.valor)
          });
      CREATE MULTI LINK evento: default::Scheduler {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
      CREATE LINK user_id: default::User;
      CREATE PROPERTY categoria: std::str;
      CREATE PROPERTY details: std::str;
      CREATE PROPERTY nome: std::str;
      CREATE PROPERTY subcategoria: std::str;
      CREATE PROPERTY tag_tipo: std::str;
      CREATE TRIGGER log_delete
          AFTER DELETE 
          FOR EACH DO (INSERT
              default::Auditable
              {
                  user_id := <default::User>__old__.id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'delete',
                  details := <std::json>__old__ {
                      *
                  }
              });
      CREATE TRIGGER log_insert
          AFTER INSERT 
          FOR EACH DO (INSERT
              default::Auditable
              {
                  user_id := <default::User>__new__.id,
                  id_objeto := <std::uuid>__new__.id,
                  action := 'insert',
                  details := <std::json>__new__ {
                      *
                  }
              });
      CREATE TRIGGER log_update
          AFTER UPDATE 
          FOR EACH 
              WHEN ((<std::json>__old__ {
                  *
              } != <std::json>__new__ {
                  *
              }))
          DO (INSERT
              default::Auditable
              {
                  user_id := <default::User>__old__.id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'update',
                  details := std::to_json((((((('{' ++ '"before": ') ++ <std::str><std::json>__old__ {
                      *
                  }) ++ ',') ++ '"after": ') ++ <std::str><std::json>__new__ {
                      *
                  }) ++ '}'))
              });
  };
};
