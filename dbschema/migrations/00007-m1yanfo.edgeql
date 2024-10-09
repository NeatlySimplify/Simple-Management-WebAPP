CREATE MIGRATION m1yanfobrnipnpble2glbyjdqgreqnq37mnbgtn3hcdlamk5eb2cuq
    ONTO m1mk2nuvewzke4v7y4tccgi55td6h56l4f77pcxeifsif7vvjed44q
{
  ALTER TYPE default::Finance {
      CREATE TRIGGER update_saldo_on_update_change_conta_or_valor
          AFTER UPDATE 
          FOR EACH 
              WHEN ((((__old__.efetivado = true) OR (__new__.efetivado = true)) AND ((__old__.valor != __new__.valor) OR (__old__.conta != __new__.conta))))
          DO (UPDATE
              default::Conta
          FILTER
              (.id IN {__old__.conta.id, __new__.conta.id})
          SET {
              saldo := (IF (.id = __old__.conta.id) THEN (.saldo - __old__.valor) ELSE .saldo)
          });
  };
};
