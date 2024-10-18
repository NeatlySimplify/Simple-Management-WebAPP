insert PessoaJuridica {
    user_id:= <User><uuid>$user_id
    nome:= <str>$nome,
    email:= <str>$email,
    nascimetno:= <datetime>$nascimento,
    sexo:= <str>$sexo,
    estado_civil:= <str>$estado_civil,
    tag_tipo:= <str>$tag_tipo,
    details:= <str>$detail,
    cnpj:= <str>$cnpj,
    responsavel:= <str>$responsavel,
    tipo_empresa:= <str>$tipo_empresa,
    atividade_principal:= <str>$atividade_principal,
    inscricao_municipal:= <str>$inscricao_municipal,
    inscricao_estadual:= <str>$inscricao_estadual
}