$(document).ready(function () {


    //map initialisation, with latitude and logitude expected
    function initMap(latitude, longitude) {
              var coordinates = {lat: latitude, lng: longitude};

              maps = document.querySelectorAll(".map")
              // selector using one, by class Name or .map : maps = document.getElementsByClassName("map");

              var map = new google.maps.Map(maps[0], {
                zoom: 15,
                center: coordinates
              });
              // using a marker on the center of the map as expected.
              var marker = new google.maps.Marker({
                position: coordinates,
                map: map
              });
            }



  $('form').on('submit'
  , function (click) {
      //preventing standard behaviour of submit
      event.preventDefault();
      //ajax on URL town_list_process
      var url = '/town_list_process';
      $.ajax({
        url: url
        , type: 'GET'
        , data: {
                'proglang' : $('#proglang').val()
                }
        , dataType: 'text'
        , beforeSend: function () { $("#spin").show(); }
        , complete: function () { $("#spin").hide(); }
        , success: function (data) {
            var town_output = JSON.parse(data);
            var output = $('#output');
            var response = $('<div class="response"></div>');
            var grandpy = $('<p></p>').text('Aaaaaah mais '+ town_output.name_r +', bien sur que je connais !');
            var wikipedia = $('<p></p>').text('D\' ailleurs, savais tu à ce propos que '+ town_output.wikipediaresult.summary);
            var lien = $('<a></a>').attr('href', town_output.wikipediaresult.url).text('En savoir plus');

            var lat = town_output.lat
            var lng = town_output.lng
            var newmap = $('<div class="map"></div>');

            wikipedia.append(lien);
            response.append(grandpy, wikipedia, newmap);
            output.prepend(response);

            initMap(lat, lng);


        }


        , error: function (data) {
            console.log(data);
            $('#output').append('<br> Désolé mon petit, je peux seulement te dire que ' + data.statusText);
        }
    })
  })
})