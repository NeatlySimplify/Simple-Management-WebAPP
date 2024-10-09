select Auditable {
    timestamp,
    action,
    details
}
filter .id = <uuid>$id;