insert Finance {
    nome:= <str>$name,
    valor:= <float32>$valor,
    tag_tipo:= <str>$tag_tipo,
    efetivado:= <bool>$efetivada,
    categoria:= <str>$categoria,
    subcategoria:= <str>$subcategoria,
    details:= <str>$details,
} filter .id = <uuid>$id;