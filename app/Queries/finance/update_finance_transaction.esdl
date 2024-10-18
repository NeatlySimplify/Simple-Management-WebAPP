update Finance filter .id = <uuid>$id set {
    nome:= <str>$nome if <str>$nome else .nome,
    valor:= <float32>$valor if <float32>$valor else .valor,
    tag_tipo:= <str>$tag_tipo if <str>$tag_tipo else .tag_tipo,
    efetivado:= <bool>$efetivado if <bool>$efetivado else .efetivado,
    categoria:= <str>$categoria if <str>$categoria else .categoria,
    subcategoria:= <str>$subcategoria if <str>$subcategoria else .subcategoria,
    details:= <str>$details if <str>$details else .details,
}