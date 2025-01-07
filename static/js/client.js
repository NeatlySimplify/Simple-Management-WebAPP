import { getHtml, postData, putData, deleteData } from './ajaxRequests.js'

const CLIENT = {
    base: '/client/',
    form: '/client/form',
};

function fetchFormData(){
    const form = $('#client-form');
    let id = '';
    let govt_id_pf = form.find('input=[name="govt-id-pf"]').val();
    let govt_id_pj = form.find('input=[name="govt-id-pj"]').val();
    id = govt_id_pf.lenght > 0 ? govt_id_pf : govt_id_pj;
    const addressDict = {
        street: form.find('input=[name="street"]').val(),
        number: form.find('input=[name="address-number"]').val(),
        complement: form.find('input=[name="address-complement"]').val(),
        state: form.find('select=[name="state"]').val(),
        city: form.find('input=[name="city"]').val(),
        district: form.find('input=[name="district"]').val(),
        postal: form.find('input=[name="postal"]').val(),
    };
    const phoneDict = {
        number: form.find('input=[name="phone-number"]').val(),
        contact: form.find('input=[name="phone-contact"]').val(),
        details: form.find('textarea=[name="phone-details"]').val(),
    };
    const data = {
        name: form.find('input=[name="name"]').val(),
        email: form.find('input=[name="email"]').val(),
        sex: form.find('select=[name="sex"]').val(),
        relationship: form.find('select=[name="relationship"]').val(),
        typeClient: form.find('select=[name="type-client"]').val(),
        govt_id: id,
        birthdate: form.find('input=[name="birthdate"]').val(),
        details: form.find('textarea=[name="details"]').val(),
        phone: phoneDict,
        address: addressDict
    };
    return data
}

export function getPartial(data, route=CLIENT.base){
    getHtml(data=data, route=route);
};

export function getForm(route=CLIENT.form){
    getHtml(route=route)
}

export function postClient(route=CLIENT.base) {
    data = fetchFormData()
    postData(route=route, data=data)
};

export function updateForm(data, route=CLIENT.form){
    getHtml(route=route, data=data)
};

export function updateClient(resource_id, route=CLIENT.base){
    data = fetchFormData();
    putData(data, resource_id, route)
}

export function deleteClient(data, route=CLIENT.base) {
    deleteData(route, data)
}