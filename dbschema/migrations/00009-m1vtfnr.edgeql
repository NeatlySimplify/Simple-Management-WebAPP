CREATE MIGRATION m1vtfnr24ffyer3scxblzxvyix7hcyig2xwbpjaba6o3iocv77ggla
    ONTO m133tpcldxyqd3pvznjiifevjhmskvfqxqlpwhjyquuqaqmiskraia
{
  ALTER TYPE default::Finance {
      ALTER TRIGGER update_saldo_on_update_change_conta_or_valor USING (UPDATE
          default::Conta
      FILTER
          (.id IN {__old__.conta.id, __new__.conta.id})
      SET {
          saldo := ((.saldo - __old__.valor) IF (.id = __old__.conta.id) ELSE ((.saldo + __new__.valor) IF (.id = __new__.conta.id) ELSE .saldo))
      });
  };
};
