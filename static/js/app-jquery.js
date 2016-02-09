

$(document).ready( function() {
  //Funcion para hacer mas pequeña la letra
  //--------------------------------------------------------------------------
  var tam_letra_original = parseFloat($('body').css('font-size'));

  $("#btn-pequena").click( function(event) {
    var tam_letra_actual = parseFloat($('body').css('font-size'));
    var tam_letra_peq=tam_letra_actual*0.9;
    if (tam_letra_peq<7.44) {
      tam_letra_peq=7.44;
    }
    $('body').css('font-size',tam_letra_peq);
  });
  //Funcion para hacer mas grande la letra
  //--------------------------------------------------------------------------
  $("#btn-grande").click( function(event) {
    var tam_letra_actual = parseFloat($('body').css('font-size'));
    var tam_letra_gran=tam_letra_actual*1.1;
    if (tam_letra_gran>29.00) {
      tam_letra_gran=29.00;
    }
    $('body').css('font-size',tam_letra_gran);
  });
  //Funcion para establecer la letra original
  //--------------------------------------------------------------------------
  $("#btn-normal").click( function(event) {
    $('body').css('font-size',tam_letra_original);
  });
  //--------------------------------------------------------------------------
});
