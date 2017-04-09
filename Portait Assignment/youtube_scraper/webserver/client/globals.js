renderDelay = 250;
transitionDelay = 750;

errorInput = function(id) {
  $(id).transition('bounce');
  $(id).addClass('error');
}
