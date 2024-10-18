# Funciona com User, PessoaFisica e PessoaJuridica
update People filter .id = <uuid>$id set {
    endereco += (insert Endereco {
            rua:= <str>$rua,
            numero:= <str>$complemento,
            complemento:= <str>$complemento,
            bairro:= <str>$bairro,
            cep:= <str>$cep,
            cidade:= <str>$cidade,
            estado:= <str>$estado
        }
    )
}