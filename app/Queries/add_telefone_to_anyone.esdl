# Funciona com User, PessoaFisica e PessoaJuridica
update People filter .id = <uuid>$id set {
    telefone += (insert Telefone {
            tipo:= <str>$tipo,
            ddd:= <str>$ddd,
            numero:= <str>$numero,
            contato:= <str>$contato,
            details:= <str>$details
        }
    )
}