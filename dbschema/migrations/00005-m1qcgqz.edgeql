CREATE MIGRATION m1qcgqzexn266jndulu6udkl2spwmngxx2vfxud4z5daawca74ngsa
    ONTO m1kixgazrag7fazvdr277rzahpmo3pe77phtaxenmdozhdycslkn6q
{
  ALTER TYPE default::Auditable {
      ALTER LINK user_id {
          SET TYPE default::People;
      };
      CREATE PROPERTY id_objeto: std::uuid;
  };
  ALTER TYPE default::PessoaFisica {
      CREATE TRIGGER log_delete
          AFTER DELETE 
          FOR EACH 
              WHEN ((__old__.tag_tipo = 'Cliente'))
          DO (INSERT
              default::Auditable
              {
                  user_id := __old__.user_id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'delete',
                  details := <std::json>__old__ {
                      *
                  }
              });
      CREATE TRIGGER log_insert
          AFTER INSERT 
          FOR EACH 
              WHEN ((__new__.tag_tipo = 'Cliente'))
          DO (INSERT
              default::Auditable
              {
                  user_id := __new__.user_id,
                  id_objeto := <std::uuid>__new__.id,
                  action := 'insert',
                  details := <std::json>__new__ {
                      *
                  }
              });
      CREATE TRIGGER log_update
          AFTER UPDATE 
          FOR EACH 
              WHEN (((<std::json>__old__ {
                  *
              } != <std::json>__new__ {
                  *
              }) AND (__old__.tag_tipo = 'Cliente')))
          DO (INSERT
              default::Auditable
              {
                  user_id := __old__.user_id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'update',
                  details := std::to_json((((((('{' ++ '"before": ') ++ <std::str><std::json>__old__ {
                      *
                  }) ++ ',') ++ '"after": ') ++ <std::str><std::json>__new__ {
                      *
                  }) ++ '}'))
              });
  };
  ALTER TYPE default::PessoaJuridica {
      CREATE TRIGGER log_delete
          AFTER DELETE 
          FOR EACH 
              WHEN ((__old__.tag_tipo = 'Cliente'))
          DO (INSERT
              default::Auditable
              {
                  user_id := <default::User>__old__.user_id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'delete',
                  details := <std::json>__old__ {
                      *
                  }
              });
      CREATE TRIGGER log_insert
          AFTER INSERT 
          FOR EACH 
              WHEN ((__new__.tag_tipo = 'Cliente'))
          DO (INSERT
              default::Auditable
              {
                  user_id := <default::User>__new__.user_id,
                  id_objeto := <std::uuid>__new__.id,
                  action := 'insert',
                  details := <std::json>__new__ {
                      *
                  }
              });
      CREATE TRIGGER log_update
          AFTER UPDATE 
          FOR EACH 
              WHEN (((<std::json>__old__ {
                  *
              } != <std::json>__new__ {
                  *
              }) AND (__old__.tag_tipo = 'Cliente')))
          DO (INSERT
              default::Auditable
              {
                  user_id := __old__.user_id,
                  id_objeto := <std::uuid>__old__.id,
                  action := 'update',
                  details := std::to_json((((((('{' ++ '"before": ') ++ <std::str><std::json>__old__ {
                      *
                  }) ++ ',') ++ '"after": ') ++ <std::str><std::json>__new__ {
                      *
                  }) ++ '}'))
              });
  };
  ALTER TYPE default::Service {
      CREATE TRIGGER log_delete
          AFTER DELETE 
          FOR EACH DO (INSERT
              default::Auditable
              {
                  user_id := __old__.user_id,
                  id_objeto := __old__.id,
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
                  user_id := __new__.user_id,
                  id_objeto := __new__.id,
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
                  user_id := __old__.user_id,
                  id_objeto := __old__.id,
                  action := 'update',
                  details := std::to_json((((((('{' ++ '"before": ') ++ <std::str><std::json>__old__ {
                      *
                  }) ++ ',') ++ '"after": ') ++ <std::str><std::json>__new__ {
                      *
                  }) ++ '}'))
              });
  };
  ALTER TYPE default::User {
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
      CREATE MULTI LINK conta: default::Conta;
  };
  ALTER TYPE default::Finance {
      DROP LINK conta;
      DROP LINK evento;
      DROP LINK user_id;
      DROP PROPERTY categoria;
      DROP PROPERTY details;
      DROP PROPERTY efetivado;
      DROP PROPERTY nome;
      DROP PROPERTY subcategoria;
      DROP PROPERTY tag_tipo;
      DROP PROPERTY valor;
  };
  ALTER TYPE default::Service {
      DROP LINK finance;
      ALTER LINK evento {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
  };
  DROP TYPE default::Finance;
  ALTER TYPE default::People {
      ALTER LINK endereco {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
      ALTER LINK evento {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
      ALTER LINK telefone {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
  };
  ALTER TYPE default::Service {
      CREATE MULTI LINK pessoa: default::People {
          ON SOURCE DELETE DELETE TARGET IF ORPHAN;
          ON TARGET DELETE ALLOW;
      };
  };
};
