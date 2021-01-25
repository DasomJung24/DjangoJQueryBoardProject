$(document).on('ready page:load', function() {

  $(document).on('click', 'button.posting-delete', function() {
    let data = $("input:checkbox[name='checked']:checked").closest("form").serialize();
    console.log(data);
    console.log(1111111);
    var ajax_options = {
      beforeSend: function(xhr, settings) {
        var csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
        xhr.setRequestHeader('X-CSRFToken', csrftoken)
      },
      url: '/board/' + data.id,
      method: 'DELETE',
      statusCode: {
        200: function(data, status) {
            console.log(data);
        },
        404: function(xhr, status, error) {

        },
        500: function(xhr, status, error) {

        }
      }
    }
  $.ajax(ajax_options);
  })
});