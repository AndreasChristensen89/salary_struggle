$(function () {

  $("#ajax").click(function () {
    $.ajax({
      url: '/grind/ajax-drink/',
      type: 'get',
      dataType: 'json',
      success: function (data) {
        $("#modal-book .modal-content").html(data.html_form);
      }
    });
  });

});