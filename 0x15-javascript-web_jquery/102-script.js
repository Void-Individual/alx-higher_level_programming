$(document).ready(function() {
  $('#btn_translate').click(function() {
    const language = $('#language_code').val();
    const url = 'http://stefanbohacek.com/hellosalut/?lang=' + language;
    $.get(url, function(data, textStatus) {
      $('#hello').text(data.hello);
    });
  });
});
