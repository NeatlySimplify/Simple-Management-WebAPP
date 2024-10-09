select Auditable{
    timestamp,
    action,
    details
} filter .user_id = <uuid>$user;