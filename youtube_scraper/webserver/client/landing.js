Template.landing.events({
  'click #runScript' (event) {
    var cb = function(error, response) {
      console.log(response);
      Session.set("loadingData", false);
      Router.go("/view_image/" + $('#username').val())
    }
    Meteor.call("runScript", $('#username').val(), $('#password').val(), cb);
    Session.set("loadingData", true)
  },
});

Template.landing.helpers({
  loadingData: function() {
    return Session.get("loadingData");
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
