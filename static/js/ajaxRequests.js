
export function getHtml(data, route) {
  if (data != 'undefined') {
    const jsonData = JSON.stringify(data);
    $.ajax({
      method: "GET",
      url: `${route}`,
      contentType: "html",
      data: jsonData,
      success: function (response) {
        $('#modal-body').html(response);
      },
      error: function (response) {
        alert(response.message)
      }
    });
  }
  else {
    $.ajax({
      method: "GET",
      url: `${route}`,
      contentType: "html",
      success: function (response) {
        $('#modal-body').html(response);
      },
      error: function (response) {
        alert(response.message)
      }
    });
  }
};

export function postData(data, route){
  const jsonData = JSON.stringify(data);
  $.ajax({
    method: "POST",
    url: `${route}`,
    contentType: "application/json",
    data: jsonData,
    success: function () {
      $("#modal-close-btn").click();
      location.reload()
    },
    error: function (response) {
      alert(response.message)
    }
  });
};

export function putData(data, resource_id, route) {
  const jsonData = JSON.stringify(data);
  $.ajax({
    method: "PUT",
    url: `${route}/${resource_id}`,
    contentType: "application/json",
    data: jsonData,
    success: function () {
      $("#modal-close-btn").click();
      location.reload()
    },
    error: function (response) {
      alert(response.message)
    }
  });
};

export function deleteData(resource_id, route) {
  $.ajax({
    method: "DELETE",
    url: `${route}/${resource_id}`,
    success: function () {
      $("#modal-close-btn").click();
      location.reload()
    },
    error: function (response) {
      alert(response.message)
    }
  });
};
