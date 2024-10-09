CREATE MIGRATION m1jr3cb3tcfcqtnftgu2jscehphp6ckvz6zcdz4y7tih43nwpl6dxa
    ONTO m1vtfnr24ffyer3scxblzxvyix7hcyig2xwbpjaba6o3iocv77ggla
{
  ALTER TYPE default::Finance {
      CREATE TRIGGER update_saldo_on_update
          AFTER UPDATE 
          FOR EACH 
              WHEN ((((__old__.efetivado = true) OR (__new__.efetivado = true)) AND (((__old__.valor != __new__.valor) OR (__old__.conta != __new__.conta)) OR (__old__.efetivado != __new__.efetivado))))
          DO (WITH
              update_account := 
                  (UPDATE
                      default::Conta
                  FILTER
                      (.id IN {__old__.conta.id, __new__.conta.id})
                  SET {
                      saldo := ((.saldo - __old__.valor) IF (.id = __old__.conta.id) ELSE ((.saldo + __new__.valor) IF (.id = __new__.conta.id) ELSE .saldo))
                  })
              ,
              new_efetivado := 
                  (UPDATE
                      default::Conta
                  FILTER
                      (.id = __old__.conta.id)
                  SET {
                      saldo := (.saldo + __old__.valor)
                  })
              ,
              not_efetivado := 
                  (UPDATE
                      default::Conta
                  FILTER
                      (.id = __old__.conta.id)
                  SET {
                      saldo := (.saldo - __old__.valor)
                  })
          SELECT
              (update_account IF ((__old__.valor != __new__.valor) OR (__old__.conta != __new__.conta)) ELSE (new_efetivado IF (__new__.efetivado = true) ELSE not_efetivado))
          );
  };
  ALTER TYPE default::Finance {
      DROP TRIGGER update_saldo_on_update_change_conta_or_valor;
  };
};
