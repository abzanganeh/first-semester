var target;
var guesses=0;
var col_name=["Red","Purple","Pink","Orange","Navy","Olive","Green","Cyan","Blue","Black","Yellow","Maroon","Lime"];
var finished=false;
var input_guess;
function colors(){
  target_index = Math.floor((Math.random()*13));
  col_name.sort();
  target = col_name[target_index];
  alert (target);
  while (!finished) {
    input_guess = prompt("I am thinking of one of these colors: \n\n"+col_name+" \n\n What color am I thinking of?\n\n");
    guesses++;
    function includ(col_name, guess_input){
      for(var i=0; i<col_name.length; i++){
        if (col_name[i] == guess_input) return true;
      }
    }
    finished = guess_input();
}

function guess_input(){
  if (includ==false)
{
  alert("ffffff");
}
if (guess_input<target)
{
  alert("<<<<<");
}
if (guess_input>target)
{
  alert(">>>>>");
}
else
{
  alert("ggod job!")
}
}
