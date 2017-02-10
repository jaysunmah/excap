Template.landing.events({
  'click #runScript' (event) {
    var cb = function(error, response) {
      console.log(response);
    }
    Meteor.call("runScript", $('#username').val(), $('#password').val(), cb);
  },
});

Template.landing.helpers({
  joiningGame: function() {
    return Session.get('joiningGame');
  },
});

Template.landing.onRendered(function() {
  if (Session.get('renderedLanding')) {
    $('#landingContainer').transition({
  		animation: 'fade right',
  		duration: transitionDelay,
  	});
  } else {
    Session.set('renderedLanding', true);
  	$('#landingContainer').transition({
  		animation: 'fade left',
  		duration: transitionDelay,
  	});
  }
});
