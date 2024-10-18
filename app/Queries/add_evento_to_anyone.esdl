# Funciona com User, PessoaFisica e PessoaJuridica
update People filter .id = <uuid>$id set {
    evento += (insert Scheduler {
            user_id:= <uuid>$user_id,
            nome := <str>$nome,
            status:= <bool>$status,
            end_time:= <datetime>$end_time,
            start_time:= <datetime>$start_time,
            details:= <str>$details,
            tag_tipo:= <str>$tag_tipo
        }
    )
}