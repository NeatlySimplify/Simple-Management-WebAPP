select (insert Auditable {
    user_id := <uuid>$user,
    action := <str>$action,
    details := <json>$details
}) {
    timestamp,
    action,
    details
};