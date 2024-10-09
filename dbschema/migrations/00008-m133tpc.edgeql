CREATE MIGRATION m133tpcldxyqd3pvznjiifevjhmskvfqxqlpwhjyquuqaqmiskraia
    ONTO m1yanfobrnipnpble2glbyjdqgreqnq37mnbgtn3hcdlamk5eb2cuq
{
  ALTER TYPE default::Finance {
      ALTER TRIGGER update_saldo_on_update_change_conta_or_valor USING (UPDATE
          default::Conta
      FILTER
          (.id IN {__old__.conta.id, __new__.conta.id})
      SET {
          saldo := (SELECT
              (IF (.id = __new__.conta.id) THEN (.saldo + __new__.valor) ELSE .saldo)
          )
      });
  };
};
