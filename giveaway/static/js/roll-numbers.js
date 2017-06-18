$(document).ready(function(){
  $("#roll-button").click(function(){
    for(var i=0; i<rolled_numbers.length; i++){
      (function(i){
        setTimeout(function(){
          var $winning_number_display = $(".winning-number-display").eq(i);
          var $roll_number_display = $(".roll-number-display").eq(i);
          var winning_number = $winning_number_display.text();
          $roll_number_display.text(rolled_numbers[i]);
          if(rolled_numbers[i] == winning_number){
            //$(".winning-number-display").eq(i).css("background-color", "green");
            $roll_number_display.css("background-color", "green");
          }else{
            //$(".winning-number-display").eq(i).css("background-color", "red");
            $roll_number_display.css("background-color", "red");
          }
        }, 200 * i);
      }(i));
    }
  });
});
