$(function(){
  //----------------------------------------------------------------------------
  $.ajax({
    url: "/reclama_datos/",
    type: 'get',
    success: function(datos) {
      Visualiza_datos (datos);
    },
    failure: function(datos) {
      alert('esto no vá');
    }
  });
  //----------------------------------------------------------------------------
	function Visualiza_datos (datos) {
    var bares=[];
		var vis=[];

		bares =  datos['bares'];
		visitas = datos['visitas'];

    $('#container').highcharts({
      chart: {
        type: 'bar'
      },
      title: {
        text: 'Número de visitas a los bares'
      },
      xAxis: {
        categories: bares
      },
      yAxis: {
        title: {
          text: 'número de visitas'
        }
      },
      series: [
        {
          name: 'Visitas',
          data: visitas
        },
      ],
    });

	};
  //----------------------------------------------------------------------------
  $('.megusta').focus(function(){
    var identificadorboton;
    identificadorboton = $(this).attr("id");
    //alert(identificadorboton);

    $('#'+identificadorboton).click(function(){
      var tapaid;
      tapaid = $(this).attr("data-tapid");
      //alert(tapaid);
      $.get('/voto_tapa/', {tapa_id:tapaid}, function(data){
                 $('#like_count').html(data);
                 $('#'+identificadorboton).hide();
      });
    });


  });




});
